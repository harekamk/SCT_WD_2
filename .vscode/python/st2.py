#wap to find the avg of all the plants with diff height in your garden. remember ht of all the plants will be entered as space separated input.
#formula used=sum of ht/total no of ht

'''height=input().split()
sum=0
for i in height:
    sum+=int(i)
average=sum//len(height)
print(average)'''


'''type=input("enter type:")
enter_time=float(input("Enter entry time HH:MM:"))
leave_time=float(input("Enter leaving time HH:MM:"))
diff=float(leave_time)-float(enter_time)
print(diff)
if (diff<3) and type=='t' or 'b':
    print("20Rs")
elif (diff>3) and type=='t' or 'b':
    print("30Rs")
elif diff<=3 and type=="c":
    print("10Rs")
elif diff>3 and type=='c':
    print("20Rs")
elif diff<=3 and type=="cy" or 's':
    print("5Rs")
elif diff>3 and type=='cy' or 's':
    print("10Rs")
else:
    print("invalid")'''

#manage employees' database. the salary is credited in the form of rupees and convert to dollars. 
'''n=int(input())
inr={}
for i in range(n):
    name=input()
    sal=input()
    inr[name]=sal
for key in inr:
    value=inr[key]
    inr[key]=round(value/84, 2)
print(inr)'''


#reverse a string in the form of a tuple
'''string1=input()
rev=string1[::-1]
print(tuple(rev))'''

#increment alphabets
'''n=input()
x=chr(ord(n)+3)
print(x)'''

#increment alphabets in a string
'''def inc(string1):
    result=""
    for char in string1:
        if char.isalpha():
            result+=chr(ord(char)+2)
        else:
            result+=char
    return result
string1=input()
print(inc(string1))'''

'''string1=input()
result=''
for i in string1:
    if i.isalpha():
        print(chr(ord(i)+2),end='')
    else:
        print(i)'''
        

#random no
'''import random
print(random.randint(0,9))'''


#check if prime
'''num=int(input())
if num==0 or num==1:
    print("not prime")
elif num>1:
    for i in range(2,num):
        if num%i==0:
            print("not prime")
            break
        else:
            print("prime")
            break
else:
    print("not prime")'''

#prime no in range
# ll=int(input())
# ul=int(input())
# for num in range(ll,ul+1):
#     if num>1:
#         for j in range(1,num):
#             if num%j==0:
#                 break
#         else:
#             print(num)

#factorial of a number
'''def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return (n*fact(n-1))
n=int(input())
print(fact(n))'''


#sum of natural no
'''n=int(input())
sum=0
for i in range(1,n+1):
    sum+=i
    n-=1
print(sum)'''

#display powers of 2
'''n=int(input())
for i in range(0,n):
    result=list(map(lambda x:2**x, range(n)))
print(result[i])'''

#reversing numbers
'''n=input()
rev=n[::-1]
print(rev)'''

#remove duplicates from a dict
'''n=int(input())
dict1={}
for i in range(n):
    key=input()
    value=input()
    dict1[key]=value
print(dict1)
temp=[]
res=dict()
for key, val in dict1.items():
    if val not in temp:
        temp.append(val)
        res[key]=val
print(str(res))'''

#frequency of each alphabet
'''string1=input()
dict1={}
for word in string1:
    if word in dict1:
        dict1[word]+=1
    else:
        dict1[word]=1
print(dict1)'''

#word freq
'''string1=input()
dict1={}
words=string1.split()
for word in words:
    if word in dict1:
        dict1[word]+=1
    else:
        dict1[word]=1
print(dict1)'''


'''def filter_temp(readings,threshold):
    return [temp*9/5+32 for temp in readings if temp>threshold]
readings=[]
n=int(input())
for i in range(n):
    a=int(input())
    readings.append(a)
threshold=int(input())
result=filter_temp(readings,threshold)
print(result)'''


'''def process_expenses(expenses):
    filtered=list(filter(lambda x:x<0, expenses))
    adjusted=list(map(lambda x:x*0.9, filtered))
    net= reduce(lambda acc,x:acc+x, adjusted+list(filter(lambda x:x>=0, expenses)))
    return net
n=int(input())
expenses=[]
for i in range(n):
    a=int(input().split())
    expenses.append(a)
print(process_expenses(expenses))'''


'''from functools import reduce
def multiply(tup):
    return reduce(lambda x,y:x*y, tup)
n=int(input())
li=[]
for i in range(n):
    a=[int(num) for num in li().split()]
    li.append(a)
tup=tuple(li)
result=multiply(tup)
print(result)'''

'''n=int(input())
print("Enter tuple values:")
tup=tuple(int(input())for _ in range(n))
list1=list(set(tup))
print(tup)
print(list1)'''

'''string1=input()
rev=string1[::-1]
tup1=tuple(rev)
print(tup1)'''

'''n=int(input("enter n:"))
dict1={}
for i in range(n):
    books=input("enter book:")
    count=input("enter count:")

    if books not in dict1:
        dict1[books]=count

for books,count in dict1.items():
    print(f"{books}:{count}")
print(dict1)'''

'''n=int(input("Enter no of employees:"))
d={}
for i in range(n):
    name=input()
    salary=float(input())
    d[name]=salary
print(d)
for key in d:
    value=d[key]
    d[key]=round(value/84,2)
print(d)'''

