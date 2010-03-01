#######
#
# E-scripts on Python.
#
# Note 1: use the eev command (defined in eev.el) and the
# ee alias (in my .zshrc) to execute parts of this file.
# Executing this file as a whole makes no sense.
#
# Note 2: be VERY careful and make sure you understand what
# you're doing.
#
# Note 3: If you use a shell other than zsh things like |&
# and the for loops may not work.
#
# Note 4: I always run as root.
#
# Note 5: some parts are too old and don't work anymore. Some
# never worked.
#
# Note 6: the definitions for the find-xxxfile commands are on my
# .emacs.
#
# Note 7: if you see a strange command check my .zshrc -- it may
# be defined there as a function or an alias.
#
# Note 8: the sections without dates are always older than the
# sections with dates.
#
# This file is at <http://angg.twu.net/e/python.e>
#           or at <http://angg.twu.net/e/python.e.html>.
#        See also <http://angg.twu.net/emacs.html>,
#                 <http://angg.twu.net/.emacs[.html]>,
#                 <http://angg.twu.net/.zshrc[.html]>,
#                 <http://angg.twu.net/escripts.html>,
#             and <http://angg.twu.net/>.
#
#######



# «.python-base»	(to "python-base")
# «.python-examples»	(to "python-examples")
# «.pyex»		(to "pyex")
# «.pydb»		(to "pydb")
# «.pdb»		(to "pdb")
# «.python-tk»		(to "python-tk")
# «.ee-for-python»	(to "ee-for-python")
# «.eechannel-python»	(to "eechannel-python")
# «.python-docutils»	(to "python-docutils")
# «.rst»		(to "rst")
# «.diveintopython»	(to "diveintopython")
# «.closures»		(to "closures")
# «.python-apt»		(to "python-apt")
# «.python-apt-deb-src»	(to "python-apt-deb-src")
# «.python-opengl»	(to "python-opengl")


# «links»
# (find-angg ".emacs" "python")
# (find-es "locz" "python")




#####
#
# Installing and finding the basic docs
# 2000may09
#
#####

Pgrepp m/python/i |& tee ~/o
# (find-fline "~/o")

apti python-base python-doc python-examples python-elisp python-dev \
  pydb python-pygresql

# (find-vldifile "python-base.list")
# (find-vldifile "python-dev.list")
# (find-vldifile "python-doc.list")
# (find-vldifile "python-elisp.list")
# (find-vldifile "python-examples.list")
# (find-fline "/usr/doc/python-base/")
# (find-fline "/usr/doc/python-dev/")
# (find-fline "/usr/doc/python-doc/")
# (find-fline "/usr/doc/python-elisp/")
# (find-fline "/usr/doc/python-examples/")

# (find-node "(python-tut)Top")
# (find-node "(python-tut)Numbers")
# (find-node "(python-lib)Top")
# (find-node "(python-ref)Top")


# (find-pytutnode "Top")

# (find-pytutnode "Defining Clean-up Actions")
# (find-pytutnode "A Word About Terminology" "if a function modifies")
# (find-pytutnode "Python Scopes and Name Spaces" "three nested")

# (find-pytutnode "Method Objects")
# (find-pytutnode "Defining Functions")

# (find-angg "EXPECT/eeg")

cat > $EEG <<'---'
class foo:
  x = 2
  def f(x):
    return x*20

foo
a = foo()
a
a.x
a.f
a.f(a.x)
---
eeg python









#####
#
# python-base
# 2000may25
#
#####

# «python-base»  (to ".python-base")
# (find-status "python-base")
# (find-vldifile "python-base.list")

