#!/usr/bin/env python3
from math import sqrt

########################################################
print("\nthe first question \n#####################\n")

first=input("enter your first name:  ")
last=input("enter your last name:  ")
print(last + ' ' +first+"\n")


#################################################################3
print("\nthe second question \n####################\n")

n=int(input("enter an integer number : "))
print(f"the result is :{n*3+n*2*10+n*100}\n")
##################################################################

print("\nthe third question\n######################\n")
n=int(input("enter a number : "))
print(f"the result is : {abs(17-n)*2}\n")
####################################################################

print("\nthe fourth question\n######################\n")

n1=int(input("enter the first number :  "))
n2=int(input("enter the second nunber :  "))
n3=int(input("enter the third number : "))
if n1 == n2 ==n3:
    print(f"as the three numbers are equal then the sum is:  {n1*9}\n")
else:
    print(f"you entered three differnet numbers.so, the sum is : {n1+n2+n3}\n")

##########################################################################
print("\nthe fifth question\n########################\n")
name=input("enter a name : ")
for i in range(len(name)):
    pass
print(f"your name has {i+1} characters\n")

print("\nthe sixth question\n######################")
word=input("enter a word : ")
word_r=''
for i in range(len(word)-1,-1,-1):
    word_r +=word[i]
print("the reverse of the word you entered is :  " + word_r + "\n" )
##########################################################################
print("\nthe seventh question\n########################\n")
for i in range(7):
    if (i != 3) and  (i != 6):
        print(i)

###########################################################
print("\n the calcultor questiion \n")

res = 0
i = 0
flag = 1
#num1=int(input("enter a number : "))
while flag :

    i += 1
    if i == 1:
        num1 = int(input("enter a number : "))
        res = num1
    else:
         opr = input("enter the operation: your avilable operations are ( + , - , / , * , SQRT , = ) : ")
         if opr == '=' :
             print(f"the result is : {res}")
      #       flag = 0
             break
         num1 = int(input("enter a number : "))
         if opr=='+' :
             res+=num1

         elif opr=='-':
             res-=num1

         elif opr == '*':
