#!/usr/bin/env python
import sys,os,shutil

# remote dir on cluster.
# On remote machine by suppression currentdir is ~/
os.chdir("/home/john/pjdra")

latexFile = open('report.tex', 'w')
latexFile.write(r"""
\documentclass[10pt,dvipdfm]{article}
\usepackage[russian]{babel}
\usepackage{breqn}
%% Page layout test

\oddsidemargin -0.5 cm \topmargin -0.5cm \headsep   0cm
\textheight 17cm \textwidth 23cm \footskip  1.5cm

\begin{document}
{
\begin{dmath}
$$
""")

formulaFile = open('formulas.tex','r')
formula = formulaFile.readlines()

# mini-language here! and broken rule SPOT.
for line in formula:
    if line == "\n":
        continue
    elif line == "separator\n":
        latexFile.write("$$\n, ")
#        latexFile.write("\n")
        continue
    elif line == "newline\n":
        latexFile.write("$$\\end{dmath}\n\\begin{dmath}\n$$")
        continue
    else:
        latexFile.write(line)
#    latexFile.write("\n")

    # latexFile.write("$, ")
    # if line == '\n':
    #     continue
 

formulaFile.close()

# remove reportFile formulas.tex after transfer data to report.tex
shutil.copy('formulas.tex','formulas.bak')
os.remove('formulas.tex')

latexFile.write(r"""$$\end{dmath}
}
\end{document}
""")

latexFile.close()

############################################
# Special replace for / to frac
import re
report = open('report.tex', 'r').read()
report = re.sub(r'([0-9]+)/([0-9]+)', r'{\\frac {\1}{\2}}', report) # Special replace for / to frac
report = re.sub(r"""
\\end{dmath}""", r'\\end{dmath}', report)
report = re.sub(r'\\int',r'\\int\\limits', report) # limits integral on top and bottom
# report = re.sub(r'\\mbox {{\\tt ```}}',r'', report)
open('report.tex', 'w').write(report)
############################################




