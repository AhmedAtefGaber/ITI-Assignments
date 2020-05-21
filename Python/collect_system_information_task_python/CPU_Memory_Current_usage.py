#!/usr/bin/python

import os

fname='CPU_MEM_Info_-"`date +"%F-%H-%M-%S"`".txt'

os.system('echo  -e  "\t \t \t ################ top processes ##################### "  >> %s ' % fname)
os.system('top -b -n 1  >> %s ' % fname)

os.system('echo -e  "\t \t \t ################ memory usage ##################### "  >> %s ' % fname)
os.system('free  >> %s ' % fname)

os.system('echo "Done.."')
os.system('echo "you can check the report file in the current directory"  ')


