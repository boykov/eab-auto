#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""

import xmltodict

text = open('/home/eab/git/org/clock/writecontact.xml','r').read()

result = xmltodict.parse(text)
print result

