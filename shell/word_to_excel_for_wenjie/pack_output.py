#!/usr/bin/python
#coding:utf-8
import time
import zipfile
import os

t=time.ctime()
zipname='/var/ftpadmin/forwenjie/file_output/会员表@%s.zip'%t
path='/var/ftpadmin/forwenjie/file_output/'
files=[]
for dirpath,dirnames,filenames in
os.walk('/var/ftpadmin/forwenjie/file_output'):
    files+=filenames
if files!=[]:

    zip=zipfile.ZipFile(zipname,'w')
    for file in files:
        fullname=path+file
        zip.write(fullname)
        os.remove(fullname)
    zip.close()

