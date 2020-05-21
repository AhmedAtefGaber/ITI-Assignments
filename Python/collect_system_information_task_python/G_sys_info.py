#!/usr/bin/env python3

import os

fname='General_System_Info_-"`date +"%F-%H-%M-%S"`".txt'

os.system('echo -e "\t \t \t ##################################### "  >> %s ' % fname)
os.system('echo "hostname: $(hostname)"  >> %s ' % fname)

os.system('echo -e "\t \t \t ################ OS INFO ##################### "  >>  %s ' % fname)
os.system('cat /etc/os-release >>   %s ' % fname)

os.system('echo -e "\t \t \t ################ Kernel Version ##################### "  >>  %s ' % fname)
os.system('uname -r >>   %s ' % fname)

os.system('echo -e "\t \t \t ################ IP INFO ##################### "  >>  %s ' % fname)
os.system('ifconfig >>   %s ' % fname)

os.system('echo -e "\t \t \t ################ CPU INFO ##################### "  >> %s ' % fname)
os.system('cat /proc/cpuinfo >>   %s ' % fname)

os.system('echo -e "\t \t \t ################ Memory INFO ##################### "  >>  %s ' % fname)
os.system('cat /proc/meminfo >> %s ' % fname)

print( "Done..")
os.system('echo you can check the report file in the current directory'  )