'''string1=input()
string2=input()
l1=list(string1)
l2=list(string2)
l1.sort()
l2.sort()
print(l1)
print(l2)
if l1==l2:
    print("True")
else:
    print("False")'''

'''def filter_temp(readings,threshold):
    return [(temp*(9/5)+32) for temp in readings if temp>threshold]

n=int(input("total:"))
readings=[]
for i in range(n):
    v=float(input("Enter readings:"))
    readings.append(v)
threshold=int(input("Enter threshold:"))
result=filter_temp(readings,threshold)
print(result)'''

'''from functools import reduce
def process_expenses(expenses):

    filtered_expenses=filter(lambda x:x<=0, expenses)
    print(filtered_expenses)
    adjusted_expenses=map(lambda x:x*0.9 if x<0 else x, filtered_expenses)
    print(adjusted_expenses)
    total_balance=reduce(lambda acc,x:acc+x, adjusted_expenses)
    return total_balance

n=int(input("Enter total:"))
expenses=[]
for i in range(n):
    v=float(input("Enter:"))
    expenses.append(v)

total=process_expenses(expenses)
print(total)'''

'''from functools import reduce
def process_expenses(expenses):
    filtered=list(filter(lambda x:x<0, expenses))
    print(filtered)
    adjusted=list(map(lambda x:x*0.9, filtered))
    print(adjusted)
    total=reduce(lambda x,acc:x+acc, adjusted,0)
    print(total)
expenses=list(map(float, input("value:").split()))
process_expenses(expenses)'''

'''from functools import reduce
list1=[]
n=int(input("total:"))
for i in range(n):
    v=int(input("enter:"))
    list1.append(v)
print(list1)
result=reduce(lambda x,y:x*y,list1)
print(result)
tup1=tuple(list1)
print(tup1)'''

'''list1=[]
n=int(input("total:"))
for i in range(n):
    v=int(input("enter:"))
    list1.append(v)
tup1=tuple(list1)
print("original tuple:",tup1)
set1=set(tup1)
list2=list(set1)
print("updated list:",list2)'''

'''l=[]
n=int(input("enter:"))
for i in range(n):
    v=int(input("enter:"))
    l.append(v)
l.reverse()
print(l)'''

'''string1=input()
rev=string1[::-1]
tup1=tuple(rev)
print(tup1)'''

'''string1=input()
start=int(input("enter start index:"))
end=int(input("enter end index:"))
substring=string1[start:end]
print(substring)'''

'''r=int(input())
c=int(input())
m=[]
for i in range(r):
    l=[]
    for j in range(c):
        v=int(input("enter:"))
        l.append(v)
    m.append(l)
print(m)

def sum_border():
    r=len(m)
    c=len(m[0])
    border_sum=0
    border_sum+=m[0]
    if r>1:
        border_sum+=m[-1]
    for i in range(1,r-1):
        border_sum=m[i][0]
        if c>1:
            border_sum+=m[i][-1]
    return border_sum
border_sum=sum_border()
print(border_sum)'''

#multiply tuple values
'''l=[]
product=1
n=int(input())
for i in range(n):
    m=int(input())
    l.append(m)
tuple1=tuple(l)
for i in tuple1:
    product=product*i
print(product)'''

#sum of tuple values
'''l=[]
sum=0
n=int(input())
for i in range(n):
    v=int(input())
    l.append(v)
tuple1=tuple(l)
for i in tuple1:
    sum+=i
print(sum)'''


'''r=int(input())
c=int(input())
m=[]
for i in range(r):
    l=[]
    for j in range(c):
        v=int(input("enter:"))
        l.append(v)
    m.append(l)
print(m)
def total_sum():
    total_list=[]
    for student_scores in m:
        total=sum(student_scores)
        total_list.append(total)
    return total_list 
total_list=total_sum()
print(total_list)'''

'''def max_product(n):
    #edge cases
    if n==1:
        return 1    #cant be split
    elif n==2:
        return 1   #the product would still be 1
    
    #main logic
    product=1
    while n>=4:
        product*=3
        n-=3

    if n==2:
        product*=2
    return product
n=int(input())
product=max_product(n)
print(product)'''



'''n=int(input("enter:"))
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
print(rev)'''

'''n=int(input("enter:"))
dict1={}
for i in range(n):
    book=input("enter book name:")
    volume=input("enter count:")
    dict1[book]=volume
print(dict1)'''

'''n=int(input("enter:"))
dictrup={}
for i in range(n):
    name=input("name:")
    salary_rupees=float(input("salary in rupees:"))
    dictrup[name]=salary_rupees
print(dictrup)
dictdoll={}
for name,salary_rupees in dictrup.items():
    dictdoll[name]=round(salary_rupees/84,2)
print(dictdoll)'''

'''def filter_temp(readings,threshold):
    return [(x*(9/5)+32) for x in readings if x>threshold]

n=int(input("total:"))
readings=[]
for i in range(n):
    v=float(input("enter readings:"))
    readings.append(v)
print(readings)
threshold=int(input("Enter threshold:"))
print(filter_temp(readings,threshold))'''

