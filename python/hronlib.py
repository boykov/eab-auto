#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
# (eepitch-shell)
python
import hronlib
import unittest

class hronlibTest(unittest.TestCase):
    def testNum(self):
        x = hronlib.test('2009-07-26 23:59,test one,1,10')
        y = (':week', 937, ':month', 234, ':min', 70, ':clu1', 'test')
        self.assertEquals(x,y)
        print x, ' equals ',y
    def testString2date(sefl):
        x = hronlib.string2date('01.02.09 10:15')
        y = '2009-02-01 10:15:00'

if __name__ == '__main__':
    unittest.main()

"""
import time,datetime,re,os
import unittest
import sympy

def splitEntry(hronString):
    return hronString.split(",")

def getDate(hronString):
    hron = splitEntry(hronString)
    YYYY = int(hron[0][0:4])
    MM =  int(hron[0][5:7])
    DD = int(hron[0][8:10])
    hh = int(hron[0][11:13])
    mm = int(hron[0][14:])
    return datetime.datetime(YYYY,MM,DD,hh,mm)

def getMinutes(hronString):
    return count_min(hronString)

def getCluster(hronString):
    return cluster1(hronString)

def getMinutesFrom(hronString,begDate=datetime.datetime(2007,01,01,00,00)):
    rstr = str(getDate(hronString) - begDate)
    dd = 0
    if "days" in rstr:
        dd = int(rstr.split(" days")[0])
    hh =  int(rstr[-8:-6])
    mm =  int(rstr[-5:-3])
    return dd * 24 * 60 +  hh * 60 + mm

def getMonthsFrom(hronString,begDate=datetime.datetime(2007,01,01,00,00)):
    return num_month(hronString)

def getWeeksFrom(hronString,begDate=datetime.datetime(2007,01,01,00,00)):
    return num_week(hronString)

def timelive(startDate,finishDate):
    duration = startDate - finishDate
    return duration.days + duration.seconds/3600./24

def parseDate(pattern):
    """
    
    Arguments:
    - `pattern`: like 'DD.MM.YY hh:mm'
    return slice of array,  e.g. for YY -  6:8
    """
    
def string2date(s):
    """
    Parse string like '01.02.09 10:15' to object datetime
    """
    YY = int(s[6:8])
    MM = int(s[3:5])
    DD = int(s[0:2])
    hh = int(s[9:11])
    mm = int(s[12:])
    try:
        if int(s[6])==9 or int(s[6])==8:
            return datetime.datetime(1900+YY,MM,DD,hh,mm)
        else:
            return datetime.datetime(2000+YY,MM,DD,hh,mm)
    except:
        return datetime.datetime(1980,1,1,0,0)

def difftime(hronList):
    """Take list like ['stuff','1','20'] and make timedelta(0,4800) in seconds  """
    hours = hronList[-2]
    minutes = hronList[-1]
    if hours=='':
        hours=0
    if minutes=='':
        minutes=0
    diff = datetime.timedelta(hours=int(hours),minutes=int(minutes))
    return diff

def nexttime(startDatetime,fShift):
    sD = startDatetime.split(",")
    YYYY = int(sD[0][0:4])
    MM =  int(sD[0][5:7])
    DD = int(sD[0][8:10])
    hh = int(sD[0][11:13])
    mm = int(sD[0][14:])
    tmp = str(datetime.datetime(YYYY,MM,DD,hh,mm) + fShift(sD))
    return tmp[:-3]

def org2dweek(orgString):
    year  = orgString[0:4]
    month = orgString[5:7]
    day   = orgString[8:10]
    a = datetime.date(int(year),int(month),int(day))
    daysweek = ['Пнд','Втр','Срд','Чтв','Птн','Сбт','Вск']
    return str(daysweek[a.isoweekday()-1])


def hron2org(hronString):
    start  = nexttime(hronString,lambda s: datetime.timedelta(0,0))
    finish = nexttime(hronString,difftime)
    start  = start[0:10]  +  " " + org2dweek(start[0:10]) + start[10:]
    finish = finish[0:10] +  " " + org2dweek(finish[0:10]) + finish[10:]
    return "  CLOCK: [" + start + "]--[" + finish  + "] =>  " + str(difftime(hronString.split(",")))[0:-3]


##############################################
##############################################
# don't need this code, because org-mode exist
def num_week(val):
    # take str (data time), 2009-07-23 18:40, return number of week
    # 2007.01.01:2007.01.07 week number 1
    # 2007.01.08:2007.01.15 week number 2 and so on...
    # the moment of the begining of hronometry - 01.01.2007
    return getMinutesFrom(val) / (60 * 24 * 7)
    
def num_month(val):
    # take str (data time), 2009-07-23 18:40, return number of week
    # 2007.01.01:2007.01.07 week number 1
    # 2007.01.08:2007.01.15 week number 2 and so on...
    return num_week(val)/4

def count_min(hronString):
    hronList=splitEntry(hronString)
    hours = hronList[-2:-1][0]
    minutes = hronList[-1:][0]
    # attention! here was trouble with \n - it comes from reading file
    if minutes=='\n' or minutes=='':
        minutes=0
    if hours=='':
        hours=0
    # return list
    return int(hours)*60+int(minutes)

def cluster1(hronString):
    """
    return name of 1-level cluster
    """
    text = splitEntry(hronString)[:][1]
    # next, parse "cluster-1 tail"->"cluster-1"
    return text.split(" ")[0]

def cluster2(hronString):
    text = splitEntry(hronString)[:][1]
    lst = text.split(" ")
    if len(lst) > 2:
        if lst[2] <> "ЖЖ":
            return str(lst[1])
    return ""

def test(val):
    # test some funcs
    return ":week",num_week(val),":month",num_month(val),":min",count_min(val),":clu1",cluster1(val)

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
