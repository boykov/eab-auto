#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""

import csv
import sys

ifl = open(sys.argv[1],"rb")

rdr = csv.reader(ifl)

ofl = open(sys.argv[2],"wb")

wrtr = csv.writer(ofl,dialect = 'excel')
for rec in rdr:
#    rc = [rec[2],rec[3],rec[6],rec[32],rec[33]
    rc = [rec[1],rec[0],rec[2],rec[3],rec[4],"dec"]
    wrtr.writerow(rc)
    
ifl.close()
ofl.close()