'''from functools import reduce
def process_expenses(expenses):
    filtered=list(filter(lambda x: x>=0,expenses))
    print(filtered)
    adjusted=list(map(lambda x:x*0.9, filtered))
    print(adjusted)
    net=reduce(lambda x,y:x+y, adjusted, 0)
    print(net)
n=int(input("enter:"))
expenses=[]
for i in range(n):
    v=float(input("enter value:"))
    expenses.append(v)
print(process_expenses(expenses))'''

'''from functools import reduce
n=int(input("enter:"))
list1=[]
for i in range(n):
    value=int(input("enter value:"))
    list1.append(value)
    product=reduce(lambda x,y:x*y, list1)
result_tuple=(product)
print(result_tuple)'''

'''n=int(input("total:"))
list1=[]
for i in range(n):
    v=int(input("enter:"))
    list1.append(v)
    list1.sort()
print(list1)
print(list1[-1])'''

'''input_str=input("enter:")
result=' '
count=1
for i in range(1,len(input_str)):
    if input_str[i]==input_str[i-1]:
        count+=1
    else:
        result+=input_str[i-1]+str(count)
        count=1

result+=input_str[-1]+str(count)
print(result)'''

'''string1=input()
result=''
for char in string1:
    if char.isalpha():
        if char=='z':
            result+='a'
        elif char=='Z':
            result+="A"
        else:
            result+=chr(ord(char)+2)
    else:
        result+=char
print(result)'''

'''string1=input()
freq={}
for char in string1:
    if char.isalpha():
        char=char.lower()
        if char in freq:
            freq[char]+=1
        else:
            freq[char]=1
print(freq)'''

'''string1=input()
result=''
for char in string1:
    if char.isalpha():
        if char=='z':
            result+='a'
        elif char=="Z":
            result+="A"
        else:
            result+=chr(ord(char)+2)
    else:
        result+=char
print(result)'''

#print even numbers
'''def even():
    n=int(input())
    for _ in range(n):
        number=int(input())
        if number%2==0:
            print(number)
even()'''

#print even numbers and its sum
'''n=int(input())
sum=0
for _ in range(n):
    number=int(input())
    if number%2==0:
        print(number)
        sum+=number
print("sum:",sum)'''

#print odd no
'''n=int(input())
for _ in range(n):
    number=int(input())
    if number%2!=0:
        print(number)'''

#print odd no and sum
'''n=int(input())
sum=0
for _ in range(n):
    number=int(input())
    if number%2!=0:
        print(number)
        sum+=number
print(sum)'''

#remove duplicate from list
'''def remove(original):
    new=[]
    for item in original:
        if item not in new:
            new.append(item)
    return new
n=int(input())
original=[]
for _ in range(n):
    v=int(input("value:"))
    original.append(v)
    
newlist=remove(original)
print(newlist)'''

#avg of even no
'''avg=0
count=0
n=int(input())
for _ in range(n):
    N=int(input())
    if N%2==0:
        count+=N
        avg+=1
if avg==0:
    print(0)
else:
    print(count//avg)'''

#fact of a no
'''def factorial(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return n*factorial(n-1)
n=int(input())
fact=factorial(n)
print(fact)'''

#print palindrome from 11 to n
'''def pal(n):
    for i in range(11,n+1):
        s=str(i)
        rev=s[::-1]
        if s==rev:
            print(s)
n=int(input())
p=pal(n)
print(p)'''


#print even and odd count
'''def eo(n):
    odd=0
    even=0
    for i in range(n):
        N=int(input())
        if N%2==0:
            even+=1
        else:
            odd+=1
    return even,odd
n=int(input())
evencount, oddcount=eo(n)
print("even:",evencount)
print("odd:",oddcount)'''

#print no of digits and sum
'''sum=0
count=0
n=int(input())
while n!=0:
    digit=n%10
    sum+=digit
    count+=1
    n=n//10
print("digits count:",count)
print("sum:",sum)'''


#print no in alphabetic form'
'''n=int(input())
s=str(n)
for i in s:
    match int(i):    #convert the no back to integer and match it
        case 0:
            print("Zero")
        case 1:
            print("One")
        case 2:
            print("Two")
        case 3:
            print("Three")
        case 4:
            print("Four")
        case 5:
            print("Five")
        case 6:
            print("Six")
        case 7:
            print("Seven")                
        case 8:
            print("Eight")
        case 9:
            print("Nine")'''

#square and cube
'''n=int(input())
square=n*n
print(square)
cube=n*n*n
print(cube)'''

#fibonacci no
'''n=int(input())
def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
fibs=fib(n)
print(fibs)'''
                                                                                                                                                                              
#check prime
'''n=int(input())
if n==1:
    print("False")
for i in range(2,n):
    if n%i==0:
        print("False")
        break
    else:
        print("True")
        break'''

#prime no from 1 to n
'''def prime(n):
    if n<1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
n=int(input())
for i in range(1,n+1):
    if prime(i):
        print(i)'''

# prime from n to m
'''def prime(n):
    if n<1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
start=int(input())
end=int(input())
for i in range(start,end+1):
    if prime(i):
        print(i)'''

#max no in input
'''n=int(input())
list1=[]
max=0
for i in range(n):
    N=int(input())
    list1.append(N)
for i in list1:
    if i>=max:
        max=i
print(max)'''

