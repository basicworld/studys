#!/usr/bin/python
#coding:utf-8

import sys
import os
path=os.getcwd()
sys.path.append(path)

from checksum import create_checksum
from diskwalk_api import diskwalk

def find_dupes(path='/tmp'):
    dup=[]
    record={}
    d=diskwalk(path)
    files=d.enumeratepaths()
    for file in files:
        compound_key=(os.path.getsize(file),create_checksum(file))
        if compound_key in record:
            dup.append(file)
        else:
            record[compound_key]=file
    return dup

if __name__=='__main__':
    dupes=find_dupes()
    for dup in dupes:
        print 'Duplicate: %s'%dup
