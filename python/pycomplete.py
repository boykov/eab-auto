import sys
import inspect
from StringIO import StringIO
import os.path

try:
    x = set
except NameError:
    from sets import Set as set
else:
    del x

from Pymacs import lisp

sys.path.append('.')

def pycomplete(s, imports=None, debug=False):
    """Display completion in Emacs window"""
    completions = _get_all_completions(s, imports)
    dots = s.split(".")
    result = os.path.commonprefix([k[len(dots[-1]):] for k in completions])

    if result == "":
        if completions:
            if debug:
                width = 80
            else:
                width = lisp.window_width() - 2

            column = width / 20
            white = " " * 20
            msg = ""

            counter = 0
            for completion in completions :
                if len(completion) < 20 :
                    msg += completion + white[len(completion):]
                    counter += 1
                else :
                    msg += completion + white[len(completion) - 20:]
                    counter += 2

                if counter >= column:
                    counter = 0
                    msg += '\n'

        else:
            msg = "no completions!"
        if debug:
            print msg
        else:
            lisp.message(msg)
    return result      

def pyhelp(s, imports=None):
    """Return object description"""
    _import_modules(imports, globals(), None)
    return _getdoc(s)

def pysignature(s):
    """Return info about function parameters"""
    f = None
    try:
        f = eval(s)
    except Exception, ex:
        return "%s" % ex

    if inspect.ismethod(f):
        f = f.im_func
    if not inspect.isfunction(f):
        return ''
    (args, varargs, varkw, defaults) = inspect.getargspec(f)
    return('%s: %s'
           % (f.__name__, inspect.formatargspec(args,varargs,varkw,defaults)))

def _getdoc(s):
    """Return string printed by `help` function"""
    obj = None
    try:
        obj = eval(s)
    except Exception, ex:
        return "%s" % ex
    out = StringIO()
    old = sys.stdout
    sys.stdout = out
    help(obj)
    sys.stdout = old
    return out.getvalue()

def _import_modules(imports, dglobals, dlocals):
    """If given, execute import statements"""

    if imports is not None:
        for stmt in imports:
            try:
                exec stmt in dglobals, dlocals
            except TypeError:
                raise TypeError, 'invalid type: %s' % stmt
            except:
                continue

def _get_all_completions(s, imports=None):
    """Return contextual completion of s (string of >= zero chars)"""

    dlocals = {}
    _import_modules(imports, globals(), dlocals)
    dots = s.split(".")
    if not s or len(dots) == 1:
        keys = set()
        keys.update(dlocals.keys())
        keys.update(globals().keys())
        import __builtin__
        keys.update(dir(__builtin__))
        keys = list(keys)
        keys.sort()
        if s:
            return [k for k in keys if k.startswith(s)]
        else:
            return keys

    sym = None
    for i in range(1, len(dots)):
        s = ".".join(dots[:i])  
        try:
            sym = eval(s, globals(), dlocals)
        except NameError:
            try:
                sym = __import__(s, globals(), dlocals, [])
            except ImportError:
                return []
    if sym is not None:  
        s = dots[-1]    
        return [k for k in dir(sym) if k.startswith(s)]

def _test():
    print ' ->', pycomplete('', debug=True)
    print 'sys.get ->', pycomplete('sys.get', debug=True)
    print 'settr ->', pycomplete('settr', debug=True)
    print 'settr (plat in context) ->',
    print pycomplete('settr', imports=['from sys import settrace'], debug=True)
    print 'foo. ->', pycomplete('foo.', debug=True)
    print 'Enc (email * imported) ->',
    print pycomplete('Enc', imports=['from email import *'], debug=True)
    print 'E (email * imported) ->',
    print pycomplete('E', imports=['from email import *'], debug=True)
    print 'Enc ->', pycomplete('Enc', debug=True)
    print 'E ->', pycomplete('E', debug=True)

if __name__ == "__main__":
    _test()