#fibonacci series
'''def fib(n):
    a,b=0,1
    for _ in range(n):
        print(a)
        a,b=b,a+b
n=int(input())
fib(n)'''

#count unique values in a list
'''n=int(input())
l=[]
li=[]
for _ in range(n):
    N=int(input())
    l.append(N)
for i in l:
    if i not in li:
        li.append(i)
print(len(li))'''

'''n=int(input())
l=[]
for _ in range(n):
    N=int(input())
    l.append(N)
li=set(l)
print(len(li))'''

#denomination of 10,50,100
'''n=int(input())
hundred=n//100
n=n%100
fifty=n//50
n=n%50
ten=n//10
n=n%10
print("hundred:",hundred)
print("fifty:",fifty)
print("ten:",ten)'''

#leap year
'''n=int(input())
if n%4==0 and n%100!=0 or n%400==0:
    print("leap year")
else:
    print("not a leap year")'''

#book discount
'''books=int(input())
price=float(input())
if books>=1 and books<=2:
    discount=0.05
elif books>=3 and books<=5:
    discount=0.10
else:
    discount=0.15
final=price-(price*discount)
print(f"Final price after discount:{final:.2f}")'''

#find pair with maximum sum in a list
'''n=int(input())
list1=[]
for _ in range(n):
    N=int(input())
    list1.append(N)
    list1.sort()
print(list1[-2])
print(list1[-1])'''

#find max diff in a list(last-first)
'''n=int(input())
l=[]
for _ in range(n):
    M=int(input())
    l.append(M)
print(l[-1]-l[0])'''

#count vowels and consonants in a list
'''n=int(input())
l=[]
vowels='aeiouAEIOU'
consonants='bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
vowelcount=0
conscount=0
for _ in range(n):
    N=input()
    for char in N:
        if char in vowels:
            vowelcount+=1
        elif char in consonants:
            conscount+=1
print("vowel:",vowelcount)
print("consonants:",conscount)'''

'''n=int(input())
l=[]
vowelcount=0
conscount=0
for _ in range(n):
    m=input()
    l.append(m)
for i in l:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        vowelcount+=1
    else:
        conscount+=1
print(vowelcount)
print(conscount)'''

#sublist extract
'''n=int(input())
l=[]
for _ in range(n):
    N=int(input())
    l.append(N)
start=int(input())
end=int(input())
print(l[start:end+1])'''

#sum of even fib no
'''n=int(input())
a,b=0,1
evensum=0
while a<=n:
    if a%2==0:
        evensum+=a
    a,b=b,a+b
print(evensum)'''


#right angle star
'''n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*", end=' ')
    print()'''

#electricity bill
'''units=int(input())
if units<=100:
    print(0.0*units)
elif units>=101 and units<=200:
    print(100*0.0+(units-100)*2.5)
elif units>=201 and units<=300:
    print(100*0.0+100*2.5+(units-200)*4)
else:
    print(100*0.0+100*2.5+100*4+(n-300)*6)'''

#taxi billing
'''distance=float(input())
if distance<=10:
    cost=11*distance
elif distance>=11 and distance<=100:
    cost=10*11+(distance-10)*10
else:
    cost=10*11+90*10+(distance-100)*9
print(cost)'''

#employee salary
'''salary=float(input())
gender=input()
if gender=="m":
    increment=(salary*10)/100
    salary=salary+increment
    print(salary)
elif gender=="f":
    increment=(salary*15)/100
    salary+=increment
    print(salary)
else:
    print("invalid")'''

#avg and highest marks
'''n=int(input())
l=[]
sum=0
count=0
for _ in range(n):
    N=int(input())
    l.append(N)
    sum+=N
    count+=1
l.sort()
avg=sum//count
print(avg)
print(l[-1])'''

'''n=int(input())
l=[]
sum=0
count=0
number=map(int, input().split())
for num in number:
    sum+=num
    count+=1
    l.append(num)
l.sort()
avg=sum//count
print(avg)
print(l[-1])'''


#reverse words without changing order
'''sentence=input()
words=sentence.split()
result=' '.join([words[::-1]] for word in words)
print(result)'''

'''string1=input()
words=string1.split()
result=" ".join(word[::-1] for word in words)
print(result)'''


#check for unique characters
'''string1=input()
for i in string1:
    if string1.count(i)==1:
        print("unique",i)
    else:
        print("not unique",i)'''


#array sum
'''n=int(input())
nums=[]
target=int(input())
for _ in range(n):
    N=int(input())
    nums.append(N)
    nums.sort()
    left=0
    right=len(nums)-1
    while (left<=right):
        if(nums[left]+nums[right]>=target):
            right=right-1
        elif(nums[left]+nums[right]<=target):
            left=left+1
        elif(nums[left]+nums[right]==target):
            print(nums[left],nums[right])
            left=left+1
            right=right-1'''

#square root
'''n=int(input())
sqroot=n**0.5
print(int(sqroot))'''

#median of a list
'''n=int(input())
l=[]
for _ in range(n):
    N=int(input())
    l.append(N)
    l.sort()
    k=len(l)
    if n%2==0:
        mid1=(l[k//2-1])
        mid2=(l[k//2])
        median=(mid1+mid2)/2
        print(median)
    else:
        median=(l[k//2])
        print(median)'''


#base raised to exponent
'''base,exponent=map(int,input().split())
result=base**exponent
print(result)'''

