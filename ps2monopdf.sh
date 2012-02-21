#!/bin/sh
filename=$*
djvups $filename.djvu $filename.ps 
gs -dSAFER -dBATCH -dNOPAUSE -r300x300 -dDITHERPPI=120 -sDEVICE=psmono -sOutputFile=tmp.ps $filename.ps
ps2pdf tmp.ps $filename.pdf
