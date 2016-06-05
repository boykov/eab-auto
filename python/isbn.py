#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Осуществляется поиск книг по номеру isbn на российском ресурсе, после 1996 года издания.
"""

import urllib
import sys
import re

lst = ['5-02-013784-7'] # ['5-8459-0791-8','978-5-93286-130-1'] #'5-279-03066-X','978-5-469-01413-3','5-9511-0014-3','5-93208-189-9','978-5-93286-149-3','978-5-93286-138-7','985-438-994-4'] # bad: '0-387-95352-3','1-56592-112-7' похоже, что только для русских книг # 1995 '5-7101-0059-5' - не подходит

for isbn in lst:
    a = urllib.urlretrieve(u'http://rbip.bookchamber.ru/search.aspx?F200a=&F700a=&F210c=&F225a=&F9071=&F010a='+isbn+'&F210d=&status_no=&description_type_no=&format_date=ddmmyyyy&news=&validate_no=&page_size=20&Submit1=+%D0%B8%D1%81%D0%BA%D0%B0%D1%82%D1%8C+')

    infile = open(a[0], 'r').readlines()
    for l in infile:
        if re.search("span class=\"biblioCaption\"",l) <> None:
            print (l.decode("cp1251")).encode("utf-8") # Обратное encode нужно, чтобы понимал shell-command-output 
#            print l.decode("cp1251") # в bash работает и так и так


