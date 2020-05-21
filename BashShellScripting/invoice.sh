#!/bin/bash

num_goods=$(cat good |wc -l)
num_inv=$(cat invoice | tail -1 |cut -f1 -d":")
select command in add delete update display
do

if [ $command == "add" ]
then
        echo "you have chosen $command"
        echo "which tabel do you want to add to"
        select table in goods  invoice 
        do
        echo "You have chosen $table"
        
	if [ $table == "goods" ]
	then
	echo "enter the good you want to add "
	read g
	for  i in $(cut good -f2 -d":") 
	do
		if [ $i == $g ]
		then
		echo "$g is existed"
		exit 1
		fi	
	done
        echo "enter the quantity: "
	read qty
	echo "enter the unit price: "
	read unt_prc 
	echo $[num_goods+1]:$g:$qty:$unt_prc >>good
	elif [ $table == "invoice" ]
	then
	echo "enter the name of the good: "
	read name
	m=$(grep ":$name:"  good)
	if [ -z $m ]
	then
	echo "this good is not existed"
	exit 1
	else
	echo "enter the quantity "
	read qty
	q=$(grep ":$name" good |cut -f3 -d":")
	if [ $qty -g $q ]
	then
	echo "there is no enough quantity , we have only >> $q << of $name. "
	exit 1
	else
	echo "enter customer name: "
	read custname
	d=$(date)
	up=$( grep ":$name:" good | cut -f4 -d":")
	tot=$[qty*up]
	gid=$(grep ":$name:" good | cut -f1 -d":")
	echo $[num_inv+1]:$gid:$qty:$d:$tot >> invoice_details
	echo $[num_inv+1]:$custname:$d:$tot >> invoice
	new_qty=$[ q - qty ]
	echo "the new qty is $new_qty"
	cat good | awk -v up=$up -v gid=$gid -v new_qty=$new_qty -v name=$name    'BEGIN { FS = ":" ; OFS = ":" } {
						if ( name == $2 )
							{			
								print gid":"name":"new_qty":"up > "/home/ahmed/good"
							}
						else
							{
								print $1":"$2":"$3":"$4 > "/home/ahmed/good"
						}}	'		 	
	
	fi
	fi
	fi

        done

elif [ $command == "update" ]
then
        echo "you have chosen $command"
        echo "which tabel do you want to update"
        
	select table in good  invoice invoice_details
        do
        
	echo "You have chosen $table"
	
	if [ $table == "good" ] 
	then
        
	echo "enter the name of the good you want to change: "
        read name
        echo "enter the field you want to change: "
        
	select f in name unit_price quantity
        do
        
	if [ $f == "name"  ]
        then
        echo "enter the new name: "
        read new_name
        sed "s/$name/$new_name/g" good > new_good_file
        sed "s///g" good > good
        cat new_good_file > good
        sed "s///g" new_good_file > new_good_file

        fi
        done
	elif [ $table == "invoice" ]
	then
	echo "enter the ID of the invoice you want to update. "
	read id
	inv_id_check=$(grep ^$id: invoice|cut -f1 -d: )
                if [ -z $inv_id_check ]
                then
                echo "there is no invoice with the ID $id to delete."
                exit 1
                else
		echo "what do you want to update. "
		select t in customer_name date total_price quantity   
		do
		if [ $t == "customer_name" ]
		then
		echo "enter the new name. "
		read name
		cat invoice | awk -v cn=$name -v inv_id=$id    'BEGIN { FS = ":" } {
                                                if ( $1 == inv_id )
                                                        {
                                                                print $1":"cn":"$3":"$4 > "/home/ahmed/invoice"
                                                        }
                                                else
                                                        {
                                                                print $1":"$2":"$3":"$4 > "/home/ahmed/invoice"
                                                }}      '

		fi
		done 
		fi	
	


        fi
        
	done



elif [ $command == "delete" ]
then
        echo "you have chosen $command"
        echo "which tabel do you want to delete from"
        select table in good  invoice 
        do
        echo "You have chosen $table"	 
	if [ $table == "good"  ]
	then
	echo "enter the name of the good you want to delete: "
	read good_d
	good_check=$(grep :$good_d: good)
		if [ -z $good_check ]
		then
		echo "there is no good with the name $good_d to delete."
		exit 1
		else
		grep -v :$good_d: good > good_after_delete
		sed "s///g" good > good
		cat good_after_delete > good
		sed "s///g" good_after_delete > good_after_delete
		echo "the good record: $good_check is deleted "
		fi	
	elif [ $table == "invoice"   ]
	then
	echo "enter id of the invoice you want to delete: "
	read id
	inv_id_check=$( grep "^$id:" invoice|cut -f1 -d: )
		if [ -z $inv_id_check ]
		then
		echo "there is no invoice with the ID $id to delete."
                exit 1
		else
		grep -v ^$id: invoice > invoice_new
		sed "s///g" invoice > invoice
		cat invoice_new > invoice
		sed "s///g" invoice_new > invoice_new
		echo "the invoice with the ID $id is deleted."
		grep -v ^$id: invoice_details > invoice_new_details
                sed "s///g" invoice_details > invoice_details
                cat invoice_new_details > invoice_details
                sed "s///g" invoice_new_details > invoice_new_details
                
		fi 
	else
	echo "you entered invalid entry. "
	exit 1
	fi 
        done

elif [ $command == "display" ]
then
        echo "you have chosen $command"
        echo "which tabel do you want to display from"
        select table in good  invoice invoice_details
        do
        echo "You have chosen $table"
	if [ $table == good ] 
	then		
	echo "enter the name of the good you want to display: "
        read good_disp
	good_recd=$(cat good |grep :$good_disp: )
		if [ -z $good_recd  ]
		then
		echo "there is no good with the name $good_disp."
		exit 1
		else
		echo "ID:Name:Quantity:Unit Price"
		echo $good_recd	
		fi

        elif [ $table == "invoice"   ]
        then
        echo "enter id of the invoice you want to display: "
		read invoice_disp
		invoice_recd=$(cat invoice |grep ^$invoice_disp: )
                if [ -z $invoice_recd  ]
                then
                echo "there is no invoice with the ID $invoice_disp."
                exit 1
                else
                echo "InvID:CustomerName:InvDate:InvTotale"
                echo $invoice_recd
                fi

        elif [ $table == "invoice_details" ]
        then
        echo "enter id of the invoice details you want to dispaly: "
		read invoice_detl_disp
                invoice_detl_recd=$(cat invoice_details |grep ^$invoice_detl_disp: )
                if [ -z $invoice_detl_recd  ]
                then
                echo "there is no invoice with the ID $invoice_detl_disp."
                exit 1
                else
                echo "InvID:GoodID:Quantity:Date:InvTotale"
                echo $invoice_detl_recd
                fi


	fi
        done




else 
        echo not recognized operation
	exit 1
fi	


done