#fizzbuzz
'''n=int(input())
for i in range(1,n+1):
    if i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    elif i%3==0 and i%5==0:
        print("FizzBuzz")
    else:
        print(i)'''

#Coleman Liau index
'''string1=input()
letters=sum(char.isalpha() for char in string1)
words=len(string1.split())
sentences=sum(char in '.?!' for char in string1)

L=(letters/words)*100
S=(sentences/words)*100
result=0.0588*L-0.296*S-15.8

if result>16:
    print("Grade 16+")
elif result<1:
    print("Before Grade 1")
else:
    print(f"Grade{round(result)}")'''

#common char
'''string1=input()
string2=input()
set1=set(string1)
set2=set(string2)
print(set1&set2)'''

#gcd and lcm
'''def gcd(a,b):
    while b:
        a,b=b,a%b
    return a
def lcm(a,b):
    lcm=abs(a*b)//gcd(a,b)
    return lcm
a=int(input())
b=int(input())
print(gcd(a,b))
print(lcm(a,b))'''

#roots of quadratic
'''b=int(input())
a=int(input())
c=int(input())
root1=(-b+(b**2-4*a*c)**0.5)/(2*a)
root2=(-b-(b**2-4*a*c)**0.5)/(2*a)
print(root1)
print(root2)'''

#factorial of a no
'''n=int(input())
fact=1
for i in range(1,n+1):
    fact=i*fact
print(fact)'''


#factors
'''n=int(input())
for a in range(1,n+1):
    if n%a==0:
        print(a)'''

#perfect no
'''n=int(input())
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i
if sum==n:
    print("perfect")
else:
    print("not perfect")'''

#prime or not
'''n=int(input())
for i in range(2,n):
    if n%i==0:
        print("not")
        break
    else:
        print("prime")
        break'''

#hcf
'''a=int(input())
b=int(input())
while a%b!=0:
    rem=a%b
    a=b
    b=rem
print(b)'''

#sum of digits
'''n=int(input())
sum=0
for i in range(0,n):
    a=n%10
    n=n//10
    sum+=a
print(sum)'''


#fibonacci number
'''n=int(input())
a=0, b=1
print(a,b)
for i in range(1,n+1):
    c=a+b
    print(c,end='')
    a=b
    b=c'''

#check palindrome no
'''n=int(input())
rev=0
while n>0:
    a=n%10
    rev=rev*10+a
    n=n//10
if n==rev:
    print("pal")
else:
    print("not")'''


#sum of series-I
'''n=int(input())
sum=0
for i in range(n+1):
    sum+=i
print(sum)'''

#sum of series-II
'''n=int(input())
sum=0
for i in range(1,n+1):
    sum+=1/i
print(sum)'''

#sum of series-III(x**1 to x**n)
'''x=int(input("enter number:"))
n=int(input("enter last power:"))
sum=0
p=1
for i in range(1,n+1):
    p=p*i
    sum+=(x**i)/p
print(x,"^",i,"/",p,"=",sum)'''


#until exit
'''sum=0
while True:
    n=input()
    if n=='exit':
        break
    else:
        sum+=int(n)
print(sum)'''

#add only no
'''sum=0
while True:
    n=input()
    if n.isalpha():
        continue
    if n=='exit':
        break
    if n.isdigit():
        sum+=int(n)
print(sum)'''


#gcd and lcm
'''n1=int(input())
n2=int(input())
def gcd(n1,n2):
    while n2!=0:
        n1,n2=n2,n1%n2
print(n1)
lcm=abs(n1*n2)/gcd(n1,n2)
print(lcm)'''



#no of vowels
'''string1=input()
vowels='aeiouAEIOU'
vowelcount=0
for char in string1:
    if char in vowels:
        vowelcount+=1
print(vowelcount)'''

'''string1=input()
vowels='aeiouAEIOU'
vowelcount=0
for i in string1:
    if i in vowels:
        vowelcount+=1
print(vowelcount)'''

#reverse string word by word
'''string1=input()
words=string1.split()
words=words[::-1]
res=''
for word in words:
    res+=word+' '
print(res)'''


#combi of 3
'''n1=int(input())
n2=int(input())
n3=int(input())
for i in range(3):
    for j in range(3):
        for k in range(3):
            print(i,j,k)

a=[0,0,0]
a[0]=int(input())
a[1]=int(input())
a[2]=int(input())
for i in range(3):
    for j in range(3):
        for k in range(3):
            print(a[i],a[j],a[k])'''

#array sum
'''n=int(input("enter total:"))
target=int(input("enter target:"))
list1=[]
for i in range(n):
    v=int(input("enter values:"))
    list1.append(v)
list1.sort()
left=0
right=len(list1)-1
while left<=right:
    if(list1[left]+list1[right]>target):
        right=right-1
    elif(list1[left]+list1[right]<target):
        left=left+1
    elif(list1[left]+list1[right]==target):
        print(list1[left],list1[right])
        left=left+1
        right=right-1'''


#convert salary into dollars
'''n=int(input("enter emplyees:"))
dict1={}
for i in range(n):
    name=input("enter name:")
    rup=float(input("enter salary:"))
    dict1[name]=rup
print(dict1)

for name in dict1:
    dict1[name]=round(dict1[name]/84,2)
print(dict1)'''


