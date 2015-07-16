#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import tempfile

fltr = ["22", "25", "139", "143", "445", "631", "993", "3306"]

a = os.popen("nmap localhost | grep open").read()

a = a.split("\n")

a = filter(lambda x: x.split("/tcp")[0] not in fltr, a)

targets = map(lambda x: ["http://192.168.0.107:" + x.split("/tcp")[0],
                         x.split("/tcp")[0],
                         x.split(" ")[-1]],a)[:-1]

a = map(lambda x: """<A HREF="%s">%s %s</A><br>""" % tuple(x),targets)

print "Content-type: text/html"
print ''

map(lambda x:sys.stdout.write(x), a)

def f(t):
    return """"%s %s" [URL="%s", target = "_blank"];\n""" % (t[1],t[2],t[0])

nmap="""
graph G {
""" + "".join(map(f,targets)) + """
}
"""

dirpath = tempfile.mkdtemp(dir='/tmp')

open(dirpath + "/nmap.dot",'w').write(nmap)

os.system("dot -Tsvg " + dirpath + "/nmap.dot -o " + dirpath + "/nmap.svg")

print open(dirpath + "/nmap.svg",'r').read()

os.system("rm -rf " + dirpath)
