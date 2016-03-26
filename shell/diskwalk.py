#!/usr/bin/python
#coding:utf-8
#docs:this is a .sh with function similiar to 'tree'

import os
path='./'

def enumeratepaths(path=path):
    '''return the path to all the files in a directory'''
    path_collection=[]
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            fullpath=os.path.join(dirpath,file)
            path_collection.append(fullpath)
    return path_collection


def enumeratefiles(path=path):
    '''return all the files in a directory'''
    file_collection=[]
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            file_collection.append(file)

    return file_collection

def enumeratedir(path=path):
    '''return all the directories in a directory'''
    dir_collection=[]
    for dirpath, dirnames, filenames in os.walk(path):
        for dir in dirnames:
            dir_collection.append(dir)
    return dir_collection

if __name__=='__main__':
    print '---------Recursive listening of all paths in a dir---------'
    for path in enumeratepaths():
        print path
    print '\n---------Recursive listening of all files in a dir---------'
    for file in enumeratefiles():
        print file
    print '\n---------Recursive listening of all dirs in a dir---------'
    for dir in enumeratedir():
        print dir
