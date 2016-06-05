#!/bin/sh
# Add org file changes to the repository
# [[file:/etc/crontab][crontab]]

cd ~/data/src/ASynK/

python asynk.py --op=sync
