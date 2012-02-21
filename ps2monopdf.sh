#!/bin/sh

gs -dSAFER -dBATCH -dNOPAUSE -r300x300 -dDITHERPPI=120 -sDEVICE=psmono -sOutputFile=gordeev2001sistemnoe_.ps gordeev2001sistemnoe.ps
ps2pdf gordeev2001sistemnoe_.ps gordeev2001sistemnoe.pdf
