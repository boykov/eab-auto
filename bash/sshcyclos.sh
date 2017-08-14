#!/bin/sh

while true; do
ssh -R 19999:localhost:22 eab@cyclos
sleep 2
done
