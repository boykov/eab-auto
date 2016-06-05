#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pytils

def enc(input):
    return input.decode("utf-8")

print pytils.translit.translify(enc(sys.argv[1]))
