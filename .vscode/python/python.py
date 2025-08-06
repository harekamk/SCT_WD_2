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

#area of rectangle using coordinates
'''x1=int(input("enter x1:"))
x2=int(input("enter x2:"))
y1=int(input("enter y1:"))
y2=int(input("enter y2:"))
print("area=",abs((x2-x1)*(y2-y1)))'''


# question
'''a=int(input("enter a:"))
b=int(input("enter b:"))
if(a==1 and b==1):
    print("CSE")
else:
    print("NOT CSE")
'''

#local and global variables

''' 
def myfunc():
    x="fantastic"
    print("python is " + x)
myfunc()'''

'''def myfunc():
    x="awesome",
    print("python is " + x)
myfunc()'''

#write a program to find out if a number is even or odd
'''def evenorodd():
    x=int(input("enter x:"))
    if(x%2==0):
        print("even")
    else:
        print("odd")
evenorodd()'''

#find average of two
'''def avg():
    num1=int(input("enter num1:"))
    num2=int(input("enter num2:"))
    avg=(num1+num2)/2
    print("average=",avg)
avg()'''

#maximum of 2 numbers from 3
'''def best():
    a=int(input("enter st1:"))
    b=int(input("enter st2:"))
    c=int(input("enter st3:"))
    if(a>b and a>c and b>c):
        print("a and b are greater", (a+b)/2)
    elif(b>a and b>c and c>a):
        print("b and c are greater", (b+c)/2)
    else:
        print("a and c are greater",(a+c)/2)
best()'''

#another alternative
'''def best():
    a=int(input("enter st1:"))
    b=int(input("enter st2:"))
    c=int(input("enter st3:"))
    if(a<b and a<c):
        print("b and c are greater",(b+c)/2)
    elif(b<a and b<c):
        print("a and c are greater",(a+c)/2)
    else:
        print("a and b are the greatest",(a+b)/2)
best()'''


#loops
'''first 10 numbers
i=1
while(i<11):
    print(i)
    i+=1'''

'''even numbers
givenrange=20
for i in range(givenrange):
    if i%2==0:
        print(i)'''

#sum of numbers
'''sum=0
i=1
while i<15:
    print(i)
    i+=1
    sum+=i
    print("sum=",sum)'''


#palindrome
'''string="madam"
rev_string="madam"
if string==rev_string:
    print("palindrome")
else:
    print("not a palindrome")'''

# reverse string
'''string=input("enter string:")
rev_string=""
for i in string:
    rev_string=i+rev_string
print(rev_string)'''

#alternative
'''string1="hello"
rev_string=reversed(string1)
for i in rev_string:
    print(rev_string)'''

# factorial
'''factorial=1
n=int(input("enter number:"))
for i in range(1,n+1):
    factorial=factorial*i
    print("factorial=",factorial)'''


# iteration
'''given_range=30
for i in given_range(1,given_range+1):
    if i%4==0 and i%5==0:
        print("fizzbuzz")
        continue
    if i%4==0 and i%5!=0:
        print("fizz")
        continue
    if i%4!=0 and i%5==0:
        print("buzz")
    else:
        print(i)'''


#convert month name to days
'''month=input("enter month:")
if(month=="January" or month=="March" or month=="may" or month=="july" or month=="august" or month=='october' or month=='december'):
    print("31 days")
elif(month=="february"):
    print("28 days")
elif(month=="april" or "june" or "september" or "november"):
    print("30 days")
else:
    print("invalid")'''

#first 10 numbers using loop
'''i=1
while(i<11):
    print(i)
    i+=1'''

#sum
'''given_range=20
sum=0
for i in range(1,given_range+1):
    sum+=1
    print("sum=",sum)'''

#multiplication table
'''n=int(input("enter table:"))
for i in range(1,11):
    print(n,"*",i,"=",n*i)'''

#cube of numbers
'''n=int(input("enter number:"))
for i in range(1,n+1):
    print("cube=",(i*i*i))'''

#validity of password
'''u,l,s,d=0,0,0,0
password=input("enter password:")
uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase="abcdefghijklmnopqrstuvwxyz"
digits="0123456789"
special_char="@#$%^&*"
if(len(password)>=8 and len(password)<=16):
    for i in password:
        if(i in lowercase):
            l+=1
        if(i in uppercase):
            u+=1
        if(i in digits):
            d+=1
        if(i in special_char):
            s+=1
    if(l>=1 and u>=1 and d>=1 and s>=1 and l+u+d+s==len(password)):
         print("valid password")
    else:
         print("invalid password")'''
    
