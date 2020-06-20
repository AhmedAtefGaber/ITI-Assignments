#!/bin/bash

log=$(ls -r | grep -e  ^error.log -e ^access.log)
re='^[0-9]+$'

for f in  ${log}
do

        last=$(echo ${f}| grep -Po '.(?=.{0}$)')


        if  [[ $last =~ $re ]]
        then
                iferr=$(echo ${f} | grep ^error )
                exit_status=$?
                if [ $exit_status -eq 0 ]
                then
                mv ${f} error.log.$[last+1]
                else
                mv ${f} access.log.$[last+1]
                fi
        else
                mv ${f} ${f}.1
                touch error.log
                touch access.log
        fi

done