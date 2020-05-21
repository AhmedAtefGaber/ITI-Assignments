#!/bin/bash

fname=CPU_MEM_Info_-"`date +"%F-%H-%M-%S"`".txt

echo  -e  "\t \t \t ################ top processes ##################### "  >> $fname
top -b -n 1 >> $fname

echo -e  "\t \t \t ################ memory usage ##################### "  >> $fname
free >> $fname

echo "Done.."
echo "you can check  $fname file in the current directory"

