#!/bin/bash

fname=General_System_Info_-"`date +"%F-%H-%M-%S"`".txt

echo -e "\t \t \t ##################################### "  >> $fname
echo "hostname: $(hostname)"  >>  $fname


echo -e "\t \t \t ################ OS INFO ##################### "  >> $fname
cat /etc/os-release >>  $fname

echo -e "\t \t \t ################ Kernel Version ##################### "  >> $fname
uname -r >>  $fname

echo -e "\t \t \t ################ IP INFO ##################### "  >> $fname
ifconfig >>  $fname

echo -e "\t \t \t ################ CPU INFO ##################### "  >> $fname
cat /proc/cpuinfo >>  $fname

echo -e "\t \t \t ################ Memory INFO ##################### "  >> $fname
cat /proc/meminfo >>  $fname

echo "Done.."
echo "you can check  $fname file in the current directory"

