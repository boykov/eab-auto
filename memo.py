#!/usr/bin/python
# -*- coding: utf-8 -*-

import functools
import cPickle

def memoize(fctn):
    memory = {}
    @functools.wraps(fctn)
    def memo(*args,**kwargs):
        haxh = cPickle.dumps((args, sorted(kwargs.iteritems())))

        if haxh not in memory:
            memory[haxh] = fctn(*args,**kwargs)

        return memory

    if memo.__doc__:
        memo.__doc__ = "\n".join([memo.__doc__,"This function is memoized."])
    return memo
        
