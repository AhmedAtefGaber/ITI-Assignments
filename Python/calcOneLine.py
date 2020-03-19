#!/usr/bin/env python3

eqn=input("enter an equation : ")
opr = []

for i in eqn :
    if not (i.isdigit()):
        opr.append(i)

nums = [''] * (len(opr) + 1)
j = 0

for i in eqn :
    if i.isdigit() :
        nums[j] += i
    else:
        j += 1

for i in range(len(nums)) :
    nums[i] = int(nums[i])

res = nums[0]

for i in range(len(opr)) :
    if opr[i] == '+' :
        res += nums[i+1]
    elif opr[i] == '-' :
        res -= nums[i+1]
    elif opr[i] == '*'  :
        res *= nums[i+1]
    elif opr == '/' :
        res /= nums[i+1]

print(f"the result = {res} \n")




