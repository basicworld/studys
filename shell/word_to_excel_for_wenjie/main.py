#!/usr/bin/python
#coding:utf-8
import subprocess
import os
import time

#this is the *.py master, you just need to run this .py to finish your work

os.chdir('/root/SHELL/word_to_excel_for_wenjie')
#test and zip all the file to ./history
subprocess.call(r'python ./test.py',shell=True)
#run the auto fill
subprocess.call(r'python ./read.py',shell=True)
subprocess.call(r'python read_company.py',shell=True)
#zip and send message
t=time.ctime()

subprocess.call(r'python ./mail.py',shell=True)


