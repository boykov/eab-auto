#!/usr/bin/env python
import sys,os,shutil


maplefile = open('wrap.mpl', 'w')
maplefile.write(r"""
restart:
read "test.mpl":
""")

maplefile.close()


# test.mpl creates report.tex
os.system("maple wrap.mpl > wraprep.tex")



