#!/bin/sh
# cp ~/git/org/norang.html ~/projects/web/narod/norang.html
# cp ~/git/org/negic.jpg ~/projects/web/narod/negic.jpg
# cd ~/projects/web/narod/
# iconv -f utf-8 -t windows-1251 norang.html > index.html
lftp -p 21 ftp.narod.ru  << cmd
mirror -e -R -c -v --log=/home/john/projects/web/lftp.log ~/projects/web/eligea /
quit
