#!/bin/bash
# /usr/local/bin/emacs # -fn -ETL-Fixed-Medium-R-Normal--16-160-72-72-C-80-ISO8859-1
bash -i -c `emacsclient -c $* -F "((fullscreen . maximized))"`&
# if (ps -e | grep emacs) # 
# then
#    bash -i -c `emacsclient -c`&
# else
#     `which emacs` --daemon
# fi
