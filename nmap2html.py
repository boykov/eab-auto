#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

a = os.popen("nmap localhost | grep open").read()

a = a.split("\n")

# b = map(lambda x:x.split(" ")[-1],a)[:-1]

a = map(lambda x: "<A HREF=\"http://192.168.0.107:" + x.split("/tcp")[0] + "\">"  + x.split("/tcp")[0] + " " + x.split(" ")[-1] +"</A><br>",a)

print "Content-type: text/html"
print ''

map(lambda x:sys.stdout.write(x), a[:-1])
