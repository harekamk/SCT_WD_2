#print tuple
'''tup1=(1,2,3,4,5,6,7,"Hello)
print(tup1)
print(type(tup1))'''

#empty tuple
'''tup2=()
print(tup2)'''

#sum of elements
'''tup3=(1,44,7,5,6)
n1,n2,n3,n4,n5=tup3
print(n1+n2+n3+n4+n5)'''

#add item
'''cannot add as tuples are immutable'''

#convert tuple into string
'''tup5=("a","g","p","r","t")
str=''.join(tup5)
print(str)'''

#find repeated items
'''tup6=(1,2,3,4,5,6,7,8,9,1,1)
count=tup6.count(1)
print(count)'''

#check
'''tup7=(1,2,3,4,5,6,7,8,9)
if 7 in tup7:
    print("yes")
else:
    print("no")'''

#convert list into tuple
'''list1=[1,2,3,4,5,6,7,8,9]
print(list1)
tup8=tuple(list1)
print(tup8)'''

#remove
#elements cannot be removed directly
'''tup9=(1,2,3,4,5,6,7)
list2=list(tup9)
list2.remove(6)
print(list2)'''

#index
'''tup10=(1,2,3,4,5,6,7)
index=tup10.index(4)
print(index)'''

#convert tuple into dictionary
'''tup11=((2,"e"),(3,"r"),(4,"u"))
dict=dict(tup11)
print(dict)'''

#unzip
'''tup12=((1,2,3),(6,7,8))
result=list(zip(*tup12))
print(result)'''

#reverse
'''tup13=("resource")
x=reversed(tup13)
print(tuple(x))'''

#convert list of tuples into dict
'''tup14=[("x",1),("y",2),("z",3),("p",5)]
dict={}
dict.update(tup14)
print(dict)'''

#print tuple with square
'''ll=int(input())
ul=int(input())
tup1=[(x,x**2) for x in range(ll,ul+1)]
print(tup1)'''

#sort the tuple in inc order
