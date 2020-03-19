#!/usr/bin/env python3


#print("\n \nthe first queestion \n")
lst=[1,2,2,1,5,5,7,2,3,4,5,6,10,11,8,8,7,8,9]
summing=0
for i in lst:
    summing +=i
print("the sum of the list items = ",summing, "\n")

################################################################3

print("\n\nthe second question \n")
max=min=lst[0]
for i in range(1,len(lst)):
        if lst[i]>max:
             max=lst[i]
        if lst[i]<min:
             min=lst[i]
print(f"the max is = {max} , and the min is = {min}\n\n")


####################################################################

print("\n\nthe third question \n\n")

lst_cp_1=[]
for i in lst:
    if i not in lst_cp_1:
        lst_cp_1.append(i)
print("the list before removing duplicates is : ",lst,"\n\n")
print("the list after removing the duplicates is : " , lst_cp_1 , "\n\n")

############################################################################

print("\n\nthe fourth question\n\n")

lst1=[10,20,30,40,50]
lst2=[110,120,130,140,150]
lst_res=[]
for i in range(len(lst1)):
    lst_res.append(lst1[i]-lst2[i])
print(f"the difference between the first list \n\n{lst1}\n\nand the second\
list\n\n{lst2}\n\nis :{lst_res}")

#############################################################################


print("\n\n the fifth question\n\n")

lst1=[1,2,3,4,5]
lst2=[6,7,8,9,10]
for i in lst2:
    lst1.append(i)
print(f"the list after being appended with another lis is : \n\n{lst1}")

###############################################################################


print("\n\nthe sixth question\n\n")

lst=[50,-3,-10,150,-100,250,200,250,100,350,-1]

for j in range(2):
    min=lst[0]
    for i in lst:
        if i < min:
            min = i
    lst.remove(min)
print("the second smallest min is : " , min)


lst=[ "ahmea" , "ahmeeeea" , "mohamed" , "mahmoum" , "mm" , "aa" , 'aaa' , 'adad' , 'm' ]
dict_res={}

for i in range(len(lst)):
    if (lst[i][0] == lst[i][-1]) and len(lst[i]) >= 2 :
        if lst[i][0] not in dict_res :
            dict_res[lst[i][0]] = 1
        else:
            dict_res[lst[i][0]] += 1

for k , v in dict_res.items() :
    print(f"\nthe strings that start and end with '{k}'  appears ( {v} ) times ) times\n")




###################################################################
print("\n\nthe question number 9\n\n")

l=[ { 'item' : 'item1' , 'amount' : 400 } , { 'item' : 'item2' , 'amount' : 300 } , \
        { 'item' : 'item1' , 'amount' : 750  } , { 'item' : 'item2' , 'amount' : 1000}  ]

dict_res={}

for i in range(len(l)):
    if (list(l[i].values())[0]) not in dict_res :
        dict_res[list(l[i].values())[0]] =  list(l[i].values())[1]
    else:
        dict_res[list(l[i].values())[0]] += list(l[i].values())[1]

print(f"the output counter dictionary is : {dict_res}\n\n")

print("\n\nthe tenth question\n\n")

Dict={ 1:100 , 2:100 , 3:300 }
ch = int(input("enter the integer key to check for "))
if ch in Dict.keys():
    print("yes , this is a key\n\n")
else:
    print("no !!, this is not a key \n\n")

###########################################################################

print("\n\nthe question number 12\n\n")

Dict={1:10 , 2:50 , 3:500 , 4:700 , 5:1000 , 6:-10 }
val =list(Dict.values())
max=min=val[0]

for i in range(1,len(val)):
    if val[i]<min:
        min = val[i]
    if val[i] > max :
        max = val[i]
print(f"the max value is : {max} , and the min value is : {min}\n\n")


########################################################

print("\n\nthe question number 13\n\n")

t=("AHMED",[13,9],7.999999,10,-1,{"ahmed":100 , "Atef":154151})
print("a tuple with differnt data types : ",t,"\n\n")


############################################################

print("\n\nthe question 16\n\n")
t = ('ahmed','atef','gaber','mohamed','osman')
s = ''
for i in t:
    s += i
    s += " "
print(s+" is the string after converting the tuple to string.\n\n")


###############################################################

print("\n\nthe question number 17\n\n")

t=(1,2,3,1,1,1,8,8,9,1,2,3,3,3,9,5,77)
l=list(t)
l_cp=l[:]
dup=[]
for i in l:
    if i in l_cp:
        l_cp.remove(i)
        if i in l_cp:
            dup.append(i)
            flag = 1
            while flag == 1 :
                 l_cp.remove(i)
                 if i not in l_cp:
                     flag = 0

print(f"the duplicate elements are : {dup} \n\n")

##########################################################

print("\n\nthe question number 18\n\n")

s1={1,2,3,6,4,5,8,9,9}
s=set({})
ch=int(input("enter anumber to delete from the set if it is existed : "))
print(s)


for i in s1:
    if i != ch :
        s.add(i)
        print(i)
print(f"the set befor deletion is {s1}")
print("the new set after deletion is : " , s , "\n\n")

###############################################################
s = { 1,2,3,4,5,6,10,100,99,-50,7,8,9,-1}
max = min = s.pop()
l=len(s)

for i in range(l):
    item = s.pop()
    if item > max :
        max = item
    if item < min:
        min = item
print(f"the max is : {max} and the min is : {min}")