# (find-eeman "1 python")
# (find-fline "/usr/doc/python-base/")
# (find-fline "/usr/doc/python/")
# (find-fline "/usr/doc/python/NEWS.gz")
# (find-fline "/usr/doc/python/HISTORY.gz")
# (find-fline "/usr/doc/python/BLURB")
# (find-fline "/usr/doc/python/sample.postinst")
# (find-fline "/usr/doc/python/sample.prerm")
# (find-fline "/usr/doc/python/README.maintainers")
# (find-fline "/usr/doc/python/README.dbm")
# (find-fline "/usr/doc/python/TODO.Debian.gz")
# (find-fline "/usr/doc/python/copyright")
# (find-fline "/usr/doc/python/README.gz")
# (find-fline "/usr/doc/python/ACKS.gz")
# (find-fline "/usr/doc/python/README.Debian.gz")
laf /usr/bin/python
laf /usr/bin/python1.5

# (find-pylibfile "lib-dynload/")
laf /usr/lib/libpython1.5.so.0.0
# (find-fline "/usr/lib/menu/python-base")
# (find-fline "/usr/lib/python1.4/")




#####
#
# python and postgresql
# 2000may12
#
#####

# (find-status "python-pygresql")
# (find-vldifile "python-pygresql.list")

# (find-fline "/usr/doc/python-pygresql/")
# (find-fline "/usr/doc/python-pygresql/README.gz" "connect -")
# (find-fline "/usr/doc/python-pygresql/tutorial/")
# (find-pylibfile "site-packages/pg.py")
# (find-pylibfile "site-packages/pgsqldb.py")






# (find-vldifile "postgresql.list")
# (find-fline "/usr/doc/postgresql/")
# (find-vldifile "postgresql-client.list")
# (find-fline "/usr/doc/postgresql-client/")

# (find-fline "/var/lib/postgres/")




(w3-open-local "/snarf/http/www.idi.ntnu.no/~mlh/python/instant.html")
(find-fline "$S/http/www.python.org/doc/essays/metaclasses/meta-vladimir.txt")
(find-file "/snarf/http/www.idi.ntnu.no/~mlh/python/quicksort.py")
(find-fline "$S/http/www.strout.net/python/pattern.py")
(find-fline "$S/http/www.strout.net/python/tabfix.py")

# (find-w3 "/usr/doc/python/examples/Demo/metaclasses/index.html")

# (find-fline "/usr/lib/python1.5/cgi.py")

# (find-node "(python-ref)import statement")
# (find-pyrefnode "import statement")
# (find-pyrefnode "Module Index")
# (find-pyrefnode "standard type hierarchy")
# (find-pyrefnode "Objects")
# (find-pytutnode "A First Look at Classes")
# (find-pytutnode "Python Scopes and Name Spaces")
# (find-pyrefnode "Keywords")
# (find-pyrefnode "standard type hierarchy" "`Classes'")

#
cat > $EEG <<'---'
class A:
    attr1 = "Hello"                  # an attribute of A
    def method1(self, *args): pass   # method1 of A
    def method2(self, *args): pass   # method2 of A

A                                # What is A?
a = A()                          # 'a' is the 1st instance of A 
a                                # What is 'a'? 
b = A()                          # 'b' is another instance of A
b                                # What is 'b'?
a == b                           # Is 'a' the same object as 'b'?
a.__class__                      # What is the class of 'a'?
b.__class__                      # What is the class of 'b'?
a.__class__ == b.__class__       # Is it really the same class A?
class B(A):                          # B inherits A's properties
    attr2 = "World"                  # additional attr2
    def method2(self, arg1): pass    # method2 is redefined
    def method3(self, *args): pass   # additional method3

B                                 # What is B?
B == A                            # Is B the same class as A?
A.__bases__                       # Does A have any superclasses?
B.__bases__                       # Does B have any superclasses?
B.__bases__[0] == A               # Is it really the class A?
---
eeg python
#


#
cat > $EEG <<'---'
import sys
sys.__dict__
type(sys.__dict__)
type(sys)
type(type)
`sys.__dict__`
type(`sys.__dict__`)
s = lambda n: n + 1
s(2)
s
type(s)
`s`
---
eeg python
#


