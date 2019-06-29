#!/bin/sh

while true; do
ssh -R 19999:localhost:22 boykov@fz-keycloak
sleep 2
done
