#!/usr/bin/python

import os

fname='List_for_all_package_installed_-"`date +"%F-%H-%M-%S"`".txt'

os.system('echo "there are $(yum list installed | wc -l) installed packages" >> %s ' % fname)

os.system('echo -e  "\t \t \t ################  List for all package installed  ##################### "  >> %s ' % fname)
os.system('yum list installed >> %s ' % fname)

print("Done..")
print("you can check the report file in the current directory")