#frequency letter
'''string1=input()
freq={}
for i in string1:
    if i in freq:
        i.lower()
        freq[i]+=1
    else:
        freq[i]=1
print(freq)'''

#frequency word
'''string1=input()
words=string1.split()
freq={}
for word in words:
    if word in freq:
        freq[word]+=1
    else:
        freq[word]=1
print(freq)'''



#convert lc string to up and up string to lc
'''string1=input()
result=''
for char in string1:
    if char.islower():
        result+=char.upper()
    elif char.isupper():
        result+=char.lower()
    else:
        result+=char
print(string1)
print(result)'''

'''n=int(input())
dict1={}
for i in range(n):
    name=input("enter name:")
    count=int(input())
    dict1[name]=count
print(dict1)'''

#border sum
'''r=int(input("rows:"))
c=int(input("columns:"))
m=[]
for i in range(r):
    l=[]
    for j in range(c):
        v=int(input("enter:"))
        l.append(v)
    m.append(l)
print(m)

r=len(m)
c=len(m[0])
total=0
total+=sum(m[0])
total+=sum(m[r-1])
for i in range(1,r-1):
    total+=m[i][0]
    total+=m[i][-1]
print(total)'''

#sum of corners
'''r=int(input("rows:"))
c=int(input("columns:"))
m=[]
for i in range(r):
    l=[]
    for j in range(c):
        v=int(input("enter:"))
        l.append(v)
    m.append(l)
print(m)

r=len(m)
c=len(m[0])
total=m[0][0]+m[r-1][0]+m[0][c-1]+m[r-1][c-1]
print(total)'''

#row sum
'''r=int(input("rows:"))
c=int(input("columns:"))
m=[]
for i in range(r):
    l=[]
    for j in range(c):
        v=int(input("enter:"))
        l.append(v)
    m.append(l)
print(m)

total=[sum(scores) for scores in m]
print(total)'''

#column sum
'''r=int(input("rows:"))
c=int(input("columns:"))
m=[]
for i in range(r):
    l=[]
    for j in range(c):
        v=int(input("enter:"))
        l.append(v)
    m.append(l)
print(m)

total=[sum(columns) for columns in zip(*m)]
print(total)'''


#sum of tuple values
'''n=int(input("total:"))
list1=[]
total=0
for i in range(n):
    v=int(input("enter:"))
    list1.append(v)
tup1=tuple(list1)
print(tup1)
for j in tup1:
    total+=j
print(total)'''

#multiply tuple values
'''n=int(input("total:"))
list1=[]
for i in range(n):
    v=int(input("values:"))
    list1.append(v)
tup1=tuple(list1)
print(tup1)
product=1
for i in tup1:
    product=product*i
print(product)'''

#sum of tuple values
'''n=int(input("total:"))
list1=[]
for i in range(n):
    v=int(input("enter:"))
    list1.append(v)
tup1=tuple(list1)
print(tup1)
sum=0
for i in tup1:
    sum+=i
print(sum)'''

#remove duplicates
'''n=int(input())
list1=[]
for i in range(n):
    N=int(input())
    list1.append(N)
print(list1)
set1=set(list1)
list2=list(set1)
print(list2)'''

#without changing order
'''n=int(input())
orig=[]
dup=[]
for i in range(n):
    N=int(input())
    orig.append(N)
for i in orig:
    if i not in dup:
        dup.append(i)
print(orig)
print(dup)'''

#average of even no
'''sum=0
avg=0
n=int(input())
for i in range(n):
    number=int(input())
    if number%2==0:
        sum+=number
        avg+=1
if avg==0:
    print(0)
else:
    print(sum//avg)'''

#factorial of n
'''def factorial(n):
    if n==1:
        return n
    else:
        return n*factorial(n-1)
number=int(input())
if number==0:
    print("1")
else:
    print(factorial(number))
factorial(number)'''

#digits and sum
'''n=int(input())
string1=str(n)
print("digits:",len(string1))
sum=0
for i in range(len(string1)):
    sum+=int(string1[i])
print(sum)'''

#odd and even count
'''n=int(input())
even=0
odd=0
for i in range(n):
    number=int(input())
    if number%2==0:
        even+=1
    else:
        odd+=1
print(even)
print(odd)'''

#reverse a no
'''n=input()
rev=n[::-1]
print(rev)'''

'''n=int(input())
rev=0
while n!=0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
print(rev)'''

#print a no
'''n=int(input())
string1=str(n)
for i in string1:
    match int(i):
        case 1:
            print("One")
        case 2:
            print("Two")
        case 3:
            print("Three")
        case 4:
            print("Four")
        case 5:
            print("Five")
        case 6:
            print("Six")
        case 7:
            print("seven")
        case 8:
            print("Eight")
        case 9:
            print("Nine")
        case 0:
            print("Zero")'''

#square and cube
'''n=int(input())
square=n*n
print(square)
cube=n*n*n
print(cube)'''

#fibbonacci
'''n=int(input())
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print(fib(n))'''

#prime no true false
'''n=int(input())
for i in range(1,n+1):
    if n==1:
        print("False")
        break
    elif n==10:
        print("False")
        break
    elif n%i==0:
        print("True")
        break
    else:
        print("False")
        break'''

