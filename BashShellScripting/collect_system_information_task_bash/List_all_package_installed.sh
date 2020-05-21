#!/bin/bash


fname=List_for_all_package_installed_-"`date +"%F-%H-%M-%S"`".txt

echo "there are $(yum list installed | wc -l) installed packages" >> $fname

echo -e  "\t \t \t ################  List for all package installed  ##################### "  >> $fname
yum list installed >> $fname

echo "Done.."
echo "you can check  $fname file in the current directory"