# (find-pyrefnode "Basic customization")
# (find-pyrefnode "Code blocks")
# (find-pyrefnode "Dictionary displays")
# (find-pyrefnode "String conversions")
# (find-pyrefnode "Boolean operations" "lambda x")
# (find-pyrefnode "Summary")
# (find-pyrefnode "Assignment statements" "target list")
# (find-pyrefnode "exec statement")
# (find-pyrefnode "Function definitions")
# (find-pyrefnode "Class definitions")

# (find-pylibnode "More String Operations")



#
cat > $EEG <<'---'
vars()
import sys
vars()
"foo %d %d" % (2, 3)
"foo %s %d" % (2, 3)
"foo %s %d" % ("2", "3")
"foo %(a)d %(b)d" % {"b":2, "a":3}
---
eeg python
#












#####
#
# python-examples
# 2000may25
#
#####

# «python-examples»  (to ".python-examples")
# «pyex»  (to ".pyex")
# (find-status "python-examples")
# (find-vldifile "python-examples.list")

# (find-pylibnode "regex")
# (find-pylibnode "re")
# (find-pylibnode "Matching vs. Searching")

# (find-pyrefnode "Miscellaneous Index")

#
cat > $EEG <<'---'
import re
d = re.__dict__
d.keys
d.keys()
d.__methods__
re.__name__
re.__file__
re.__builtins__.keys()
[].__methods__
---
eeg python

#
cat > $EEG <<'---'
[].__methods__
import re,string
string.join(["a", "b"])
string.join(["a", "b", "c"], "--")
---
eeg python

#
cat > $EEG <<'---'
[].__methods__
import re, string
string.join(["a", "b"])
string.join(["a", "b", "c"], "--")
string.__dict__.keys()
dir(string)
join
string.__dict__.keys().sort.__doc__
---
eeg python

#


#
cat > $EEG <<'---'
a = [2, 4, 1, 3]
a.sort()
a
d = {1:2, 5:6, 3:4}
d
---
eeg python
#

a.join



# (find-pytutnode "for Statements")
# (find-pytutnode "dir Function")
# (find-pylibnode "Mutable Sequence Types")



cd /usr/share/info/
zcat python-ref.info{,-?}.gz	 > /tmp/python-ref
zcat python-lib.info{,-?,-??}.gz > /tmp/python-lib
zcat python-tut.info{,-?}.gz	 > /tmp/python-tut


# (find-status "htmlgen")
# (find-vldifile "htmlgen.list")
# (find-fline "/usr/doc/htmlgen/")

# (find-status "idle")
# (find-vldifile "idle.list")
# (find-fline "/usr/doc/idle/")



# (find-status "python-bobo")
# (find-vldifile "python-bobo.list")
# (find-fline "/usr/doc/python-bobo/")

# (find-status "python-bobodtml")
# (find-vldifile "python-bobodtml.list")
# (find-fline "/usr/doc/python-bobodtml/")

python-bobo
apti python-bobodtml





#####
#
# dpkg-python
# 2000aug02
#
#####

pdsc $SDEBIAN/dists/woody/main/source/devel/dpkg-scriptlib_0.1-3.1.dsc
cd /usr/src/dpkg-scriptlib-0.1/

# (find-status "dpkg-python")
# (find-vldifile "dpkg-python.list")
# (find-fline "/usr/doc/dpkg-python/")

# (code-c-d "dsl" "/usr/src/dpkg-scriptlib-0.1/")
# (find-dslfile "")
# (find-dslfile "perl5/Dpkg/Archive/")
# (find-dslfile "perl5/Dpkg/Package/")
# (find-dslfile "python/dpkg/")

# (find-fline "/usr/lib/site-python/dpkg/")

#
cat > $EEG <<'---'
import sys; sys.path.append("/usr/lib/site-python/dpkg")
from dpkg_packages import *
parse_package_name("kernel-image-2.2.15_angg.00jun13.deb")
---
eeg python
#

