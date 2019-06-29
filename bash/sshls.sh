#!/bin/sh

while true; do
ssh -R 19999:localhost:22 boykov@fplace-dev-ls
sleep 2
done
