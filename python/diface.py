#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Единый py-интерфейс ко всему наработанному коду (fortran, mpl).
Все функции (или обертки) тестируются единообразно при помощи unittest.
"""
import os

VERSION = "0.2"

DEFAULT_CONFIG_FILE = os.path.join(os.environ["HOME"], ".diface_startup.py")

try:
    os.stat(DEFAULT_CONFIG_FILE)
except OSError:
    DEFAULT_CONFIG_FILE = None

def usage():
    print """Usage: sage -python diface.py [-s sessionfile] [-c new_startup_file] [-C]
    -C: do not read startup file"""
    sys.exit(0)


#############################
##### Logging subsystem #####
#############################

import logging

# create handler's for logging
log_diface = logging.getLogger("diface")
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler("diface.log")

# set handler's
map(lambda x:
    x.setFormatter(logging.Formatter("%(levelname)s: %(message)s")),
    [console_handler,file_handler])

# привязываем log_diface к handler's
map(lambda x:
    log_diface.addHandler(x),
    [console_handler,file_handler])

if __name__ == "__main__":
    log_diface.setLevel(1)
    # log_diface.error("error")
    # log_diface.warning("warning")
    # log_diface.info("info")
    

##################
##### Module #####
##################

from sage.all import *
from sage.interfaces.maple import maple
from sage.interfaces.maxima import maxima

from numpy import * 

# maple.read("ffunc.mpl")

import unittest

class TestFfunc(unittest.TestCase):
    def setUp(self):
        pass
    def testExample(self):
        self.assertEqual(
            maple.testFnd3a(),
            maple('true'))
    def testFormula(self):
        self.assertEqual(
            maple.testFormula(),
            maple('true'))
    def testMakeDiscret(self):
        NumPoints,Points = MakeDiscret()
        print "Points...",Points

def MakeDiscret(axes=[float(0.75),float(1.),float(0.5)]):
    # Make discretization of ellipsoid with using library point.
    # in:  axes - 3-vector with lengths
    # out: Number of points and array of points.
    import point
    Num = 0
    NumMax = 1000
    PointsTmp = zeros((NumMax,3))
    Num = point.point(Num,PointsTmp,NumMax,axes)
    Points = zeros((Num,3))
    Points[0:Num,0:3] = PointsTmp[0:Num,0:3]
    return Num,Points

if __name__ == '__main__':
    # для корректной работы символических ссылок
    sys.path.append(os.getcwd())
    
    # TODO как пользоваться unittest? 
    # TestFfunc.testExample()
    

    
