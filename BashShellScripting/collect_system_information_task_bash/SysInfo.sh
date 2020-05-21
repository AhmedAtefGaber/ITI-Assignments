#!/bin/bash

select task in "General_System_Information" "CPUMemory_Current_Usage" "Disk_Usage" "Available_Package_Updates" \
                 "List_for_all_package_installed" "ALL" "EXIT"
do
	if [ $task ==  'General_System_Information'  ]
	then
		source "./G_sys_info.sh"

        elif [ $task ==  'CPUMemory_Current_Usage'  ]
        then
                source "./CPU_Memory_Current_usage.sh"
	
	elif [ $task ==  'Disk_Usage'  ]
        then
                source "./Disk_usage.sh"

        elif [ $task ==  'Available_Package_Updates'  ]
        then
                source "./Available_Package_Update.sh"

	elif [ $task ==  'List_for_all_package_installed'  ]
        then
                source "./List_all_package_installed.sh"

	elif [ $task ==  'ALL'  ]
        then
                source "./G_sys_info.sh" &&  source "./CPU_Memory_Current_usage.sh" && source "./Disk_usage.sh" &&  \
		source "./Available_Package_Update.sh" && source "./List_all_package_installed.sh"


	else 
		exit 0
	fi
exit 0
done
