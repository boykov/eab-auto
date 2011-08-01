#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""

import urllib
import sys
import re
import os
# a = urllib.urlretrieve(u'http://prezent-khv.ru/print/present/2010/3/work12')

# infile = open(a[0], 'r').readlines()
# begin = False
# # for l in infile:
# el = infile[3].decode("cp1251").encode("utf8")
# # if re.search("&nbsp;&nbsp;",el) <> None:
# #     lst = el.split("div")
# #     print lst[0][12:-2] # Обратное encode нужно, чтобы понимал shell-command-output
# lst = el.split("nbsp")
# for l in lst[2:]:
#     print (l.split("<br>")[0])[1:]
#     print "################################################################################"
# #            print l.decode("cp1251") # в bash работает и так и так



a = urllib.urlretrieve(u'http://www.rabota27.ru/vca-1-1.html')

infile = open(a[0], 'r').readlines()
begin = False
for l in infile:
    el = l.decode("cp1251").encode("utf8")
    if re.search("vacancy-",el) <> None:
        link = "http://www.rabota27.ru/printv.php?v=" + (el.split("vacancy-")[1]).split("html")[0][:-1]
        # cont = urllib.urlretrieve(link)
        os.system("w3m " + link + " && echo --------------------------------------------------------------------------------")
        break # test on first item
        # file = open(cont[0], 'r').readlines()
        # for f in file:
        #     print f.decode("cp1251").encode("utf8")
#            print l.decode("cp1251") # в bash работает и так и так

# TODO аналогично делать для
# http://habarovsk.superjob.ru/rabota/547/informacionnye-tehnologii/
# здесь проблема, w3m тупит:
# http://khabarovsk.irr.ru/jobs-education/vacancies/it/
# и т.д...Очевидно, надо делать функцию, которая бы единообразно обрабатывала
# подобные ссылки. Отключил ropemacs все равно тормозит. Отключил ropemacs и AC,
# все равно тормоза продолжаются. => дело в python-mode
# maybe in russian. Yes. When I print latin symbols no brakes
# adsfkl;aj a;dlskfj al;kj
# asdkfja aldkfj al alsdkfj aldksjf kla
# adkflja aldksfj lak adlkfj adkfj
# dkfaj a kdjfadfj adksfj a aldskfj aaaaa alsjdfk
# adf kjdf                           adsf jak
