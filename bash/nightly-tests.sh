#!/bin/sh
# Add org file changes to the repository
# [[file:/etc/crontab][crontab]]

export PATH=$PATH:/usr/local/bin/ # path for maxima

cd ~/git/difwave/gsie && make -f Makefile libjacobian.so

cd ~/git/difwave/gsie/dotgsie/

export LD_LIBRARY_PATH=/home/eab/git/difwave/gsie/ && python -m unittest testcover
