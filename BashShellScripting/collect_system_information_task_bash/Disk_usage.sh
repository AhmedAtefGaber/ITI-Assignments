#!/bin/bash

fname=Disk_Usage_Info_-"`date +"%F-%H-%M-%S"`".txt


echo -e  "\t \t \t ################  file system disk space usage  ##################### "  >> $fname
df -h >> $fname

echo -e  "\t \t \t ################   I/O  usage  ##################### "  >> $fname
iotop -b -n 1 >> $fname

echo "Done.."
echo "you can check  $fname file in the current directory"

