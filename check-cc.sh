#!/bin/sh

is=`ping -c 3 ???? | grep -c "64 bytes"`
   # Проверяем прошли ли пинги на внутренний сервер CC
if !(test $is -gt "0") # если пинги не проходят
then
    echo "CC server is down"
    return 1
else
    return 0
    echo "we are in CC"
fi
