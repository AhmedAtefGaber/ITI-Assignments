#!/usr/bin/python

import os , sys

prnt= """
      1) General_System_Information      5) List_for_all_package_installed 
      2) CPUMemory_Current_Usage         6) ALL                             
      3) Disk_Usage                      7) EXIT                            
      4) Available_Package_Updates
      """         
print(prnt)
task=int(input('Enter the Task Number: '))

if task == 1 :
    os.system('python "./G_sys_info.py"')
elif task == 2 :
    os.system('python "./CPU_Memory_Current_usage.py"')
elif task == 3 :
    os.system('python "./Disk_usage.py"')
elif task == 4 :
    os.system('python "./Available_Package_Update.py"')
elif task == 5 :
    os.system('python "./List_all_package_installed.py"')
elif task == 6 :
    os.system('python "./CPU_Memory_Current_usage.py" && python "./G_sys_info.py" && python "./Disk_usage.py" &&\
               python "./Available_Package_Update.py" && python "./List_all_package_installed.py" ')
else:
    sys.exit(0)
