#!/bin/python

echo ---------------------------
#command 1
UNAME="uname -a"
echo "Gathering sys information using $UNAME command:"
$UNAME

echo ---------------------------
#command 2
DISKSPACE="df -h"
echo "Gathering diskspace information using $DISKSPACE command:"
$DISKSPACE
echo ---------------------------
