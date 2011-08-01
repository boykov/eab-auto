#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# (eepitch-shell)
# (eepitch-sage-python)
sage -python
execfile("pylib.py")

# from sage.all import *
# from sage.interfaces.maple import maple
"""
import subprocess, os
import unittest
import re
import math

from sage.all import *
from sage.interfaces.maple import maple
from sage.interfaces.maxima import maxima
from sympy import latex
import sympy

if __name__ == '__main__':
    """
    """
    # для корректной работы символических ссылок
    sys.path.append(os.getcwd())
    sys.path.append("/home/john/svn/difwave/upr_upr/")

    maple.read("testF.mpl")
    maple.with_package("ex2")
    f = maple.fbod
    xv = maple.xv
    u = maple.ubod
    subs = maple.subs
    x = maple.x
    y = maple.y
#     n = maple.n
#     a = 1
    evalf = maple.evalf

    out = []
    lst = (u(x)[1],u(x)[2],u(x)[3],f(x)[1],f(x)[2],f(x)[3])
    maple.with_package('CodeGeneration')

    for l in lst:
        mystr = str(maple.execute('Fortran(%s,output=string)' % l))
        out.append(mystr.replace("\\n     #","").replace("sqrt","dsqrt").replace("cexp","cdexp").split("=")[1][:-3])
    print out
    
#     outfile = r"""subroutine my (x, n, a)
#    doubleprecision x(*)
#    doubleprecision n(*)
#    double complex a(*)
#    a(1) =%s
#    a(2) =%s
#    a(3) =%s
#    a(4) =%s
#    a(5) =%s
#    a(6) =%s
# end subroutine my   
# """ % (out[0],out[1],out[2],out[3],out[4],out[5])

#     open("prav.f90", 'w').write(outfile)

    out = []
    funs = ["testlimG","testG","testlimTG","testTG","testlimG","testG","testlimTG","testTG"]
    subst = ["exsub","exsub","exsub","exsub","exsubsr","exsubsr","exsubsr","exsubsr"]
    c = 0
    for f in funs:
        for i in range(1,4,1):
            for j in range(1,4,1):
                mystr = str(maple.execute((u"Fortran(" + f + "(" + subst[c] + ",%s,%s),output = string);" % (j,i)).encode('utf-8')))
                out.append(mystr)
        c = c + 1

            
    print mystr
    
    out = map(lambda x:
              x.replace("\\n     #","").
              replace("cexp","cdexp").
              replace("csqrt(pi)","sqrt(pi)").
              replace("cdexp(-(t(1) ** 2 + t(2) ** 2 + t(3) ** 2) / sigma ** 2)","dexp(-(t(1) ** 2 + t(2) ** 2 + t(3) ** 2) / sigma ** 2)").
              replace(" sqrt"," dsqrt").
              replace("(sqrt","(dsqrt").
              replace(" exp"," dexp").
              replace("(0, -0.1D1 / 0.4D1)","(0, -0.25)").
              replace("(0, 0.1D1 / 0.4D1)","(0, 0.25)").split("=")[1][:-3],out)

    outfile = r"""subroutine jdra (sigma,t,n,upr,pi,ieqj)
    doubleprecision t(*)
    doubleprecision n(*)    
    doubleprecision sigma,pi
    dimension upr(6,6)
    double complex upr

    if (ieqj .eq. 1) then
    # testlimG exsub
    upr(1,1) = %s
    upr(2,1) = %s
    upr(3,1) = %s

    upr(1,2) = %s
    upr(2,2) = %s
    upr(3,2) = %s

    upr(1,3) = %s
    upr(2,3) = %s
    upr(3,3) = %s
    else
    # testG exsub
    upr(1,1) = %s
    upr(2,1) = %s
    upr(3,1) = %s

    upr(1,2) = %s
    upr(2,2) = %s
    upr(3,2) = %s

    upr(1,3) = %s
    upr(2,3) = %s
    upr(3,3) = %s
    end if

    if (ieqj .eq. 1) then
    # testlimTG bad exsub
    upr(4,1) = %s
    upr(5,1) = %s
    upr(6,1) = %s

    upr(4,2) = %s
    upr(5,2) = %s
    upr(6,2) = %s

    upr(4,3) = %s
    upr(5,3) = %s
    upr(6,3) = %s
    else
    # testTG too bad exsub
    upr(4,1) = %s
    upr(5,1) = %s
    upr(6,1) = %s

    upr(4,2) = %s
    upr(5,2) = %s
    upr(6,2) = %s

    upr(4,3) = %s
    upr(5,3) = %s
    upr(6,3) = %s
    end if

    if (ieqj .eq. 1) then
    # testlimG exsubsr
    upr(1,4) = %s
    upr(2,4) = %s
    upr(3,4) = %s

    upr(1,5) = %s
    upr(2,5) = %s
    upr(3,5) = %s

    upr(1,6) = %s
    upr(2,6) = %s
    upr(3,6) = %s
    else
    # testG exsubsr
    upr(1,4) = %s
    upr(2,4) = %s
    upr(3,4) = %s

    upr(1,5) = %s
    upr(2,5) = %s
    upr(3,5) = %s

    upr(1,6) = %s
    upr(2,6) = %s
    upr(3,6) = %s
    end if

    if (ieqj .eq. 1) then
    # testlimTG exsubsr
    upr(4,4) = %s
    upr(5,4) = %s
    upr(6,4) = %s

    upr(4,5) = %s
    upr(5,5) = %s
    upr(6,5) = %s

    upr(4,6) = %s
    upr(5,6) = %s
    upr(6,6) = %s
    else
    # testTG good exsubsr
    upr(4,4) = %s
    upr(5,4) = %s
    upr(6,4) = %s

    upr(4,5) = %s
    upr(5,5) = %s
    upr(6,5) = %s

    upr(4,6) = %s
    upr(5,6) = %s
    upr(6,6) = %s
    end if

end subroutine jdra
""" % tuple(out)
    
    open("jdra.f90", 'w').write(outfile)

    
