#!/bin/bash
#this shell will be used to mv /var/ftpadmin/uploadfromwin/public_file_saves_here/ 
#to /var/ftp/pub/

if [ -n /var/ftpadmin/uploadfromwin/public_file_saves_here/ ]
then
mv /var/ftpadmin/uploadfromwin/public_file_saves_here/* /var/ftp/pub/
fi

