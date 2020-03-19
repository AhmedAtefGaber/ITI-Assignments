#!/usr/bin/env python3
'''
problem 1:
    create class math
        -has method class calc 
            take 2 operand and one operator
        - hanlde errors like -> if operand not numuric,
                                division by zero,
                                strange operator like @

problem 2:
    create class AgeCalc:
        - has method class getAge take birth_date
            return yearOld, monthOld, dayOld
    create class person inheritance from AgeCalc:
        - has attributes -> fname, lname, birth_date, age

        - has methods class:    
          * get person data -> take from user his data,
          * welcome method -> print -> Welcome Mr/Mrs fname and lname
                              you are *** years, **** month, **** days





'''
#################### problem 1 ##########################
class Math:
    def calc(self,num1,num2,opr):

        if isinstance(num1,int) and isinstance(num2,int):
            if opr == "+":
                print(f"the result of {num1} {opr} {num2} = {num1+num2}")
            elif opr == "-":
                print(f"the result of {num1} {opr} {num2} = {num1-num2}")
            elif opr == "*":
                print(f"the result of {num1} {opr} {num2} = {num1*num2}")
            elif opr == "/":
                if num2 == 0:
                    print("error >> division by zero.")
                else:
                    print(f"the result of {num1} {opr} {num2} = {num1/num2}")

            else:
                print("not a number")

expr1=Math()
expr1.calc(5,0,"/")


#################### problem 2 ##########################


class AgeCalc:

    def getAge(self,birth_date):
        dy_of_mon=[31,28,31,30,31,30,31,31,30,31,30,31]
        date=birth_date.split(":")
        tody_date = "10:01:2020".split(":")
        tody_days=int(tody_date[0])
        days = int(date[0])
        for i in range(int(date[1])-1):
            days = days + dy_of_mon[i]
        for i in range(int(tody_date[1])-1):
            tody_days = tody_days + dy_of_mon[i]
        if tody_days >= days :
            num_years = int(tody_date[2]) - int(date[2])
            num_mons = (tody_days - days) // 30
            num_days = (tody_days - days ) % 30
        else:
            num_years = int(tody_date[2]) - int(date[2]) - 1
            num_mons = ( tody_days - days + 365 ) // 30
            num_days = ( tody_days - days + 365 ) % 30
        return { "yearOld" : num_years , "monthOld" : num_mons , "dayOld" : num_days }

class Person(AgeCalc):
   # data={"fname":0,"lname":0,"birth_date":0,"age":0}

    def __init__(self):
        self.getdata()

    def getdata(self):
        self.fname=input("Enter your First Name: ")
        self.lname=input("Enter your last Name: ")
        self.birth_date=input("enter your birth date separated by ':' : ")
        while int(self.birth_date.split(":")[2]) > 1997 or int(self.birth_date.split(":")[2]) < 1960  :
                if int(self.birth_date.split(":")[2]) > 1997 :
                    print("not allowed, you are so young.")
                    self.birth_date=input("enter your birth date separated by ':' : ")
                else:
                    print("not allowed, you are too old.")
                    self.birth_date=input("enter your birth date separated by ':' : ")
        self.age=int(input("enter your age: "))


        return [self.fname,self.lname,self.birth_date,self.age]


    def welcome(self):

        date=AgeCalc.getAge(self,self.birth_date)
        print(f"Welcome Mr/Mrs {self.fname} {self.lname} you are {date['yearOld']} years, {date['monthOld']}  month, {date['dayOld']} days")

ahmed=Person()
ahmed.welcome()

