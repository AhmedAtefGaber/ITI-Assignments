#!/usr/bin/python

import os

fname='Available_Package_Update_"`date +"%F-%H-%M-%S"`".txt'

os.system('echo -e "\t \t \t ################  Available Package Updates  ##################### "  >> %s ' % fname)
os.system('yum check-update | grep -v ^Load*  >> %s ' % fname) 

print("Done..")
os.system('echo "you can check the report file in the current directory" ' )


