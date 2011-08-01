#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Составляются множества, описывающие данные хронометража, напр. clus, clus2.
(Аналогично, можно добавлять выборку типа < grep keyword > и т.п.)
Отчет (report) формируется с использованием этих множеств.
"""

import hronlib

HRONFILE =  "analizatorOO.csv"

hData = open(HRONFILE, 'r').readlines()

def extractSet(data,actions):
    """
    Get hron data and list of actions on set. Return tuple of answers.
    Actions on list not implemented.
    """
    total = []
    clus = {}
    for doit in actions.keys():
        clus[doit] = set([])
    #
    for line in data:
        for doit in actions.keys():
            r = doit(line)
            clus[doit].add(r)
    #
    for doit in actions.keys():
        clus[doit].add("")
        clus[doit].remove("")
        total.append(clus[doit])
    return tuple(total)

def printSet(s):
    """
    Print selection from hron data.
    """
    res = ""
    for l in s:
        res = res + "," + l
    print res[1:]
    print "total length =",len(s)

def printReport():
    clus1,clus2 = extractSet(hData, {hronlib.cluster1:set,hronlib.cluster2:set})
    map(printSet,[clus1,clus2])
    minutes = reduce(lambda x,y: x + y, map(hronlib.count_min,hData))
    minuteG = hronlib.getMinutesFrom(hData[-1])
    print minutes, " minutes with ::"
    print minuteG, " minutes"
    print minutes / float(minuteG), " koef"
    end = hData[-1]
    beg = hData[0]
    print hronlib.num_month(end) - hronlib.num_month(beg), "months"
    print hronlib.num_week(end) - hronlib.num_week(beg), "weeks"
    print (hronlib.getMinutesFrom(end)), "mins"
    print (hronlib.getMinutesFrom(end)/60), "hours"
    print minutes, "mins with ::"
    print minutes/60, "hours with ::"
    print "1% from total hours = ", minutes/6000



if __name__ == '__main__':
    printReport()