#max input in list
'''n=int(input())
max=0
list1=[]
for i in range(n):
    number=int(input())
    list1.append(number)
for i in list1:
    if i>max:
        max=i
print(max)'''

#sort in ascending
'''n=int(input())
list1=[]
for i in range(n):
    N=int(input())
    list1.append(N)
list1.sort()
print(list1)'''

#lcm
'''a=int(input())
b=int(input())
if a>b:
    greater=a
else:
    greater=b
while True:
    if greater%a==0 and greater%b==0:
        lcm=greater
        break
    greater+=1
print(lcm)'''


#lcm and its multiple
'''a=int(input())
b=int(input())
if a>b:
    greater=a
else:
    greater=b
while True:
    if greater%a==0 and greater%b==0:
        lcm=greater
        break
    greater+=1
print(lcm)
print(lcm//a)
print(lcm//b)'''

#fib series
'''n=int(input())
a=0
b=1
c=b
if n==0:
    pass
elif n==1:
    print(a)
elif n==2:
    print(a)
    print(b)
else:
    print(a)
    print(b)
    print(c)
    for i in range(2,n-1):
        a=b
        b=c
        c=a+b
        print(c)'''


#count unique in a list
'''n=int(input())
orig=[]
new=[]
for i in range(n):
    N=int(input())
    orig.append(N)
    for i in orig:
        if i not in new:
            new.append(i)
print(len(new))'''

#atm
'''n=int(input())
hundred=n//100
n=n%100
fifty=n//50
n=n%50
ten=n//10
n=n%10
print("hundred:",hundred)
print("fifty:",fifty)
print("tens:",ten)'''

#count vowels and consonants
'''n=int(input())
vowelcount=0
consonantcount=0
vowels=['a','e','i','o','u','A','E','I','O','U']
list1=[]
for i in range(n):
    N=input()
    list1.append(N)
    for i in list1:
        if i.isalpha():
            if i in vowels:
                vowelcount+=1
            else:
                consonantcount+=1
print(vowelcount)
print(consonantcount)'''

#avg and highest marks
'''n=int(input())
list1=[]
sum=0
for i in range(n):
    N=int(input())
    list1.append(N)
    list1.sort()
    sum+=N
avg=sum/n
print(avg)
print(list1[-1])'''

#sum of odd and even indexes
'''n=int(input())
list1=[]
evensum=0
oddsum=0
for i in range(n):
    N=int(input())
    list1.append(N)
list1.sort()
for i in range(0,len(list1),2):
    evensum+=list1[i]
for i in range(1,len(list1),2):
    oddsum+=list1[i]
print(evensum)
print(oddsum)'''


#reverse string
'''string1=input()
rev=string1[::-1]
print(rev)'''

#without changing order
'''string1=input()
words=string1.split()
result=' '.join(word[::-1] for word in words)
print(result)'''

#unique
'''string1=input()
set1=set(string1)
if len(string1)==len(set1):
    print("unique")
else:
    print("not unique")'''

#array sum
'''target=int(input("target:"))
n=list(map(int,input().split()))
n.sort()
left=0
right=len(n)-1
while left<=right:
    if(n[left]+n[right]>target):
        right=right-1
    elif(n[left]+n[right]<target):
        left=left+1
    elif(n[left]+n[right]==target):
        print(n[left],n[right])
        left=left+1
        right=right-1'''

'''n=int(input())
arr=list(map(int, input().split()))
target=int(input())
index={value: i+1 for i, value in enumerate(arr)}
left=0
right=len(arr)-1
if(arr[left]+arr[right]>target):
    right=right-1
elif(arr[left]+arr[right]<target):
    left=left+1
else:
    leftindex=index[arr[left]]
    rightindex=index[arr[right]]
    print(leftindex,rightindex)
    left=left+1
    right=right-1'''
    
#median
'''n=int(input())
l=[]
for i in range(n):
    m=int(input())
    l.append(m)
l.sort()
if n%2==0:
    median=l[n//2]
    print(median)
else:
    mid1=l[n//2-1]
    mid2=l[n//2]
    median=(mid1+mid2)/2
    print(median)'''

#square root
'''n=int(input())
sqroot=int(n**0.5)
print(sqroot)'''

#base exponent
'''base,exponent=map(int,input().split())
result=base**exponent
print(result)'''

#gcd
'''a=int(input())
b=int(input())
if a>b:
    greater=a
else:
    greater=b
while True:
    if greater%a==0 and greater%b==0:
        lcm=greater
        break
    greater+=1
print("lcm=",lcm)
gcd=(a*b)//lcm
print(gcd)'''

#fizzbuzz
'''n=int(input())
for i in range(1,n+1):
    if i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    elif i%3==0 and i%5==0:
        print("FizzBuzz")
    else:
        print(i)'''

#exit(sum numbers)
'''n=input().split()
sum=0
for i in n:
    if i=='exit':
        break
    else:
        sum+=int(i)
print(sum)'''

#exit(sum only numbers)
'''n=input().split()
sum=0
for i in n:
    if i=='exit':
        break
    elif i.isalpha():
        continue
    else:
        sum+=int(i)
print(sum)'''

#pair with max sum
'''n=int(input())
l=[]
for i in range(n):
    v=int(input())
    l.append(v)

l.sort()
print(l[-2],l[-1])'''

