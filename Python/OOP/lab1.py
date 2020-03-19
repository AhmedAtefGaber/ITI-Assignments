#!/usr/bin/env python3
'''
create class employee with the following characteristics:

* Attributes:
* first_name
* last_name
* Age
* department
* Salary
* static list container all the employees

* Methods:
* constructor:
    Assign values to the instance Attributes
    insert the create object to the list
    insert new record in file employee

* transfer()
     change employee dpartment
     update file record employee with the update

* fire()
    remove employee from list
    remove employee from file

* show()
    prints all employees data

* list_employee()
    select all employees from file and print thier data



proplem2:
- create class Manager:
class manager inherits from class employee
with additional department managed_deparment

method:
show()
    print all data except salary will print condfidentianl 
    instead of the salary value


'''


##########  promlem 1  #################


class employee:
    emp_cont=[]
    ID=0
    
    with open('employee',"r") as f:
        lines=f.readlines()
    for l in lines:
        ID=ID+1

    def __init__(self,fname,lname,age,dep,sal):
        self.fname=fname
        self.lname=lname
        self.age=age
        self.dep=dep
        self.sal=sal
        employee.emp_cont.append(self)
        employee.ID = employee.ID +1
        self.ID=employee.ID
        l=str(self.ID)+":"+self.fname+":"+self.lname+":"+str(self.age)+":"+self.dep+":"+str(self.sal)
        f=open('employee',"a")
        f.write(l)
        f.write("\n")

    def transfer(self,chng_dep):
        with open("employee","r") as f:
            lines=f.readlines()
        with open("employee","w") as f:
            for line in lines:
                ll=str(self.ID)+":"+self.fname+":"+self.lname+":"+str(self.age)+":"+self.dep+":"+str(self.sal)
                if line.strip("\n") != ll :
                    f.write(line)
        self.dep=chng_dep
        l=str(self.ID)+":"+self.fname+":"+self.lname+":"+str(self.age)+":"+self.dep+":"+str(self.sal)
        f=open("employee","a")
        f.write(self.l)
        f.write("\n")

    def fire(self):
        employee.emp_cont.remove(self)
        with open("employee","r") as f:
            lines=f.readlines()
        with open("employee","w") as f:
            for line in lines:
                l=str(self.ID)+":"+self.fname+":"+self.lname+":"+str(self.age)+":"+self.dep+":"+str(self.sal)
                if line.strip("\n") != l :
                    f.write(line)
    def show(self):
        print("ID:fname:lname:age:dep:sal")
        print(self.ID,":",self.fname,":",self.lname,":",self.age,":",self.dep,":",self.sal)

    def list_employee(self):
        f=open("employee","r")
        with open("employee","r") as f:
            lines=f.readlines()
        for line in lines:
                print(line)
##################  	Problem2	####################
class manager(employee):

    def __init__(self,fname,lname,age,dep,sal,managed_deparment):
        employee.__init__(self,fname,lname,age,dep,sal)
        self.managed_deparment=managed_deparment
        ll=str(self.ID)+":"+self.fname+":"+self.lname+":"+str(self.age)+":"+self.dep+":"+str(self.sal)+":"+self.managed_deparment
        with open("employee","r") as f:
            lines=f.readlines()
        with open("employee","w") as f:
            for l in range(len(lines)-1):
                    f.write(lines[l])
        f=open("employee","a")
        f.write(ll)
        f.write("\n")

    def show(self):
        print("ID:fname:lname:age:dep:sal:managed_deparment")
        print(self.ID,":",self.fname,":",self.lname,":",self.age,":",self.dep,":","condfidentianl",":",self.managed_deparment)
