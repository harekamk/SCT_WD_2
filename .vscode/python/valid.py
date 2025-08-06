#otp
'''import random
for i in range(4):
    n=random.randint(0,9)
    print(n,end=' ')'''

#validity of an email
'''email=input("enter email:")
if email.endswith(".com"):
    if email[0]!="@" and email[-1]!="@" and email.count("@")==1:
        for ch in email:
            if ch.isalpha() or ch.isdigit() or ch=="." or ch=="@" or ch=="_":
                print("valid")
                break
    else:
        print("invalid")
else:
    print("invalid")'''

#name 
'''name=input()
if name.isalpha():
    print("valid")
else:
    print("invalid")'''

#phone number
'''number=input()
if len(number)!=15:
    print("invalid")
else:
    if number[4] not in ("6789"):
        print("invalid")
    elif number[0]=="+" and number[9]=="-" or " " in number:
        print("valid")
    else:
        print("invalid")'''

#password
'''password=input()
n=len(password)
u=0
l=0
d=0
s=0
a=0
if n>=8 and n<=16:
    
    for ch in password:
        if ch.isupper():
            u+=1
        elif ch.islower():
            l+=1
        elif ch.isdigit():
            d+=1
        elif ch in "@#$^&*_><?,.":
            s+=1
        else:
            a+=1
            break
    if a!=0:
        print("invalid")
    if(u>0 and l>0 and d>0 and s>0):
        print("password strength is good")
    else:
        print("invalid")
else:
    print("invalid")'''

#pronunciation(no 4 consonants together)
'''word=input()
c=0
for ch in word:
    if ch.isalpha():
        if ch not in 'aeiouAEIOU':
            c+=1
            if c==4:
                print("It is difficult to pronounce")
                break
        else:
            c=0
    else:
        print("invalid input")
        break
else:
    print("It is easy to pronounce")'''

#dollar dict
'''n=int(input("enter no of employees:"))
dict1={}
for i in range(n):
    name=input("name:")
    salary=float(input("salary:"))
    dict1[name]=salary
print(dict1)
for name in dict1:
    dict1[name]=round(dict1[name]/84,2)
print(dict1)'''

#anagrams
'''string1=input()
string2=input()
list1=list(string1)
list1.sort()
list2=list(string2)
list2.sort()
if list1==list2:
    print("anagrams")
else:
    print("not anagrams")'''

#temperature
'''def filter_temp(readings,threshold):
    return[(((9/5)*reading)+32) for reading in readings if reading>threshold]
n=int(input("enter:"))
readings=[]
for i in range(n):
    v=int(input("temperature:"))
    readings.append(v)
threshold=int(input("threshold:"))
print(filter_temp(readings,threshold))'''

#multiply values of a tuple
'''from functools import reduce
n=int(input("total:"))
list1=[]
for i in range(n):
    v=int(input())
    list1.append(v)
tup1=tuple(list1)
print(tup1)
#result=reduce(lambda x,y:x*y, list1)
result=1
for i in tup1:
    result=result*i
print(result)'''

#substring
'''string1=input()
start=int(input("start:"))
end=int(input("end:"))
substring=string1[start:end]
print(substring)'''

#lcs
'''string1=input()
string2=input()
for i in string1:
    if i in string2:
        print(i,end='')'''

#aabcccdeee
'''string1=input()
count=1
for i in range(1,len(string1)):
    if string1[i]==string1[i-1]:
        count+=1
    else:
        print(f"{string1[i-1]}{count}",end='')
        count=1
print(f"{string1[-1]}{count}")'''




