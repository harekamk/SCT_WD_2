#EXERCISM

#collatz conjecture
'''def collatz(n):
    while n>1:
        print(n,end=" ")
        if n%2!=0:
            n=3*n +1
        else:
            n=n//2
            print(1,end="")
n=int(input())
print("Sequence:",end=" ")
collatz(n)'''

#bob
'''q,c,s=0,0,0
enter=input()
if_ques="?"
if_capital="ABCDEFGHJIKLMNOPQRSTUVWXYZ"
if_silence="nothing"
for i in enter:
    if i in if_ques:
        print("Sure")
        break
for i in enter:
    if i in if_capital:
        print("Whoa,chill out!")
        break
for i in enter:
    if i in if_silence:
        print("Calm down! I know what i'm doing!")
        break
    else:
        print("Whatever")
        break'''

#raindrops
'''def raindrops(n):
    result=' '

    if n%3==0:
        result+="Pling"

    if n%5==0:
        result+="Plang"

    if n%7==0:
        result+="Plong"
n=int(input())
print(result)
raindrops(n)'''

#darts
'''n=int(input("enter radius:"))
if n>=0 and n<=1:
    print("10 points")
elif n>1 and n<=5:
    print("5 points")
elif n>5 and n<=10:
    print("1 point")
else:
    print("0 points")'''

#perfect numbers
'''n=int(input())
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i

if n==sum:
    print("perfect")
elif n<sum:
    print("abundant")
else:
    print("deficient")'''

#resistor color
'''colorcodedict={'black':0,'brown':1,'red':2,'orange':3,'yellow':4,'green':5,'blue':6,'violet':7,'gray':8,'white':9}
print(colorcodedict)'''

n=int(input())
dict1={}
for i in range(n):
    name=input("name:")
    rupees=float(input("rupees:"))
    dict1[name]=rupees

print(dict1)
dict2={}
for name,rupees in dict1.items():
    



