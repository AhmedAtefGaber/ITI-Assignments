#!/bin/bash

fname=Available_Package_Update_"`date +"%F-%H-%M-%S"`".txt

echo -e "\t \t \t ################  Available Package Updates  ##################### "  >> $fname
yum check-update | grep -v ^Load* >> $fname

echo "Done.."
echo "you can check  $fname file in the current directory"

