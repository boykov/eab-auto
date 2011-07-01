#!/bin/bash
# /usr/local/bin/emacs # -fn -ETL-Fixed-Medium-R-Normal--16-160-72-72-C-80-ISO8859-1
if !(ps -e | grep emacs) # 
then
    `which emacs` --daemon
else
    bash -i -c `emacsclient -c`&
fi