echo 'import foo' \
  | strace-to ~/s python

# (find-pytutnode "Invoking the Interpreter")

python -c '
import sys; sys.path.append("/usr/lib/site-python/dpkg")
from dpkg_packages import *
print parse_package_name("kernel-image-2.2.15_angg.00jun13.deb")
'




#####
#
# classes
# 2000aug02
#
#####

# (find-pytutnode "Class Definition Syntax")
# (find-pytutnode "Class Objects")
# (find-pytutnode "Instance Objects")
# (find-pyrefnode "del statement")
# (find-pytutnode "Method Objects")
# (find-pytutnode "Random Remarks")
# (find-pytutnode "Inheritance")
# (find-pytutnode "Multiple Inheritance")

# (find-pytutnode "Dictionaries")
# (find-pyrefnode "Special method names")
# (find-pyrefnode "Emulating sequence and mapping types")
# (find-pyrefnode "Code blocks" "\"namespace\"")

# (find-shttpw3 "www.idi.ntnu.no/~mlh/python/instant.html" "__init__")

#
cat > $EEG <<'---'
import sys
class DictFirst:
  # dict = {}		# Wrong: makes every instance share the same dict!
  def __init__(self):	# This is the corrected version.
    self.dict = {}
  def feed(self, k, v):
    # print self; print self.dict; print k; print v
    if self.dict.has_key(k):
      print "Repeated key %s, old val %s" % (k, self.dict[k])
    else:
      self.dict[k] = v

d = DictFirst()
d.feed(2,3)
d.dict
d.feed(4,5)
d.dict
d.feed(2,10)
d.dict

d2 = DictFirst()
d2.feed("a", "b")
d2.dict
d.dict		# d and d2 are sharing the same dict!

d.a = 20	# However new "fields" like a here are not shared:
d.a		# this is ok
d2.a		# but this gives an error.
d
d2
d.__dict__
d2.__dict__
d.__class__
d2.__class__

pr1 = lambda x: print "pr1 %s" % x	# error: print is a statement (?)
d.f = pr1
d.pr1(12)
d2.pr1(12)
---
eeg python

#





#####
#
# regexps in Python (module re)
# 2000aug06
#
#####

# (find-pylibnode "re")
# (find-pylibnode "Contents of Module re")
# (find-pylibnode "Regular Expression Objects")
# (find-pylibnode "Match Objects")
# (find-pylibnode "Regular Expression Syntax" "?P<id>")
# (find-pyrefnode "String literals")

# (find-angg ".zshrc" "debbasename")

# (find-pyrefnode "Exceptions")
# (find-pyrefnode "try statement")

# (find-fline "~/PYTHON/debs.py")

#

lynx http://www.python.org/doc/howto/

#
cd ~/PYTHON/
echo 'from debs import *' > $EEG
eeg python
#





#####
#
# python source
# 2000aug08
#
#####

pdsc $SDEBIAN/dists/potato/main/source/interpreters/python_1.5.2-10.dsc
cd /usr/src/python-1.5.2/

# find * | grep '\.[ch]$'
find Include Modules Objects Parser Python | grep '\.[ch]$' > .files.ch
etags $(<.files.ch)
glimpseindex -H . -y $(<.files.ch)

# (code-c-d "pysrc" "/usr/src/python-1.5.2/")
# (find-pysrcfile "")
# (find-pysrcfile "Python/")
# (find-pysrcfile "Python/bltinmodule.c")

# (find-pysrctag "execfile_doc")
# (find-pysrctag "eval_doc")
# (find-pysrctag "intern_doc")




#####
#
# compiling
# 2000aug21
#
#####

# «compiling»
# (find-pylibfile "compileall.py")
# (find-pylibfile "py_compile.py")
# (find-vldifile "" " python")




#####
#
# running interactively
# 2004aug07
#
#####

