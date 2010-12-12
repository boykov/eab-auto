#!/bin/sh

is=`ping -c 3 213.177.96.1 | grep -c "64 bytes"`
   # Проверяем прошли ли пинги
if !(test $is -gt "0") # если пинги не проходят
then
    echo no inet connection
    return 1
else
    return 0
    echo it works
fi
