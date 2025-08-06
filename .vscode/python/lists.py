'''fruits=['apple','mango','grapes','cherry','strawberry']
print(fruits)
print(len(fruits))
print(type(fruits))
print(fruits[2])
print(fruits[-3])
print(fruits[2:4])   #last one not included
print(fruits[:3])
print(fruits[0:])
print(fruits[-4:-1])    #1 to 4'''

'''brands=['madame','puma','nike','adidas','levis']
brands[0]='glamly'
print(brands)
brands[1:4]=['octave','skechers','rayban']
print(brands)'''

#list functions
'''snacks=['maggi','pasta','idli','dosa','spring rolls','samosa']
snacks.insert(2,"momos")
print(snacks)
snacks.append("pizza")  
print(snacks)'''

'''thislist=['apple','mango','grapes','banana']'''
'''thistuple=('kiwi','orange')
thislist.extend(thistuple)
print(thislist)'''

'''thislist.remove("mango")
print(thislist)'''

'''thislist.pop(2)
print(thislist)'''

'''del thislist[1]
print(thislist)'''

'''thislist.clear()
print(thislist)'''

'''for x in "apple":
    print(x)'''

'''for x in thislist:
    if x=="mango":
        break
    print(x)'''

'''for x in thislist:
    if x=="mango":
        continue
    print(x)'''

'''adj=["red","big","tasty"]
fruit=["apple","cherry","strawberry","litci","pomegranate"]
for x in adj:
    for y in fruit:
        print(x,y)'''

#list
'''numbers=[12,75,150,180,145,525,50]
for item in numbers():
    if item>500:
        break
    elif item>150:
        continue
    elif item%5==0:
        print(item)'''

#reverse list
'''list1=[1,2,3,4,5,6,7,8,9]
rev_list=list1[::-1]
print(rev_list)'''

#largest no 
'''a=[]
n=int(input("enter number of elements:"))
for i in range(1,n+1):
    b=int(input("enter element:"))
    a.append(b)
a.sort()
print("Largest element=",a[n-1])'''

#second largest no
'''a=[]
n=int(input("enter number of elements:"))
for i in range(1,n+1):
    b=int(input("enter element:"))
    a.append(b)
a.sort()
print("Second largest element=",a[n-2])'''

#check if sm exists or not
'''list1=['10','20','30','40','50']
i='30'
if i in list1:
    print("yes")
else:
    print("no")'''

#copy list
'''names=["John","Jatin","Mark","Jia","Mia"]
copy_names=[x for x in names]
print(copy_names)'''

'''copy=[]
copy.extend(names)
print(copy)'''

#capitalise first letter
'''animals=["lion","tiger","monkey","elephant","frog"]
filtered_animals=[]
for x in animals:
    filtered_animals.append(x.title())
print(filtered_animals)'''

#grades
'''marks=[77,87,96,66,69,71,99,32,56,59]
def grade(marks):
    if marks>=90:
        return "A"
    elif 80<=marks<90:
        return "B"
    elif 70<=marks<80:
        return "C"
    elif 60<=marks<70:
        return "D"
    else:
        return "F"
grades=map(grade,marks)
print("Exam marks:",marks)
print("Grades:",list(grades))'''

#1 double all the numbers in the list using map function and list comprehension
#2 create two different list named list1 and list2 and add two numbers of two lists in sequent manner using lambda and map function
#3 find out vowels in a provided string using list comprehension
#4 find out if a number is divisible by 2 and 5 using list comprehension

'''nums=[1,2,3,4,5,6,7,8,9]
new_nums=[]
new_nums=[2*x for x in nums]
print(new_nums)'''

#count occurences
'''names=["John","Albert","Sam","Pam","Sarah","Megan","John","John","John","John"]
ele="John"
x=[i for i in names if i==ele]
print(len(x))'''

#sum and average
'''list1=[1,4,6,9,98,65,3,4,5,6,7]
count=0
for i in list1:
    count+=i
    print("sum=",count)
average=count/len(list1)
print("average=",average)'''

#multiply
'''from functools import reduce
list1=[1,2,3]
list2=[4,5,6]
result1=reduce((lambda x,y:x*y),list1)
result2=reduce((lambda x,y:x*y),list2)
print(result1)
print(result2)'''

#smallest and second smallest element
'''list1=[4,5,6,7,1]
list1.sort()
print(list1[0])
print(list1[1])'''

#largest and second largest element
'''list1=[10,11,2,3,4]
list1.sort()
print(list1[-1])
print(list1[2])'''

#even and odd
'''list1 = [10, 21, 4, 45, 66, 93]
for x in list1:
    if x%2==0:
        print(x,end=" ")'''

#count even and odd
'''list1=[10,11,2,3,4,5,7,8,24]
even_count=0
odd_count=0
for x in list1:
    if x%2==0:
        even_count+=1
    else:
        odd_count+=1
print(even_count)
print(odd_count)'''

#map function
'''def addition(n):
    return n+n
numbers=(1,2,3,4)
result=map(addition,numbers)
print(list(result))'''

#filter function
'''ages=[5,12,13,17,18,19,25,30]
def vote(x):
    if x<18:
        return False
    else:
        return True
voting=filter(vote,ages)
print("vote:",list(voting))'''