#distance
'''x1=int(input("enter x1:"))
x2=int(input("enter x2:"))
y1=int(input("enter y1:"))
y2=int(input("enter y2:"))
distance=((x2-x1)**2+(y2-y1)**2)/0.5
print("distance=",distance)'''

#km to m
'''km=int(input("enter km:"))
m=km*1000
print("meter=",m)'''


#bitwise operators
#print bitwise AND operation
'''print("a & b=",a & b)'''
#print bitwise OR operation
'''print("a|b=",a|b)'''
#print bitwise NOT operation
'''print("~a=",~a)'''
#print bitwise XOR operation
'''print("a^b=",a^b)'''

#HCF
'''def gcd(a,b):
    if(a==0):
        return b
    if(b==0):
        return a
    if(a==b):
        return a
    if(a>b):
        return gcd(a-b,b)
    return gcd(a,b-a)

a=98
b=56
if(gcd(a,b)):
    print("GCD of",a,"and",b,"is",gcd(a,b))
else:
    print("not found")'''

'''s=0
for i in range(1,21,1):
    s+=i
    print(s)'''

#print current date and time 
'''import datetime
print(datetime.datetime.now())
print(datetime.datetime.now().time()'''

# x/y== answer in decimals
# x//y==answer in round off

#celsius to kelvin
'''temperature=input("enter temperature:")
print(temperature)
kelvin=int(temperature)+273
print("kelvin-",kelvin)'''

#swap
'''a=7
b=5
c=a
a=b
b=c
print("value of a=",a)
print("value of b=",b)'''

#add digits of no
'''n=int(input("enter number"))
a=n%10 #(345%10=5)
n=n//10 #(34)
b=n%10 #(4)
c=n//10 #(3)
sum=a+b+c
print(sum)'''

'''n=4567
a=n%10 #(7)
n=n//10 #456
b=n%10 #6
n=n//10 #45
c=n%10 #5
d=n//10  #4
sum=a+b+c+d
print(sum)'''


#reverse digits
'''n=12345
rev=n
a=n%10 #5
n=n//10 #1234

b=n%10 #4
n=n//10 #123

c=n%10 #3
n=n//10 #12

d=n%10 #2
e=n//10 #1

rev=10000*a+1000*b+100*c+10*d+e

print("original no=",n)
print("reversed=",rev)

if(n==rev):
    print(True)
else:
    print(False)'''

#leap year
'''year=int(input("enter year:"))
if(year%4==0 and year%400==0 and year%100!=0):
    print("leap year")
else:
    print("not a leap year")'''

#euclidean distance
'''x1=int(input("enter x1:"))
x2=int(input("enter x2:"))
y1=int(input("enter y1:"))
y2=int(input("enter y2:"))
distance=((x2-x1)**2+(y2-y1)**2)/0.5
print(distance)'''

#to check if a triangle exists
'''a=input("enter angle:")
b=input("enter angle:")
c=input("enter angle:")
if(a+b+c==180 and a!=0 and b!=0 and c!=0):
    print("possible")
else:
    print("impossible")'''

#profit or loss
'''costprice=input("enter cost price:")
sellingprice=input("enter selling price:")
profit=sellingprice-costprice
loss=costprice-sellingprice
if(sellingprice>costprice):
    print("profit=")
else:
    print("loss=")'''

#weather
'''temperature=input("enter temperature:")
humidity=input("enter humidity percentage:")
if temperature>=30 and humidity>=90:
    print("hot and humid")
elif temperature>=30 and humidity<90:
    print("hot")
elif temperature<30 and humidity>=90:
    print("cold and humid")
else:
    print("cold")'''

#armstrong no
#if sum of the digits raised to the power number of digits is equal to the number itself, it is an armstrong number


#sum of squares of digits
'''n=int(input("enter number:"))
#n=1928
a=n%10 #8
n=n//10 #192
b=n%10 #2
n=n//10 #19
c=n%10 #9
d=n//10 #1
sum=(a**2)+(b**2)+(c**2)+(d**2)
print(sum)'''

