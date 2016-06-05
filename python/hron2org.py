#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Convert file.rep => file.org
# Some abnormality of DRY principe
# Prepare rep-file:
# grep ",negative" analizatorOO.csv > negative.rep

import sys,os
import hronlib

# Parse entries of the form
# "Time" + "cluster-1 " +  "rest" + ",Hours,Minutes"

# length of Time position
lenTime = len("2007-01-01 00:00,")

list = open(sys.argv[1],'r').readlines()

# move cluster-1 on first position, before Time
list = map(lambda(s):s[lenTime:]+s[:lenTime],list)

# sort by cluster-1
list.sort()

# back cluster-1 on position after Time
list = map(lambda(s):s[-lenTime:]+s[:-lenTime],list)

clus2,clus1 = hronlib.extractSet(list, {hronlib.cluster1:set,hronlib.cluster2:set})

org = []

for l in list:
    l = l[:-1]
    nameEntry = l[lenTime:].split(",")[0]
    org.append("* " + nameEntry)
    org.append(hronlib.hron2org(l))

out = []
cand = org[0].split(",")[0][2:]

def iscluster2(string):
    lst = string.split(" ")
    if lst[-1] == "ЖЖ":
        if lst.__len__() == 4:
            return True
        else:
            return False
    else:
        if lst.__len__() == 3:
            return True
        else:
            return False

# extract cluster-1
# clus = cand.split()[0]
# print "* " + clus
clus2o = ""
clus = ""
cand = ""
# print "** " + "nocluster2"
# print "**" + org[0] # here org[0] already has one star => *** 
# previousCluster2 = False

i = 0
prevclock = False
for o in org[0:]:
    tmp = o.split(",")[0][2:]
    if tmp <> cand:
        # if o[1:6] <> 'CLOCK':
        if (o[0:9] <> '  CLOCK: '):
            # patch for clock
            if prevclock:
                pass
                # out.append('  :END:')
            prevclock = False
            # patch for clock end
            cltmp = tmp.split()[0]
            if clus == "":
                clus = cltmp
                out.append("* " + cltmp)
            if cltmp <> clus:
                out.append("* " + cltmp)
                clus = cltmp
                clus2o = ""
            if iscluster2(tmp):
                previousCluster2 = True
                cl2tmp = tmp.split()[1]
                if clus2o == "":
                    clus2o = cl2tmp
                    out.append("** " + cl2tmp)
                if cl2tmp <> clus2o:
                    out.append("** " + cl2tmp)
                    clus2o = cl2tmp
            else:
                pass
                # if previousCluster2:
                #     out.append("** " + "nocluster2")
                # previousCluster2 = False
            
            out.append("**"+o) # here org[i] already has one star => ***
            cand = tmp
        else:
            out.append(o)
            if prevclock:
                pass
                # out.append(o)
            else:
                pass
                # out.append('  :CLOCK:') 
                # out.append(o)
            prevclock = True

# out.append('  :END:')

print """#+BEGIN: clocktable :tstart "<2007-01-01 00:00>" :tend "<2011-12-11 23:59>" :step year :maxlevel 3 :narrow 80! :scope file

#+END:
"""

for o in out:
    print o
        
