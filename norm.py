#!/usr/bin/python
# -*- coding: utf-8 -*-

import math

path =  '/home/john/git/difwave/test/uuinit/'

all = 0
for k in range(1,4,1):
    f1 = open(path +  'upr7' + str(k) +'.TXT','r').readlines()
    f2 = open('fortestupr7' + str(k) +'.TXT','r').readlines()
    i = 0
    sum = 0.0
    for l1 in f1:
        if l1 <> "" :
            if k<4:
                # извлекаем комплексные пары для 1 и 2 файлов
                v1,v2 = map(lambda y:
                              map(lambda x:
                                  x.strip().strip("()").strip(),y.split(",")),
                              (l1,f2[i]))
                c1,c2 = map(lambda lst:
                            complex(float(lst[0]),float(lst[1])),
                            (v1,v2))
                
                sum = sum + abs(c1 - c2) / abs(c1)
            else:
                sum = sum + math.fabs(float(l1)-float(f2[i])) / math.fabs(float(l1))

            i = i + 1
    all = all + sum / i

if all / 7 <0.2:
    print "OK --- norm.py: compare upr7x.TXT and fortestupr7x.TXT success."
    print all / 7
else:
    print "FAIL --- norm.py: compare upr7x.TXT and fortestupr7x.TXT failed."
    print all / 7