#inhand salary
'''salary=input("enter salary:")
if salary>=500000 and salary<=1000000:
    tax=(10/100)*salary
    new_salary=salary-tax
elif salary>=1000000 and salary<=2000000:
    tax=(20/100)*salary
    new_salary=salary-tax
else:
    tax=(30/100)*salary
    new_salary=salary-tax
print("after tax reduction=",new_salary)

hra=(10/100)*new_salary
da=(5/100)*new_salary
pf=(3/100)*new_salary

in_handsalary=(new_salary-hra-da-pf)/12
print("in hand salary=",in_handsalary)

if in_handsalary<=999:
    print(in_handsalary)
elif in_handsalary>=1000 and in_handsalary<=9999:
    print(in_handsalary/1000,"k")
elif in_handsalary>=100000 and in_handsalary<=9999999:
    print(in_handsalary/100000,"l")
else:
    print(in_handsalary/10000000,"cr")'''

#possible combinations
'''for i in range(1,5):
    for j in range(1,5):
        if(i!=j):
            print(i,j)'''

#prime numbers
'''counter=0
num=2   #smallest prime
while(counter<=25):
    for i in range(2,num):
        if num%i==0:
            break
    else:
        print(num)
        counter+=1
    num+=1'''


#sum of n numbers
'''n=int(input("enter number:"))
sum=n*(n+1)/2
print(sum)'''

#multiply without *
'''print(5*5)
sum=5+5+5+5+5
print(sum)'''

#first 25 odd numbers
'''i=1
for i in range(1,26):
    if i%2!=0:
        print(i)
        i+=1
    if i==25:
     break'''

#fibonacci series
#third no of the series should be the sum of the first two no
'''count=0
a=0
b=1
print(a)
print(b)
while True:
    c=a+b
    a=b
    b=c
    print(c)
    count+=1
    if count==18:
        break'''


'''def fib():
    count=0
    a=0
    b=1
    print(a)
    print(b)
    while True:
        c=a+b
        a=b
        b=c
        print(c)
        count+=1
        if count==20:
            break
print(fib())'''

#factorial using functions
'''def fact():
    n=int(input("enter n:"))
    factorial=1
    for i in range(1,n+1):
        factorial=factorial*i
        print("fact=",factorial)
fact()'''

'''factorial=1
n=int(input("enter number:"))
for i in range(1,n+1):
    factorial=factorial*i
    print(f"The factorial of {i} is {factorial}")'''

#no divisible by 3 and 5
'''for i in range(0,50):
    if i%3==0 and i%5==0:
        print(i)'''


#sum of even from 1 to 100
'''sum=0
for i in range(1,101):
    if i%2==0:
        sum+=i
    print(f"sum of even no from 1 to 100={sum}")'''

#sum of 1-100
'''sum=0
for i in range(1,101):
    sum+=i
    print(f"sum of no={sum}")'''

#bitwise
'''a=10
b=4
print("a & b=",a&b)
print("a | b=",a|b)
print("~a=",~a)
print("a^b=",a^b)'''

#break and continue
'''i=1
while i<6:
    print(i)
    if i==3:
        break
    i+=1'''

'''i=1
while i<6:
    i+=1
    if i==3:
        continue
    print(i)'''

#sum using while loop
'''sum=0
i=1
while i<=15:
    print(i)
    sum+=i
    i+=1
print(f"sum={sum}")'''

#table using for and range
'''num=17
for i in range(1,11):
    print(num,"x",i,"=",num*i)'''

#continue using for loop
'''for i in range(1,11):
    if i==5:
        i+=1
        continue
    print(i)'''

#LCM
'''import math
a=int(input("enter num1:"))
b=int(input("enter num2:"))
def g(a,b):
    g=math.gcd(a,b)
    return g
result=g(a,b)
print(f"the lcm of {a} and {b} is {result}")'''

#LCM
'''import math
a=int(input("enter num1:"))
b=int(input("enter num2:"))
def l(a,b):
    g=math.gcd(a,b)
    l=(a*b)//g
    return l
result=l(a,b)
print(f"the lcm of {a} and {b} is {result}")'''

#HCF/GCD
'''def gcd():
    a=int(input("enter num1:"))
    b=int(input("enter num2:"))
    print(f"a={a}")
    print("b=",b)
    while b!=0:
        a,b=b,a%b
        c=a
        print(f"The HCF= {c}")
gcd()'''

#sum of odd
'''sum=0
for i in range(1,16,2):
    print(i)
    sum+=i
    print("sum=",sum)'''

