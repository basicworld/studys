#!/usr/bin/python
#coding:utf-8

import platform

'''
fingerprint the following operating systems:
*Mac OS X
*UBUNTU
*Centos
*FreeBSD
*Sunos

'''

class OpSysType(object):
    def __getattr__(self,attr):
        if attr=='osx': return 'osx'
        elif attr=='rhel': return 'redhat'
        elif attr=='ubu': return 'ubu'
        elif attr=='fbsd': return 'ofbsd'
        elif attr=='sun': return 'SunOS'
        elif attr=='unknown_linux': return 'unknown_linux'
        elif attr=='unknown': return 'unknown'
        else: raise AttributeError,attr

def linuxType(self):

