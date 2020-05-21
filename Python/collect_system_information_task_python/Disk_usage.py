#!/usr/bin/python

import os

fname='Disk_Usage_Info_-"`date +"%F-%H-%M-%S"`".txt'


os.system('echo -e  "\t \t \t ################  file system disk space usage  ##################### "  >> %s '  % fname)
os.system('df -h >>  %s '  % fname)

os.system('echo -e  "\t \t \t ################   I/O  usage  ##################### "  >>  %s '  % fname)
os.system('iotop -b -n 1 >>  %s '  % fname)

print("Done...")
print("you can check the report file in the current directory")


