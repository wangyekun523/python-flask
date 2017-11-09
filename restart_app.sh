#!/bin/bash
while :
do
   ps -ef|grep app.py|grep -v grep
   if [ $? -ne 0 ] ;then
     sudo python $app start   
     echo "starting"
   else
     echo "runing....."
   fi
   sleep 100
done