#Pizza hut
'''size=input("enter size:")
Small=8
Medium=10
Large=15
toppings=int(input("enter number of toppings:"))
toppings_cost=2
if size=="Small":
    print("Pizza costs $",Small+toppings*toppings_cost)
elif size=="Medium":
    print("Pizza costs $",Medium+toppings*toppings_cost)
else:
    print("Pizza costs $",Large+toppings*toppings_cost)

print("Thanks for ordering")'''


'''def calculate_pizza_cost(size,toppings):
    base_price={"Small":10,"Medium":15,"Large":20}
    topping_cost=2
    total_cost=base_price[size]+toppings*topping_cost
    return total_cost

size=input("enter size:")
toppings=int(input("enter number of toppings:"))
total_cost=calculate_pizza_cost(size,toppings)
print(size)
print(toppings)
print(f"${total_cost}")
print("Thank you for ordering")
calculate_pizza_cost()'''
  

#palindrome of an integer number
'''n=int(input("enter number:"))
rev=0
x=n
while (n>0):
    rev=(rev*10)+n%10
    n=n//10
if n==rev:
    print("palindrome")
else:
    print("not a palindrome")'''

#swap first and last element
'''list1=[1,2,3,4,5,6]
list1[0],list1[-1]=list1[-1],list1[0]
print(list1)'''

#check whether a number is prime or not
'''n=int(input("enter number:"))
for i in range(2,n):
    if n%i==0:
        print("not prime")
        break
    else:
        print("prime")
        break'''


#electricity bill
'''units=int(input("enter units consumed:"))
if units<=100:
    print("The total bill:Rs 0")
elif units>100 and units<200:
    print("The total bill:Rs",100*0+(n-100)*1.5)
elif units<200 and units<300:
    print("The total bill:Rs",100*0+100*1.5+(n-200)*4)
else:
    print("The total bill:Rs",100*0+100*1.5+100*4+(n-300)*6)'''

#gcd

'''def GCD(a,b):
    if b==0:
        return a
    else:
        return GCD(b,a%b)
num1=int(input("enter num1:"))
num2=int(input("enter num2:"))
print(GCD(num1,num2))'''

#zodiac sign
'''def zodiac_sign(month,day):
  month=int(input("enter month:"))
  day=int(input("enter day:"))
  if (month==3 and day>=21) or (month==4 and day<=19):
    return "Aries"
  elif(month==4 and day>=20) or (month==5 and day<=20):
        return "Taurus"
  elif(month==5 and day>=21) or (month==6 and day<=20):
        return "Gemini"
  elif (month==6 and day>=21) or (month==7 and day<=22):
        return "Cancer"
  elif (month==7 and day>=23) or (month==8 and day<=22):
        return "Leo"
  elif (month==8 and day>=23) or (month==9 and day<=22):
        return "Virgo"
  elif (month==9 and day>=23) or (month==10 and day<=22):
        return "Libra"
  elif(month==10 and day>=23) or (month==11 and day<=21):
        return "Scorpio"
  elif (month==11 and day>=22) or (month==12 and day<=21):
        return "Sagittarius"
  elif (month==12 and day>=22) or (month==1 and day<=19):
        return "Capricorn"
  elif (month==1 and day>=20) or (month==2 and day <=18):
        return "Aquarius"
  elif (month==2 and day>=19) or (month==3 and day<=20):
        return "Pisces"
  else:
        return "date not found"
print(zodiac_sign())'''

#square root
'''num1=int(input("enter number:"))
sr=num1**0.5
print("Square root=",sr)'''

#find ascii value
'''char="a"
print("The ascii value of",char,"is",ord(char))

char="A"
print("The ascii value of",char,"is",ord(char))'''

#shuffle a deck of cards
#symmetric
'''import random, itertools
deck=list(itertools.product(range(1,14),["Spade","Club","Hearts","Diamond"]))
print(deck)'''
#shuffled
'''import random,itertools
deck=list(itertools.product(range(1,14),["Spade","Club","Diamond","Hearts"]))
random.shuffle(deck)
print(deck)'''

'''import random,itertools
deck=list(itertools.product(range(1,14),["Spade","Club","Hearts","Diamond"]))
for i in range(5):
    print(deck[i][0],"of",deck[i][1])'''

'''import random,itertools
deck=list(itertools.product(range(1,14),["Spade","Club","Diamond","Hearts"]))
random.shuffle(deck)
for i in range(10):
    print(deck[i][0],"of",deck[i][1])'''

#calendar
'''import calendar
year=int(input("enter year:"))
month=int(input("enter month:"))
calendar=calendar.month(year,month)
print(calendar)'''

