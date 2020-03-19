#!/usr/bin/env python3
import random

'''

given two points repersented as x1, y1, x2, y2
return float distance, between them considering the fllowing the distance equation
--------------------

consider dividing a string into two halves
case1: the length is even, the front and  back halves are the same length

case 2:
the length is odd, we'll say the extra char goes in the front half,
e.g
abcde', the front half is 'abc', the back half'de.

given 2 strings, a and b, return a string of the form:
(a-front + b-front) + (a-back + b-back)

# program takes command line arg this arg is the name of a txt.file
the program reads all the txt and split them and calc the 20 common used word
file name: popular_wods.txt
hint, my_str.split()


#guess game
*
1-- generate a random number and
2-- give only 10 tries for the user to guess that number
3-- get user input and compare it with the random number.
4-- display a hint message to the user in case the user number is smaller or bigger of the random number
4-- if user type a number out of range(100),
display a message that is not allowed and don't count this a s a try
5-- in case the user entered a correct number within the 10 tries, display a congratulations message and let your application guess another random number
with the reamin number of traies.
* if user finish his all tries, display a message to ask hom
if he want to play a gain or not.
*Next time the user open the game, he receives a welcome message tells him the nimebr of
games he played, how many times he won and how many he lost,


'''

def div_half(s):
    
    if len(s) % 2 == 0 :
        s1 = s[:len(s)//2]
        s2 = s[len(s)//2:]
    else:
        s1 = s[:len(s)//2 + 1]
        s2 = s[len(s)//2 + 1:]
    return s1,s2
        
s1 = "ahmed"
s2 = "atef"
print(div_half(s2))

def combine_str(s1,s2):

    s = ''
    s1_f , s1_b = div_half(s1)
    s2_f , s2_b = div_half(s2)
    s = "(" + s1_b + s2_b + ")" + "(" + s1_f + s2_f + ")"
    print(s)

combine_str(s1,s2)


def popular_wods(f_path) :
    
    dict_res = {}
    f=open(f_path,"r")
    words = (f.read()).split(" ")
    for i in words:
        if i not in dict_res:
            dict_res[i] = 1
        else:
            dict_res[i] += 1
    res_sorted_keys = sorted(dict_res, key=dict_res.get, reverse=True)
    
    j=0
    for i in res_sorted_keys:
        print(i,dict_res[i])
        if j == 20:
            break
        else:
            j += 1
        
popular_wods("./mockingjay.txt")



def lets_play1(i,num):

    guess =int(input(f"\nyou have {10-i} trails\nenter yor guess : "))
    flag = 1
    while flag:
        i += 1
        if i >= 10 :
            print("\nloooooooooooser\n")
            flag = 0
        else:
            if guess == num :
                print("\nbro you are amazing\n")
                flag = 0
            else :
                if guess > 100:
                    print("\nenter a number smaller than 100\n")
                    i -= 1
                    guess =int(input(f"\nyou have {10-i} trails\nenter yor guess : "))
                if guess < num :
                    print("your guess is smaller than the number\n")
                    guess =int(input(f"\nyou have {10-i} trails\nenter yor guess : "))
                else:
                    print("your guess is bigger than the number\n")
                    guess =int(input(f"\nyou have {10-i} trails\nenter yor guess : "))
    return i  
                    

def play():
    i = 0
    num = random.randint(1,100)
    
    i =lets_play1(i,num)
    if i < 10:
       print("\nlets play again\n")
       print(i,"\n")
       num = random.randint(1,100)
       i = lets_play1(i,num) 

play()       

