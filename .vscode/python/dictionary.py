#check if a key exists in a dict or not
'''dict1={"A":1,"B":2,"C":3,"D":4}
key1=input()
if key1 in dict1.keys():
    print("key is present")
else:
    print("key is not present")'''

#add a key value pair
'''dict1={"A":1,"B":2,"C":3,"D":4}
dict1.update({"E":5})
print(dict1)'''

#sum all values
'''dict1={"A":1,"B":2,"C":3,"D":4}
print(sum(dict1.values()))'''

#multiply
'''dict1={"A":1,"B":2,"C":3,"D":4}
total=1
for i in dict1:
    total=total*dict1[i]
print(total)'''

#remove
'''dict1={"A":1,"B":2,"C":3,"D":4}
dict1.pop("C")
print(dict1)'''

#map two lists into dict
'''keys=[]
n=int(input("Enter no of elements:"))
for x in range(0,n):
    a=input("enter element"+str(x+1)+":")
    keys.append(a)
values=[]
for x in range(0,n):
    b=int(input("enter element"+str(x+1)+":"))
    values.append(b)
dict1=dict(zip(keys,values))
print(dict1)'''

#number with square
'''n=int(input("enter a number:"))
dict1={x:x*x for x in range(1,n+1)}
print(dict1)'''

#count frequncy using dict
'''string1=input()
list1=[]
list1=string1.split()
freq=[list1.count(x) for x in list1]
print(dict(zip(list1,freq)))'''