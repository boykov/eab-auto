#!/bin/sh

GATEWAY=$5

sudo route add 193.142.56.242 gw $GATEWAY tun5
sudo route add 193.142.56.243 gw $GATEWAY tun5
sudo route add 217.23.158.114 gw $GATEWAY tun5