#reduce function
'''import functools
num=[1,2,3,4,5,6]
print(functools.reduce(lambda x,y:x+y, num))'''

#add elements in a list
'''list1=[]
n=int(input())
for i in range(1,n+1):
    a=input()
    list1.append(a)
print(list1)'''

#largest even and odd number

#separate even and odd no
'''n=int(input())
list1=[]
for i in range(1,n+1):
    m=int(input())
    list1.append(m)
odd=[]
even=[]
for j in list1:
    if j%2==0:
        even.append(j)
    else:
        odd.append(j)
print(odd)
print(even)'''

#avg of elements in a list
'''n=int(input())
list1=[]
for i in range(1,n+1):
    element=int(input())
    list1.append(element)
avg=sum(list1)/n
print(list1)
print(avg)'''

#sum of neg no, sum of positive odd no and sum of positive even no
'''n=int(input())
list1=[]
for i in range(1,n+1):
    a=int(input())
    list1.append(a)
sum1=0
sum2=0
sum3=0
for j in list1:
    if j>0:
        if j%2==0:
            sum1+=j
        else:
            sum2+=j
    else:
        sum3+=j
print("Sum of positive even numbers is:",sum1)
print("Sum of positive odd numbers is:",sum2)
print("Sum of negative numbers is:",sum3)'''

#count occurence
'''n=int(input())
list1=[]
for i in range(1,n+1):
    m=int(input())
    list1.append(m)
num=int(input("enter no to be counted:"))
k=0
for j in list1:
    if k==num:
        k+=1
print(k)'''

#sum of elements using recursion

#length using recursion

#merge two lists into a new one and sort it
'''n=int(input("enter no of elements in list1"))
list1=[]
m=int(input("enter no of elements in list2"))
list2=[]
for i in range(1,n+1):
    a=int(input())
    list1.append(a)
for j in range(1,m+1):
    b=int(input())
    list2.append(b)
list3=list1+list2
print(list3)'''

#remove duplicates
'''n=int(input())
list1=[]
for i in range(1,n+1):
    m=int(input())
    list1.append(m)
set1=set(list1)
print(set1)'''

#sort a list acc to second element in a sublist

#length of longest words
'''input_words=input()
words=input_words.split()
final=[]
for x in words:
    final.append((len(x),x))
final.sort()
print(final[-1][1])'''

#find the no occuring odd no of times in a list

#generate random no and append them in a list
'''import random
n=int(input("Enter no of elements:"))
list1=[]
for i in range(n):
    list1.append(random.randint(1,20))
print(list1)'''

#remove ith occurence

#union and intersection of two lists
'''list1=[]
n=int(input("enter no.of elements in list1:"))
for i in range(1,n+1):
    a=int(input("Elements in list1:"))
    list1.append(a)
list2=[]
m=int(input("enter no of elements in list2:"))
for j in range(1,m+1):
    b=int(input("Elements in list2:"))
    list2.append(b)
set1=set(list1)
set2=set(list2)
set3=set1.intersection(set2)
set4=set1.union(set2)
print("intersection=",set3)
print("union=",set4)'''

#reverse a list
'''n=int(input())
list1=[]
for i in range(n):
    v=int(input())
    list1.append(v)
print(list1)

rev=list1[::-1]
print(rev)'''

#swap adjacent
'''n=int(input())
list1=[]
for i in range(n):
    v=int(input())
    list1.append(v)
print(list1)

for i in range(0,len(list1),2):
    temp=list1[i]
    list1[i]=list1[i+1]
    list1[i+1]=temp
print(list1)'''

#swap 1st half with 2nd half
'''n=int(input())
list1=[]
for i in range(n):
    v=int(input())
    list1.append(v)
print(list1)

l=len(list1)
if l%2==0:
    gap=l//2
else:
    gap=(l//2)+1

for i in range(l//2):
    temp=list1[i]
    list1[i]=list1[i+gap]
    list1[i+gap]=temp
print(list1)'''

#remove duplicates
'''n=int(input())
list1=[]
for i in range(n):
    v=int(input())
    list1.append(v)
print(list1)
set1=set(list1)
list2=list(set1)
print(list2)'''

#second highest value
'''n=int(input())
list1=[]
for i in range(n):
    v=int(input())
    list1.append(v)
    list1.sort()
print(list1[-2])'''

#union and intersection
'''n1=int(input())
n2=int(input())
list1=[]
list2=[]
for i in range(n1):
    v1=int(input())
    list1.append(v1)
for j in range(n2):
    v2=int(input())
    list2.append(v2)
print(list1)
print(list2)

set1=set(list1)
set2=set(list2)

u=set1.union(set2)
inter=set1.intersection(set2)
print(u)
print(inter)

ul=list(u)
intersec=list(inter)'''

#cartesian product
'''n1=int(input())
n2=int(input())
list1=[]
list2=[]
for i in range(n1):
    v1=int(input())
    list1.append(v1)
for j in range(n2):
    v2=int(input())
    list2.append(v2)
res=[]
for k in list1:
    for m in list2:
        res.append((k,m))
print(list1)
print(list2)
print(res)'''

#