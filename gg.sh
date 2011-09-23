#!/bin/sh
exec firefox "http://www.google.ru/search?hl=ru&q=$*"
echo "asd" >> /home/eab/tmp.log
return 0