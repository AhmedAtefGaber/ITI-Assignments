#!/usr/bin/env python3
from lab1 import *

'''
bouns **
create app user command interface
    print menu for the user with operation 
    he can do and the key word to enter for running an operation
    for example:
    - for adding new employee enter "add"
    - if manager press 'm' 
    - if employee press 'e'
    please insert data:
    Name: >>
    Age: >>
    And so on.
    the final option in the menu should be q 
    for exiting the program and select all data user entered in file and displayed it 



'''

while (1):

    opr=input("if you want to add new employee enter >> add <<: ")
    while ( opr != "add"):
        print("you entered an invalid entry.")
        opr=input("if you want to add new employee enter >> add <<: ")


    typ=input("if manager press >> m << if employee press >> e << : ")
    while (typ !="e" and typ != "m"):
        print("you entered an invalid entry.")
        typ=input("if manager press >> m << if employee press >> e << : ")


    print("please insert these data :")
    fname=input("first name >>  ")
    lname=input("last name >>  ")
    dep=input("department >>  ")
    try:
        age=int(input("Age >>  "))
    except:
        age="invalid"
    try:
        sal=int(input("salary >>  "))
    except:
        sal="invalid"
    if (typ == "m" and opr == "add"):
        m_dep=input(f"enter the dapatement name which managed by {fname} {lname} : ")
        mgr=manager(fname,lname,age,dep,sal,m_dep)
        print("you enterd this manager record.")
        mgr.show()
    else:
        emp=employee(fname,lname,age,dep,sal)
        print("you enterd this employee record.")
        emp.show()