#check whether palindrome
'''a=input("enter string:")
rev=a[::-1]
if a==rev:
    print("It is a palindrome")
else:
    print("not a palindrome")'''

#HCF
'''a=int(input("enter num1:"))
b=int(input("enter num2:"))
while a%b!=0:
    remainder=a%b
    a=b
    b=remainder
    print("HCF=",b)'''


#LCM
'''a=int(input("enter num1:"))
b=int(input("enter num2:"))
while a%b!=0:
    remainder=a%b
    a=b
    b=remainder
    HCF=b
    LCM=(a*b)/HCF
    print(LCM)'''


#doubts
#prime,, armstrong, sum of square,sum using loop,sum of digits,volume of cylinder and cost per l,salary,sum of odd

#compound interest
'''p=int(input("enter principal:"))
r=int(input("enter rate:"))
t=int(input("enter time:"))
n=int(input("enter n:"))
amount=p*(1+int(r/n))**n*t
CI=amount+p
print("Amount=",amount)
print("Compound Interest=",CI)'''

#count number of digits
'''a=0
n=int(input("enter number:"))
while n!=0:
    b=n%10
    n=n//10
    a+=1

print("no of digits",a)'''

#sum of digits
'''a=0
n=int(input("enter number:"))
while n!=0:
    b=n%10
    n=n//10
    a=a+b
    print(f"sum={a}")'''



#palindrome
'''string=input("enter string:")
rev=string[::-1]
if string==rev:
    print("palindrome")
else:
    print("not a palindrome")'''

#prime
'''count=0
n=int(input("enter n:"))
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count==2:
    print("prime")
else:
    print("not prime")'''

'''for i in range(1,11):
    if i%2!=0:
        pass
    else:
        print(i)
        i+=1'''

#bank
'''p=int(input("enter principal amount:"))
t=input("enter account type:")
def savings_account(t):
    return p*0.04
def fixed_account(t):
    return p*0.06
def calculate_interest(t):

 if t=="Fixed account":
  print(fixed_account())
 elif t=="Savings account":
   print(savings_account())
 else:
   print("invalid")'''

#Organization
'''def calculate_gross_salary():
    current_gross_salary=int(input("enter salary:"))
    gender=input("enter gender:")
    if gender=="male":
        print("final gross salary:",current_gross_salary+(current_gross_salary)*(10/100))
    elif gender=="female":
        print("final gross salary:",current_gross_salary+(current_gross_salary)*(15/100))
    else:
        print("invalid")
calculate_gross_salary()'''

#reverse
'''n=input("enter number:")
rev=n[::-1]
print(rev)'''

#numbers not divisible by 2 and 3
'''for i in range(1,51):
    if (i%2!=0 and i%3!=0):
        print(i)'''

#divide
'''n=int(input("divisor:"))
ll=int(input("lower limit"))
ul=int(input("upper limit:"))
for i in range(ll,ul+1):
    if (i%n==0):
        print(i)'''

#smallest divisor
'''n=int(input("Enter an integer:"))
a=[]
for i in range(2,n+1):
    if(n%i==0):
        a.append(i)
a.sort()
print("Smallest divisor is:",a[0])'''

#convert cm into inches and feet
'''cm=int(input("enter length in cm:"))
inches=0.394*cm
feet=0.328*cm
print("Length in inches=",round(inches,2))
print("Length in feet=",round(feet,2))'''

#perfect number
'''n=int(input("enter number:"))
sum=0
for i in range(1,n):
    if(n%i==0):
        sum=sum+i
if n==sum:
    print("perfect number")
else:
    print("not a perfect number")'''

#prime factors

#amicable numbers
'''num1=int(input("enter num1:"))
num2=int(input("enter num2:"))
sum1=0
sum2=0
for i in range(1,num1):
    if num1%i==0:
        sum1+=i
for j in range(1,num2):
    if num2%j==0:
        sum2+=j
if(sum1==num2 and sum2==num1):
    print("Amicable numbers")
else:
    print("Not amicable")'''

#possible combination of 3 numbers
'''for i in range(1,5):
 for j in range(1,5):
  for k in range(1,5):
    if (i!=j and i!=k and j!=k):
     print(i,j,k)'''

#denomination of notes
'''amt=int(input("enter amount:"))
hundred=amt//100
amt=amt%100
fifty=amt//50
amt=amt%50
ten=amt//10
print("No. of hundred notes:",hundred)
print("No. of fifty notes:",fifty)
print("No. of ten notes:",ten)'''

