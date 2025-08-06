#print this is my first prog in python
'''print("this is my first program in python")'''

#assign values and print types
'''a=5
print(a,type(a))
b=3.6
print(b,type(b))
c=True
print(c,type(c))
d="hi"
print(d,type(d))
e=3j+6
print(e,type(e))'''

#input student details
'''rollnumber=int(input("enter roll number:"))
batch=input("enter batch:")
course=input("enter course:")
name=input("enter name:")
percentage=(input("enter percentage:"))
print("my name is",name,"from batch",batch,".I enrolled in",course,"course. I scored",percentage,"in 12th grade.")'''

#avg marks
'''maths=int(input("enter maths marks:"))
physics=int(input("enter physics marks:"))
chemistry=int(input("enter chemistry:"))
avg=(maths+physics+chemistry)/3
print(avg)'''

#calculator
'''a=int(input("enter a:"))
b=int(input("enter b:"))
number=int(input("enter number:"))
if(number==1):
    print("add=",a+b)
elif(number==2):
    print("sub=",a-b)
elif(number==3):
    print("mul=",a*b)
else:
    print("div=",a/b)'''

#check ID
'''a=7
print(id(a))
b=9.7
print(id(b))
c="hello"
print(id(c))'''

#compare 2 numbers
'''a=int(input("enter number:"))
b=int(input("enter number:"))
if(a>b):
    print("a is greater")
elif(a<b):
    print("a is smaller")
else:
    print("equal")'''

#week2
#Ques 1
''' i=1
 while(i<11):
     print(i)
    if(i==5):
       break
    i+=1'''

#Ques 2
'''i=0
while(i<=10):
    i+=1
    if(i==5):
        continue
    print(i)'''
    


#Ques 3
'''nums=[1,2,3,4,5,6,7,8,9,-4,-6,-2,-9]
for i in nums:
    if(i<0):
        pass
        print(nums)'''

#Ques 4
'''i=1
while(i<11):
    print(i)
    i+=1'''

#Ques 5

#Ques 6
'''n=int(input("enter number:"))
factorial=1
if(n==0 or n==1):
    print("factorial is 1")
elif(n<0):
    print("no factorial")
else:
    for i in range(1,n+1):
        factorial=factorial*i
        print("fact=",factorial)'''

#Ques 7
'''n=int(input("enter table:"))
for i in range(1,11):
    print(n,"*",i,"=",n*i)'''

#Ques 8
'''for i in range(1,51):
    if(i%7==0):
        print(i)'''

#Ques 9
'''for i in range(1,11):
    square=i*i
    print("square=",square)'''

#Ques 10
'''for i in range(1,51):
    if(i%2!=0):
        print(i)'''

