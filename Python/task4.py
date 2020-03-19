f1=open("./task1.py",'r')
f2=open("./task2.py",'r')
f3=open("./task3.py",'r')
f4=open("./result.py",'a')

new=[f1,f2,f3]

for i in new:
    for j in i.read():
        f4.write(j)
 

