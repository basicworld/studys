#!/usr/bin/python
#coding:utf-8
#wrap up rsync to synchronize two directories
from subprocess import call
import sys
import time

source="/tmp/sync_dir_a"
target="/tmp/sync_dir_b"
rsync="rsync"
arguments="-av"

cmd="%s %s %s %s"%(rsync,arguments,source,target)

def sync():
    while True:
        ret=call(cmd,shell=True)
        if ret!=0:
            print 'resubmitting rsync'
            time.sleep(30)
        else:
            print 'rsync successful'
            sys.exit(1)

if __name__=='__main__':
    sync()
