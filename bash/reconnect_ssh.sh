#!/bin/sh

while true; do
    ssh -t -o BatchMode=yes eeepc-rsi "screen -r 3453"
    sleep 2
done