#a3b2
'''count=1
string1=input()
for i in range(1,len(string1)):
    if string1[i]==string1[i-1]:
        count+=1
    else:
        print(f"{string1[i-1]}{count}",end='')
        count=1
print(f"{string1[-1]}{count}",end='')'''




#max value in a list using recursion
'''def maxi():
    list1=[]
    for i in range(n):
        v=int(input())
        list1.append(v)
    list1.sort()
    return list1[-1]
n=int(input())
print(maxi())'''

#currency
'''list1=[]
list2=[]
name1=input("enter name:")
n1=int(input("number of notes:"))
for i in range(n1):
    v1=input("value:")
    list1.append(v1)
name2=input("enter name:")
n2=int(input("number of notes:"))
for i in range(n2):
    v2=input("value:")
    list2.append(v2)
set1=set(list1)
set2=set(list2)
print("common notes=",set1&set2)
print("notes with Payal=",set1-set2)
print("notes with Rashi=",set2-set1)'''

#reversing no
'''n=int(input())
rev=0
while n!=0:
    digit=n%10
    rev=10*rev+digit
    n=n//10
print(rev)'''

'''n=int(input())
dict1={}
for i in range(n):
    name=input("name:")
    volume=int(input("volume:"))
    dict1[name]=volume
print(dict1)'''

#frequency 
'''string1=input()
freq={}
for i in string1:
    if i.isalpha():
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
print(freq)'''

'''string1=input()
freq={}
words=string1.split()
for i in words:
    if i.isalpha():
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
print(freq)'''

'''n=int(input())
dict1={}
for i in range(n):
    name=input("name:")
    rupees=float(input("salary:"))
    dict1[name]=rupees
print(dict1)

dict2={}
for name,rupees in dict1.items():
    dict2[name]=round(rupees/84,2)
print(dict2)'''

'''string1=input()
string2=input()
list1=list(string1)
list2=list(string2)
sorted1=sorted(list1)
sorted2=sorted(list2)
if sorted1==sorted2:
    print("True")
else:
    print("False")'''

'''string1=input()
count=1
for i in range(1,len(string1)):
    if string1[i-1]==string1[i]:
        count+=1
    else:
        print(f"{string1[i-1]}{count}",end='')
        count=1
print(f"{string1[-1]}{count}",end='')'''

'''def filter_temp(readings,threshold):
    result=[((x*9/5)+32) for x in readings if x>threshold]
    print(result)
readings=[]
threshold=int(input("threshold:"))
n=int(input("total:"))
for i in range(n):
    v=float(input("celsius:"))
    readings.append(v)
filter_temp(readings,threshold)'''

'''list1=[]
product=1
n=int(input())
for i in range(n):
    v=int(input("value:"))
    list1.append(v)
    product=product*v
print(product)'''

'''list1=[]
n=int(input())
for i in range(n):
    v=int(input("value:"))
    list1.append(v)
print(list1)
rev=list1[::-1]
print(rev)'''

'''n=int(input())
if n%3==0 and n%5==0:
    print("Chitkara university")
elif n%3==0:
    print("Chitkara")
elif n%5==0:
    print("University")
else:
    print("not divisible")'''

'''n=int(input())
m=int(input())
set1=set()
set2=set()
for i in range(n):
    a=int(input())
    set1.add(a)
for j in range(m):
    b=int(input())
    set2.add(b)
print(set1)
print(set2)
set=set1&set2
print("common currencies:", set)
shuvam=set1-set2
print("Shuvam:", shuvam)
rishi=set2-set1
print("Rishi:",rishi)'''

'''def maximum():
    n=int(input())
    l=[]
    for i in range(n):
        m=int(input())
        l.append(m)
    l.sort()
    print(l[-1])
maximum()'''

'''threshold=int(input())
n=int(input())
l=[]
for i in range(n):
    m=int(input())
    l.append(m)
result=list(filter(lambda x:x<threshold,l))
print(result)'''

'''n=int(input())
l=[]
l2=[]
for i in range(n):
    m=int(input())
    l.append(m)
for num in l:
    if num not in l2:
        l2.append(num)
print(l2)'''

'''set1=set()
set2=set()
n=int(input())
m=int(input())
for i in range(n):
    a=int(input())
    set1.add(a)
for j in range(m):
    b=int(input())
    set2.add(b)
union=set1 | set2
print(union)
intersection=set1 & set2
print(intersection)
diff=set1=set2
print(diff)'''

'''n=int(input())
l=[]
l2=[]
for i in range(n):
    m=int(input())
    l.append(m)
for i in l:
    if l.count(i)==1 and i not in l2:
        l2.append(i)
print(l2)
print(len(l2))'''


'''n=int(input())
l=[]
for i in range(n):
    m=int(input())
    l.append(m)
l.sort()
diff=l[-1]-l[0]
print(diff)'''

'''n=int(input())
l=[]
sum=0
count=0
for i in range(n):
    m=int(input())
    l.append(m)
for i in l:
    sum+=i
    count+=1
print(sum)
print(sum//count)'''

'''n=int(input())
l=[]
for i in range(n):
    m=int(input())
    l.append(m)
start=int(input("index:"))
end=int(input("end:"))
for i in l[start:end+1]:
    print(i)'''