#
# (find-pytutnode "Interactive Startup File")
# (find-pyrefnode "global statement" "execfile()")

cd /usr/share/doc/python/examples/Demo/tkinter/guido/
cat > $EEG <<'---'
import os
execfile("hanoi.py")
---
eeg python

#
cat > /tmp/test.py <<'---'
print "Hello from tmp!\n"
---
python /tmp/test.py

cd /tmp
cat > $EEG <<'---'
import test
import test
---
eeg python

#





#####
#
# pdb
# 2004aug06
#
#####

# «pdb»  (to ".pdb")
# http://page.sourceforge.net/tricks.html
# (find-efile "progmodes/python.el" "M-x pdb")

#
# (eev-bounded)
# This block works - both "python /tmp/fib.py" and ".../pdb.py /tmp/fib.py".

cat > /tmp/fib.py <<'%%%'
def fib(n):    # write Fibonacci series up to n
    "Print a Fibonacci series up to n"
    a, b = 0, 1
    while b < n:
        print b,
        a, b = b, a+b

# Now call the function we just defined:
fib(2000)
%%%

python /tmp/fib.py
/usr/lib/python2.1/pdb.py /tmp/fib.py

#
# But the pdb invocation does NOT work:
# (require 'gud)
# (setq gud-pdb-command-name "/usr/lib/python2.1/pdb.py")
# (pdb "/usr/lib/python2.1/pdb.py /tmp/fib.py")

#
# «pydb»  (to ".pydb")
#
# (find-status "pydb")
# (find-vldifile "pydb.list")
# (find-fline "/usr/doc/pydb/")

/usr/bin/pydb /tmp/fib.py

#
# Running pdb with pydb still doesn't show the source lines, but at
# least it shows the prompt and accepts the "h" command".

# (require 'gud)
# (setq gud-pdb-command-name "/usr/bin/pydb")
# (pdb "/usr/bin/pydb /tmp/fib.py")






#####
#
# python-tk
# 2004aug07
#
#####

# «python-tk»  (to ".python-tk")
# (find-status "python2.1-tk")
# (find-vldifile "python2.1-tk.list")
# (find-fline "/usr/doc/python2.1-tk/")

#
# (find-pyexdfile "tkinter/guido/hanoi.py")
cd /usr/share/doc/python2.1/examples/Demo/tkinter/guido/
python hanoi.py

#




# (find-status "python")
# (find-vldifile "python.list")
# (find-fline "/usr/doc/python/")
# (find-status "python2.1")
# (find-vldifile "python2.1.list")
# (find-fline "/usr/doc/python2.1/")

# (find-fline "/usr/lib/python2.1/")
# (find-fline "/usr/lib/python2.1/pdb.py")
# (find-fline "/usr/lib/python2.1/pdb.doc")


apti python2.1-doc
# (find-status "python2.1-doc")
# (find-vldifile "python2.1-doc.list")
# (find-fline "/usr/doc/python2.1-doc/")

# (find-progoutput "dpkg --get-selections")

# (find-status "python2.1")
# (find-vldifile "python2.1.list")
# (find-fline "/usr/doc/python2.1/")

(find-pytutnode "")
(find-pylibnode "")
(find-pyrefnode "")

(find-pyapinode "")
(find-pydistnode "")
(find-pyextnode "")

(find-pytutnode "break and continue Statements")

# (find-status "python2.1-examples")
# (find-vldifile "python2.1-examples.list")
# (find-fline "/usr/doc/python2.1-examples/")
# (find-pyexdfile "")
# (find-pyexdfile "scripts/")

# (find-status "python2.1-elisp")
# (find-vldifile "python2.1-elisp.list")
# (find-fline "/usr/doc/python2.1-elisp/")


#
python =(<<'%%%'
print 2+3
%%%)

#




#
# By kov

function pyrename () { python =(<<'%%%'
import os
l = os.listdir ('.')
for arquivo in l:
   os.rename (arquivo, arquivo.replace (' ', '_'))
%%%) $*
}

