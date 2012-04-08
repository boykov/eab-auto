#!/usr/bin/python
# -*- coding: utf-8 -*-

import functools
import cPickle
from ellipsoid import *
import shelve
from numpy import *

def memoize(fctn):
    memory = shelve.open("memo.dat")
    @functools.wraps(fctn)
    def memo(*args,**kwargs):
        haxh = cPickle.dumps((args, sorted(kwargs.iteritems())))

        if haxh not in memory:
            memory[haxh] = fctn(*args,**kwargs)

        return memory

    if memo.__doc__:
        memo.__doc__ = "\n".join([memo.__doc__,"This function is memoized."])
    return memo

@memoize
def wrapellipsoid(axes,points):
    return ellipsoid(axes,points)

if __name__ == "__main__":
    e = wrapellipsoid(array([0.75,1,0.5]),200)
