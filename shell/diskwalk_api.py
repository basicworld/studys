#!/usr/bin/python
#coding:utf-8
#docs:this is a .sh with function similiar to 'tree'
import os
class diskwalk(object):
    def __init__(self,path):
        self.path=path

    def enumeratepaths(self):
        '''return the path to all the files in a directory'''
        path_collection=[]
        for dirpath, dirnames, filenames in os.walk(self.path):
            for file in filenames:
                fullpath=os.path.join(dirpath,file)
                path_collection.append(fullpath)
        return path_collection


    def enumeratefiles(self):
        '''return all the files in a directory'''
        file_collection=[]
        for dirpath, dirnames, filenames in os.walk(self.path):
            for file in filenames:
                file_collection.append(file)

        return file_collection

    def enumeratedir(self):
        '''return all the directories in a directory'''
        dir_collection=[]
        for dirpath, dirnames, filenames in os.walk(self.path):
            for dir in dirnames:
                dir_collection.append(dir)
        return dir_collection

if __name__=='__main__':
    default_path=os.getcwd()
    while True:
        print 'please input your path([y|yes|Enter] for', default_path,'):'
        path=raw_input()
        if (path=='yes' or path=='y' or path==''): path ='./'
        try:
            os.chdir(path)
            break
        except OSError:
            continue
    disk=diskwalk(path)


    print '---------Recursive listening of all paths in a dir---------'
    if len(disk.enumeratepaths())>0:
        for path in disk.enumeratepaths():
            print path
    else:
        print '!!No result!!'

    print '\n---------Recursive listening of all files in a dir---------'
    if len(disk.enumeratefiles())>0:
        for file in disk.enumeratefiles():
            print file
    else:
        print '!!No result!!'
    print '\n---------Recursive listening of all dirs in a dir---------'
    if len(disk.enumeratedir())>0:
        for dir in disk.enumeratedir():
            print dir
    else:
        print '!!No result!!'