rm -Rv /tmp/pyr
mkdir  /tmp/pyr
cd     /tmp/pyr
echo 1 > 'um um um'
echo 2 > 'dois dois dois'
pyrename 'um um um' 'dois dois dois'

#




#####
#
# an ee() function for python
# 2004nov03
#
#####

# «ee-for-python»  (to ".ee-for-python")
#
# The wrong way:
# (find-pyrefnode "exec statement")

python <(<<'%%%'
def ee():
  exec "print 999"
  exec "print 777\ndef foo():\n  print 888\nfoo()"
ee()
print "We lost the definition of foo:"
foo()
%%%)

#
# The right way: execfile("fname", globals())
# (find-pyrefnode "import statement")
# (find-pylibnode "os")
# (find-pylibnode "Process Parameters" "`getenv(varname[, value])'")
# (find-pylibnode "Built-in Functions" "`execfile(filename")
# (find-pyrefnode "exec statement" "`globals()'")

cat > $EEVTMPDIR/ee.py <<'%%%'
print 11
def foo():
  print 22
print 33
%%%

python =(<<'%%%'
import os
def ee():
  execfile(os.getenv("EEVTMPDIR")+"/ee.py", globals())
print 0
ee()
foo()
%%%)

#



#####
#
# dumping the arguments
# 2004nov04
#
#####

# (find-pylibnode "File Descriptor Operations")


#
rm -v /tmp/o

python =(<<'%%%'
import os
def foo(*args):
  fd = open("/tmp/o", "w")
  fd.write(str(args)+"\n")
  fd.close
foo((1, 2), "3")
%%%)

cat /tmp/o

#



#####
#
# talking to python through eechannel
# 2005jan01
#
#####

# «eechannel-python»  (to ".eechannel-python")
# http://people.debian.org/~kov/stuff/edrx.tar.gz
# (find-pylibnode "signal")
# (find-pyrefnode "Comments")
# (find-pyrefnode "String literals")
# (my-modes :scroll-bar    :pager    :erc-track    :fringe    :width80)
# (my-modes :no-scroll-bar :no-pager :no-erc-track :no-fringe :width80)

 (eebg-channel-xterm "pysh")
 (eechannel "pysh")

cd /tmp/
python

import signal, time, os

channel = 'python'
pidfile = os.getenv('EEVTMPDIR') + '/eeg.' + channel + '.pid'
strfile = os.getenv('EEVTMPDIR') + '/eeg.' + channel + '.str'
fhandle = open (pidfile, 'w')
fhandle.write (str(os.getpid()) + '\n')
fhandle.close ()

def signal_handler (num, frame):
  execfile(strfile, globals())

signal.signal (signal.SIGUSR1, signal_handler)

a = 0
while (1):
    print a
    time.sleep (1)
    a = a + 1

 (eechannel "python")
print '(hi)'
print '(hi again)'

 (find-sh0 "~/bin/Xscreenshot")
 ;; http://angg.twu.net/tmp/shot-pychannel0.png


 

# (write-region "print '(oi)'\n" nil "/tmp/coisa.py")
# (find-zsh0 "kill -SIGUSR1 $(cat /tmp/eeg.python.pid)")

(find-pytutnode "")
(find-pylibnode "")
(find-pyrefnode "")

(find-pyapinode  "")
(find-pydistnode "")
(find-pyextnode  "")



    import coisa
    del coisa






#####
#
# python-docutils / rst
# 2007mar25
#
#####

# «python-docutils»  (to ".python-docutils")
# «rst»  (to ".rst")
# http://docutils.sourceforge.net/rst.html
# http://docutils.sourceforge.net/docs/user/rst/quickstart.txt
# (find-status   "python-docutils")
# (find-vldifile "python-docutils.list")
# (find-udfile   "python-docutils/")

