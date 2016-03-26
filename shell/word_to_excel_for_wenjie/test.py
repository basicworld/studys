#!/usr/bin/python
#coding:utf-8
import subprocess
#clear ./file_ouput
import zipfile
import os
import time
e=0
try:
    os.chdir('/var/ftpadmin/forwenjie/file_output')
except:
    subprocess.call('mkdir -p /var/ftpadmin/forwenjie/file_output',shell=True)
    e+=1
if __name__=='__main__' and e!=0:
    print 'mkdir -p /var/ftpadmin/forwenjie/file_output'
files=[]
e=0
try:
    os.chdir('/var/ftpadmin/forwenjie/history')
except:
    subprocess.call('mkdir -p /var/ftpadmin/forwenjie/history',shell=True)
if e!=0 and __name__=='__main__':
    print 'mkdir -p /var/ftpadmin/forwenjie/history'

for dirpath,dirnames,filenames in os.walk('/var/ftpadmin/forwenjie/file_output'):
    files+=filenames
t=time.ctime()
zipname='/var/ftpadmin/forwenjie/history/history@%s.zip'%t
path='/var/ftpadmin/forwenjie/file_output/'
if files!=[]:

    zip=zipfile.ZipFile(zipname,'w')
    for file in files:
        fullname=path+file
        zip.write(fullname)
        os.remove(fullname)
    zip.close()


