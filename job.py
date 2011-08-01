#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""

import urllib
import sys
import re
import os

# add saving results 2org

print "--------------------------------------------------------------------------------"

pathContentRetrieved = urllib.urlretrieve(u'http://prezent-khv.ru/print/present/2010/3/work12')
contentRetrieved = open(pathContentRetrieved[0], 'r').readlines()

# Extract content from fourth string and parse it
cnt = contentRetrieved[3].decode("cp1251").encode("utf8")
content = cnt.split("nbsp")[2:]
for l in content:
    print (l.split("<br>")[0])[1:]
    print "--------------------------------------------------------------------------------"

print "--------------------------------------------------------------------------------"

pathContentRetrieved = urllib.urlretrieve(u'http://www.rabota27.ru/vca-1-1.html')
contentRetrieved = open(pathContentRetrieved[0], 'r').readlines()
for l in contentRetrieved:
    content = l.decode("cp1251").encode("utf8")
    if re.search("vacancy-",content) <> None:
        link = "http://www.rabota27.ru/printv.php?v=" + (content.split("vacancy-")[1]).split("html")[0][:-1]
        os.system("w3m " + link + " && echo --------------------------------------------------------------------------------")
#        break # test on first item

print "--------------------------------------------------------------------------------"

pathContentRetrieved = urllib.urlretrieve(u'http://habarovsk.superjob.ru/rabota/547/informacionnye-tehnologii/')
contentRetrieved = open(pathContentRetrieved[0], 'r').readlines()
for l in contentRetrieved:
    content = l.decode("cp1251").encode("utf8")
    pattern = "vacancy/"
    if re.search(pattern,content) <> None:
        idd = (content.split(pattern)[1]).split("html")[0][0:12]
        if idd[1:3]=="id":
            link = "http://habarovsk.superjob.ru/print/vacancy/" + idd
            os.system("w3m " + link + " && echo --------------------------------------------------------------------------------")
#            break # test on first item