# (code-c-d "pydocudoc" "/usr/share/doc/python-docutils/")
# (find-pydocudocfile "ref/rst/introduction.txt.gz")
# (find-pydocudocfile "user/rst/quickstart.txt.gz")
# (find-pydocudocfile "user/rst/")
# (find-pydocudocfile "")

# (find-fline "/tmp/rst/")
#
rm -Rv /tmp/rst/
mkdir  /tmp/rst/
cd /usr/share/doc/python-docutils/user/rst/
cp -v * /tmp/rst/
cd /tmp/rst/
gunzip -v *.gz
for i in *.txt; do
  echo $i
  rst2html $i > $(basename $i .txt).html
done   |& tee o

#

# Source:
# (code-c-d "pydocusp"  "/usr/lib/site-python/docutils/")
# (find-pydocuspfile "")







#####
#
# dive into python
# 2007mar25
#
#####

# «diveintopython»  (to ".diveintopython")
# (find-status   "diveintopython")
# (find-vldifile "diveintopython.list")
# (find-udfile   "diveintopython/")
# (code-c-d "pydip" "/usr/share/doc/diveintopython/")
# (find-pydipfile "")
# (find-pydipw3m "html/toc/index.html")

# Very bad book, incredibly bad examples.




#####
#
# closures
# 2008jun28
#
#####

# «closures»  (to ".closures")
 (eepitch-python)
 (eepitch-kill)
 (eepitch-python)

def adder(x):
    def foo(y): 
            return y + x
    return foo

plus2 = adder(2)
plus2(3)

plus3 = adder(3)
plus3(5)      




#####
#
# python-apt (from the debian sources)
# 2009jul27
#
#####

# «python-apt-deb-src»  (to ".python-apt-deb-src")
# http://ftp.de.debian.org/debian/pool/main/p/python-apt/
# http://ftp.de.debian.org/debian/pool/main/p/python-apt/python-apt_0.7.7.1+nmu1.dsc
# http://ftp.de.debian.org/debian/pool/main/p/python-apt/python-apt_0.7.7.1+nmu1.tar.gz
#
rm -Rv ~/usrc/python-apt/
mkdir  ~/usrc/python-apt/
cd $S/http/ftp.de.debian.org/debian/pool/main/p/python-apt/
cp -v python-apt_0.7.7.1+nmu1* ~/usrc/python-apt/
cd     ~/usrc/python-apt/
dpkg-source -sn -x python-apt_0.7.7.1+nmu1.dsc
cd     ~/usrc/python-apt/python-apt-0.7.7.1+nmu1/
dpkg-buildpackage -us -uc -b -rfakeroot     |& tee odb

#
# (find-fline "~/usrc/python-apt/")
 (eepitch-shell)
cd ~/usrc/python-apt/
sudo dpkg -i *.deb

#
# (code-c-d "pythonapt" "~/usrc/python-apt/python-apt-0.7.7.1+nmu1/")
# (find-pythonaptfile "")
# (find-pythonaptfile "doc/examples/")




#####
#
# python-apt
# 2009jul27
#
#####

# «python-apt»  (to ".python-apt")
# (find-es "apt" "libapt")
# (find-status   "python-apt")
# (find-vldifile "python-apt.list")
# (find-udfile   "python-apt/")

# (code-c-d "pythonapt"   "/usr/lib/python2.5/site-packages/apt/")
# (code-c-d "pythonaptex" "/usr/share/doc/python-apt/examples/")
# (find-pythonaptfile "")
# (find-pythonaptexfile "")
# (find-pythonaptexfile "build-deps.py")

 (eepitch-python)
 (eepitch-kill)
 (eepitch-python)
import apt_pkg
import sys
import sets

def get_source_pkg(pkg, records, depcache):
        """ get the source package name of a given package """
        version = depcache.GetCandidateVer(pkg)
        if not version:
                return None
        file, index = version.FileList.pop(0)
        records.Lookup((file, index))
        if records.SourcePkg != "":
                srcpkg = records.SourcePkg
        else:
                srcpkg = pkg.Name
        return srcpkg

