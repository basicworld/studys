#!/bin/bash

echo connect to mysql

mysql -u root -p test
echo select something

mysql -e "select * from hello;"
