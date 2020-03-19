#!/usr/bin/env python3

import string
from math import sqrt
#####################################################################
# 1-- Write a Python program to append a list to the second list.


l1 = [10 ,20 , 30 , 40 ,50]
l2 = [60 ,70 , 80 ,90  ,10]

def l_append(l1,l2):

    while l2 != [] :
        l1.append(l2.pop())

    return l1

print(f"\n\nthe resulted list is : {l_append(l1,l2)} \n\n")


#######################################################################
#2-- Write a Python program to get the 4th element and 4th element from last of a tuple.

t = ( 1 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 , 13 , 14 , 15 , 16 )

def get_4th (t) :

    print(f"\n\nthe 4th element is : ( {t[3]} ) and the fourth element from last is : ( {t[-4]} ) \n\n ")

get_4th(t)


#############################################################################
#3-- Write a Python program to check whether an element exists within a tuple.
t = ( 1 , 'ahmed' , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 , 13 , 'atef' , 14 , 15 , 16 )


def element_check( t=t ) :
    ch = input("\nenter the element you want to check for : ")
    if ch.isdigit() :
        ch = int(ch)

    flag = 1
    i = 0

    while flag :
        if t[i] == ch :
            print(f"\nyes, {ch} exists in the tuple \n\n")
            flag = 0
        else:
            if i < len(t)-1 :
                i += 1
            else:
                print(f"\nno!!, {ch} does not exist in the tuple \n\n")
                flag = 0
element_check(t)
##############################################################################

#4-- Write a Python program to find those numbers which are divisible by 7 and multiple of 5,
# between two given numbers (both included)


def check_7_5 ( ) :

    l = int(input("\nenter the lower bound : "))
    u = int(input("\nenter the upper bound : "))
    res = []

    for i in range(l,u+1):
        if ((i % 7) == 0) and (i % 5 == 0) :
            res.append(i)

    if res == [] :
        print(f"\nthere is no numbers between  {l}  and  {u}   which are divisible by 7 and multiple of 5\n")
    else:
        print(f"\n{res} between  {l}  and  {u} are divisible by 7 and multiple of 5\n")

check_7_5()
############################################################################3
#5-- Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).

def dist (x1,x2,y1,y2 ):
    return sqrt(pow(x1-x2,2)+ pow(y1-y2,2))

print(f"\nthe distance is : {dist(3,7,2,8)} \n\n")


###########################################################################
'''
6-- Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
If the given string already ends with 'ing' then add 'ly' instead.
If the string length of the given string is less than 3, leave it unchanged.
'''

def chg_string(s):
    s1=s
    if len(s) >= 3:
        if s[-3:] == 'ing' :
            s += 'ly'
        else:
            s += 'ing'
    print(s1 +" ==> " + s)

s = ['bring' , 'ff ' , 'end' , 'string' , 'so' ]
for i in s:
    chg_string(i)

#############################################################################################
'''
8-- Write a Python program which iterates the integers from 1 to n.
    For multiples of three print "Fizz" instead of the number and for the multiples of five print
    "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

'''

def beeb(n):

    print("\n")

    for i in range(1,n+1):
        if i % 3 ==0 and i % 5 != 0 :
            print('Fizz',end=' ')
        elif i % 5 == 0 and i % 3 != 0:
            print('Buzz',end=' ')
        elif i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz',end=' ')
        else:
            print(i,end=' ' )

    print("\n")

beeb(15)
#############################################################################################

'''
9-- Write a Python program that accepts a string and calculate the number of digits and letters.
# Use a separate condition for each validity rule
'''
s = "      ahmed  13 atef 99         "

def calc_num_let (s) :

    let = 0
    dig = 0

    for i in s :
        if i.isdigit() :
            dig += 1
        elif not(i.isdigit()) :
            if i != ' ' :
                let += 1
    return dig , let

dig , let = calc_num_let (s)
print(f"\nthe number of the digits = {dig} , \nthe number of digit = {let}   \n")

###############################################################################

'''
10-- Write a Python program to check the validity of a given password.
    Validation :

     1   At least 1 letter between [a-z] and
     2   1 letter between [A-Z].
     3   At least 1 number between [0-9].
     4   At least 1 character from [$#@].
     5   Minimum length 6 characters.
     6   Maximum length 16 characters.
'''

def validate_pass (Pass) :

    low_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    checked = [ False ] * 6
    acceptance = False
    for i in Pass:
        if i in low_case :
            checked [0] = True
        if i in low_case :
            checked [1] = True
        if i.isdigit() :
            checked [2] = True
        if i in "$#@" :
            checked [3] = True
    if len(Pass)>= 6 :
        checked [4] = True
    if len(Pass) <= 16 :
        checked [5] = True

    if False not in checked :
        acceptance = True
        print("\nthe password is accepted.\n")
    else :
        print("\nthe password is rejected.\n")
Pass = "ahmed1996"

validate_pass( Pass )

#########################################################################

#11-- Write a Python program to create the multiplication table (from 1 to 10) of a given number.


for i in range(1,11):
    for j in range(1,11):
       # if i == 1:
       #     print(f"tabele of{j}",end=' ')
        #    print("\n")
        print(f"{i}*{j}={i*j}" , end='     ')
    print("\n")

######################################################################

'''
12-- Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
     If the given string already ends with 'ing' then add 'ly' instead.
     If the string length of the given string is less than 3, leave it unchanged.
'''

### repeated#########3


#Write a Python program to remove the characters which have odd index values of a given string.
def rm_odd(s):
    s_rm = ""
    for i in range(len(s)) :
        if i%2 == 0:
            s_rm += s[i]
    return s_rm

s = "a1h3m5e7d8"

print(f"the edited string becomes: {rm_odd(s)}")

#Write a Python program to calculate the sum and average of n integer numbers


def cal_sum_avg(nums):
    Sum=0
    for i in nums:
        Sum += i
    avg=Sum / len(nums)
    return Sum , avg

nums = [ 10 , 20 , 30 , 40 ]
Sum ,avg = cal_sum_avg(nums)

print(f"sum = {Sum} , average = {avg} .")

###############################################################################


'''
#15-- Write a Python program to print the following pattern
1
22
333
4444
55555
666666
7777777
...n
'''

for i in range(1,8):
    print(f"{str(i)*i}")
print("...n")
###########################################################################

'''
16-- Write a Python program to construct the following pattern
  using a nested for loop and a given (n) number
*
* *
* * *
* * * *
* * * * n
* * * *
* * *
* *
*
'''
n = 8

for i in range(1,n+1):
    if i != n:
        print(f"{'* '*i}")
    else:
        print(f"{'* '*(n-1)}",n)
for i in range (n-1,0,-1):
     print(f"{'* '*i}")


