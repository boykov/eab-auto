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
flg = False
tmp = [1]
tmpoct=[]
tmpdec=[]
tmpnov=[]
arpu3low = 999999
for rec in rdr:
    rc = []
    if (tmp[0]<>rec[0]) and flg:
        if tmpoct<>[] and tmpnov<>[] and tmpdec<>[]:
            arpu3low = int(tmpoct[3])+int(tmpnov[3])+int(tmpdec[3])
        else:
            arpu3low = 999999
        # if arpu3low < 135:
        # if tmpoct<>[]:            
        #     wrtr.writerow([tmpoct[1],tmpoct[0],tmpoct[2],tmpoct[3],tmpoct[4],tmpoct[5]])
        # if tmpnov<>[]:            
        #     wrtr.writerow([tmpnov[1],tmpnov[0],tmpnov[2],tmpnov[3],tmpnov[4],tmpnov[5]])
        # if tmpdec<>[]:
        #     wrtr.writerow([tmpdec[1],tmpdec[0],tmpdec[2],tmpdec[3],tmpdec[4],tmpdec[5]])
        rc.append(tmp[1])
        rc.extend(tmpoct)
        rc.extend(tmpnov)
        rc.extend(tmpdec)
        wrtr.writerow(rc)
        tmpoct=[]
        tmpnov=[]
        tmpdec=[]
    flg = True
    tmp = rec
    if tmp[5]=="dec":
        tmpdec=tmp
    if tmp[5]=="oct":
        tmpoct=tmp
    if tmp[5]=="nov":
        tmpnov=tmp
                
if tmpoct<>[] and tmpnov<>[] and tmpdec<>[]:
    arpu3low = int(tmpoct[3])+int(tmpnov[3])+int(tmpdec[3])
else:
    arpu3low = 999999
# if arpu3low < 135:
# if tmpoct<>[]:            
#     wrtr.writerow([tmpoct[1],tmpoct[0],tmpoct[2],tmpoct[3],tmpoct[4],tmpoct[5]])
# if tmpnov<>[]:            
#     wrtr.writerow([tmpnov[1],tmpnov[0],tmpnov[2],tmpnov[3],tmpnov[4],tmpnov[5]])
# if tmpdec<>[]:
#     wrtr.writerow([tmpdec[1],tmpdec[0],tmpdec[2],tmpdec[3],tmpdec[4],tmpdec[5]])

rc.extend(tmpoct)
rc.extend(tmpnov)
rc.extend(tmpdec)
wrtr.writerow(rc)


ifl.close()
ofl.close()


