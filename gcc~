#!/bin/bash
 
if [ $# -eq 0 ]; then
	/usr/bin/gcc
else
	case "$1" in
		# Patch cadena maple 11:
	        --version)
       		         echo "gcc (GCC) 4.3.1"
       	        	 #echo "gcc version 4.3.2 (Debian 4.3.2-1.1)"
       			 ;;
		# Executar el gcc real:
        	*)
			/usr/bin/gcc $*
        		;;
	esac
fi
 
exit $?