# main
apt_pkg.init()
cache      = apt_pkg.GetCache()
depcache   = apt_pkg.GetDepCache(cache)
depcache.Init()
records    = apt_pkg.GetPkgRecords(cache)
srcrecords = apt_pkg.GetPkgSrcRecords()

base              = cache["emacs22-el"]                 # For example
all_build_depends = sets.Set()

# get the build depdends for the package itself
srcpkg_name = get_source_pkg(base, records, depcache)
print "srcpkg_name: %s " % srcpkg_name
if not srcpkg_name:
        print "Can't find source package for '%s'" % pkg.Name

srcrec = srcrecords.Lookup(srcpkg_name)
if srcrec:
        print "Files:"
        print srcrecords.Files
        bd = srcrecords.BuildDepends
        print "build-depends of the package: %s " % bd
        for b in bd:
                all_build_depends.add(b[0])

# calculate the build depends for all dependencies
depends = depcache.GetCandidateVer(base).DependsList
for dep in depends["Depends"]: # FIXME: do we need to consider PreDepends?
        pkg = dep[0].TargetPkg
        srcpkg_name = get_source_pkg(pkg, records, depcache)
        if not srcpkg_name:
                print "Can't find source package for '%s'" % pkg.Name
                continue
        srcrec = srcrecords.Lookup(srcpkg_name)
        if srcrec:
                #print srcrecords.Package
                #print srcrecords.Binaries
                bd = srcrecords.BuildDepends
                #print "%s: %s " % (srcpkg_name, bd)
                for b in bd:
                        all_build_depends.add(b[0])

print "\n".join(all_build_depends)





#####
#
# python-opengl
# 2009jul27
#
#####

# «python-opengl»  (to ".python-opengl")
apti python-opengl python-opengl-doc

# (find-status   "python-opengl")
# (find-vldifile "python-opengl.list")
# (find-udfile   "python-opengl/")
# (find-status   "python-opengl-doc")
# (find-vldifile "python-opengl-doc.list")
# (find-udfile   "python-opengl-doc/")

# (find-fline "/usr/share/doc/python-opengl-doc/documentation/pydoc/")

# http://code.activestate.com/recipes/325391/

 (eepitch-python)
 (eepitch-kill)
 (eepitch-python)
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys

name = 'ball_glut'

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(400,400)
    glutCreateWindow(name)
    #
    glClearColor(0.,0.,0.,1.)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_CULL_FACE)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    lightZeroPosition = [10.,4.,10.,1.]
    lightZeroColor = [0.8,1.0,0.8,1.0] #green tinged
    glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
    glEnable(GL_LIGHT0)
    glutDisplayFunc(display)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(40.,1.,1.,40.)
    glMatrixMode(GL_MODELVIEW)
    gluLookAt(0,0,10,
              0,0,0,
              0,1,0)
    glPushMatrix()
    glutMainLoop()
    return

def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    color = [1.0,0.,0.,1.]
    glMaterialfv(GL_FRONT,GL_DIFFUSE,color)
    glutSolidSphere(2,20,20)
    glPopMatrix()
    glutSwapBuffers()
    return

if __name__ == '__main__': main()










http://en.wikipedia.org/wiki/PyPy


# http://www.dabeaz.com/ply/
# (find-status   "python-ply")
# (find-vldifile "python-ply.list")
# (find-udfile   "python-ply/")


Cairo:
# http://arstechnica.com/articles/columns/linux/linux-20050822.ars
# (find-zsh "availabledebs | sort | grep cairo")

apti python-cairo-dev







#  Local Variables:
#  coding:               raw-text-unix
#  ee-delimiter-hash:    "\n#\n"
#  ee-delimiter-percent: "\n%\n"
#  ee-anchor-format:     "«%s»"
#  End:

