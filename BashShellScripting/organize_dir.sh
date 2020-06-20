#!/bin/bash

#organize a given directory

mkdir images music videos 
mv $(ls | grep -e *.jpg -e *.png) images/
mv $(ls | grep -e *.mp3 -e *.flac) music/
mv $(ls | grep -e *.avi -e *.mov) videos/
rm -f $(ls | grep -e *.log)
