#!/usr/bin/python
#coding:utf-8
#there are three ways to interacte with you when delete /tmp/*
import os
import sys
path=os.getcwd()
sys.path.append(path)

class Delete(object):
    def __init__(self,file):
        self.file=file

    def interactive(self):
        input=raw_input('Do you really want to delete %s [N]|Y: '%self.file)
        if input.upper()=='Y':
            print 'Deleting: %s'%self.file
            for fi in self.file:
                status=os.remove(fi)
        else:
            print 'Skipping: %s'%self.file
        return

    def dryrun(self):
        for fi in self.file:
            print 'Dry run: %s [Not deleted]'%self.file
        return

    def delete(self):
        for fi in self.file:
            print 'Deleting: %s'%self.file
            try:
                status=os.remove(self.file)
            except Exception,err:
                print err
                return status

if __name__=='__main__':
    print '---------------------------------------------'
    from find_dupes import find_dupes
    dupes=find_dupes('/tmp')

    if dupes==[]:
        print 'No duplicate files in /tmp'
    else:
        for dup in dupes:
            delete=Delete(dupes)
#            delete.dryrun()
            delete.interactive()
#            delete.delete()
