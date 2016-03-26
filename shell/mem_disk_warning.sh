#!/bin/bash
#used for memory and disk warning

echo "--get the gree swap--"
swap_free=` free -m | grep Swap | gawk '{print $4}'`
if(( swap_free<15 ))
then
    echo "warning:swap not enough"
fi
echo "remaning swap is:" $swap_free
echo

echo "--get the free memory--"
mem_free=`free -m | grep Mem | gawk '{print $4}'`
if(( mem_free<15 ))
then
    echo "warning:memory not enough"
fi
echo "remaning mem is:" $mem_free "M"
echo

echo "--get the free disk--"
disk_free=`df -h | grep xvda1 | gawk '{print $4}' | cut -f 1 -d "G"`
if(( disk_free<2 ))
then
    echo "warning:disk not enough"
fi
echo "remaning disk is:" $disk_free "G"
echo
