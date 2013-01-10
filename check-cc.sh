#!/bin/sh

is=`ping -c 3 172.25.0.82 | grep -c "64 bytes"`
   # Проверяем прошли ли пинги на Ростелеком default gateway
if (test $is -gt "0") # если пинги проходят
then
    echo "Rostelecom. CC server is down"
    return 1
else
    return 0
    echo "we are in CC"
fi