#salary
'''current_gross_salary=int(input())
gender=input()
if gender=="male":
    increment=(current_gross_salary*10)/100
    current_gross_salary+=increment
    print(current_gross_salary)
elif gender=="female":
    increment=(current_gross_salary*15)/100
    current_gross_salary+=increment
    print(current_gross_salary)
else:
    print("wrong")'''

#marks
'''a=int(input("enter marks:"))
b=int(input("enter marks:"))
c=int(input("enter marks:"))
d=int(input("enter marks:"))
total=a+b+c+d
avg=total/4
print(total)
print(avg)
if avg>=75:
    print("Distinction")
elif avg>=60 and avg<75:
    print("First division")
elif avg>=50 and avg<60:
    print("Second division")
elif avg>=40 and avg<50:
    print("Third division")
else:
    print("fail")'''

#efficiency of worker
'''time=float(input("enter time duration:"))
if time>0 and time<=3:
    print("Worker is highly efficient")
elif time>3 and time<4:
    print("improve speed")
elif time>=4 and time<5:
    print("Given training")
else:
    print("Worker must leave")'''

#employee bonus
'''current_year=int(input("enter current year:"))
join_year=int(input("enter join year:"))
diff=current_year-join_year
if diff>=3:
    print("bonus is Rs 2500")
else:
    print("no bonus")'''

#rectangle
'''length=int(input("enter length:"))
breadth=int(input("enter breadth:"))
area=length*breadth
perimeter=2*(length+breadth)
print(area)
print(perimeter)
if area>perimeter:
    print("purchases the land")
else:
    print("rejects")'''

#library
'''days=int(input("enter days:"))
if days>=1 and days<=5:
    print("fine=",0.50*days)
elif days>=6 and days<=10:
    print("fine=",1*days)
elif days>10 and days<=30:
    print("fine=",2*days)
else:
    print("membership is cancelled")'''

#locker password
'''pwd=input("enter password:")
rev=pwd[::-1]
if pwd==rev:
    print("correct")
else:
    print("incorrect")'''

#armstrong
'''n=int(input("enter:"))
sum=0
x=n
b=len(str(n))
while x>0:
    a=x%10
    sum+=a**b
    x=x//10
if sum==n:
    print("yes")
else:
    print("no")'''

'''original_str="like"
new_str=""
for i in range(len(original_str)):
    new_str+=chr(ord(original_str[i])+3)
print(new_str)
n=int(input())
m=int(input())
badi_array=[]
for i in range(n):
    choti_array=[]
    for j in range(m):
        a=int(input())
        choti_array.append(a)
        badi_array.append(choti_array)
sum=0
for i in range(n):
    for j in range(m):
        print(badi_array[i][j],end=' ')
    print()
for i in range(n):
    for j in range(m):
        if (i==0 or i==n-1 or j==0 or j==m-1):
            sum+=badi_array[i][j]
print(sum)'''

#check whether prime or not only if no is positive
'''def prime(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                break
            else:
                print(n,"is a prime number")
                break
num=int(input())
if num>0:
    prime(num)
else:
    print("enter a positive number")'''

#number series
'''n=int(input())
odd=0
even=0
for i in range(1,n+1):
    if n%i==0:
        even+=6
    else:
        odd+=7
print("{} term of series is {}".format(n,even-6))
print("{} term of series is {}".format(n,odd-7))'''

#sparse matrix
'''a=[[0,1,2],
   [4,7,8],
   [7,5,3]]
count=0
rows=len(a)
cols=len(a[0])
size=rows*cols
for i in range(0,rows):
    for j in range(0,cols):
        if a[i][j]==0:
            count+=1
if count>(size/2):
    print("sparse matrix")
else:
    print("not a sparse matrix")'''

#hcf or gcd
'''def compute(x,y):
    if x>y:
        smaller=y
    else:
        smaller=x
    for i in range(1,smaller+1):
        if x%i==0 and y%i==0:
            hcf=i
    return hcf
x=int(input())
y=int(input())
print(compute(x,y))'''

#sum of digits
'''total=0
n=int(input())
while (n>0):
    digit=n%10
    total+=digit
    n=n//10
print(total)'''

#count the digits
'''count=0
n=int(input())
while (n>0):
    count+=1
    n=n//10
print(count)'''

#smallest divisor
n=int(input())
a=[]
for i in range(1,n+1):
    if n%i==0:
        a.append(i)
a.sort()
print(a[0])