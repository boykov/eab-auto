#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# (eepitch-shell)

"""

import hronlib
import os,shutil
import time,datetime,re
import csv
import sys
import hronlib
import random



def doFile(inputFile,outputFile,processFile):
    """
    Split inputFile to matchedFile and restFile with using conditions in processFile and pattern.
    """
    ifl = open(inputFile,"rb")
    rdr = csv.reader(ifl)
    ofl = open(outputFile,"wb")
    wtr = csv.writer(ofl,dialect = 'excel')
    processFile(rdr,wtr)
    ifl.close()
    ofl.close()    


def makeFile(inputFile):
    outputFile =  inputFile +  "-out"
    doFile(inputFile,outputFile,addTime)


def addTime(rdr,wtr):
    """
    """
    mas = []
    for rec in rdr:
        try:
            if rec[2] == "":
                hours = 0
            else:
                hours = int(rec[2])
            if rec[3] == "":
                minutes = 0
            else:
                minutes = int(rec[3])
            allmin = str(hours * 60 + minutes)
            wtr.writerow([rec[0],rec[1],allmin])
            if mas <> []:
                for m in mas:
                    m.append(allmin)
                    wtr.writerow(m)
            mas = []
        except:
            mas.append(rec)


def identy(rdr,wtr):
    """
    Identical processing. Input = Output
    """
    for rec in rdr:
        wtr.writerow(rec)

if __name__ == '__main__':
    """
    ./do.py
    ./do.py input.csv output &
    ps -e | grep bash
    """
    finput = sys.argv[1]
    makeFile(finput)
