#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""

import urllib
import sys
import re
import os

# link = u"http://ru.wikipedia.org/wiki/%D0%AD%D0%BB%D0%BB%D0%B8%D0%BF%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9_%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%82%D0%BE%D1%80"

def short(lnk):
    a = urllib.urlretrieve(u"http://bit.ly/?s=&keyword=&url=" + lnk)
    infile = open(a[0], 'r').readlines()
    return (str(infile).split("""<textarea tabindex="3" class="tweet_body make_content_editable" id="tweet_body" name="tweet_body">""")[1]).split("""</textarea>""")[0]

if __name__ == '__main__':
    print short(sys.argv[1])
