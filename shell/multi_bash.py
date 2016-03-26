#!/usr/bin/python
#coding:utf-8
'''use this function you can do many bash jobs in one line'''
import subprocess

def multi(*args):
    for cmd in args:
        print '--------------------------------------------------------'
        p=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
        out=p.stdout.readlines()
        for line in out:
            print line.strip()
        print
