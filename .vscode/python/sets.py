#print a set
'''set1={1,2,3,"apple",True}
print(set1)
print(type(set1))'''

#add members
'''set2={2,5,"mango",65.9,False}
set2.add("red")
print(set2)'''

#remove item
'''set3={"red","orange","pink","blue","yellow"}
set3.remove("red")
print(set3)
set3.pop()
print(set3)'''

#intersection
'''set4={"red","blue","pink","orange","yellow","green"}
set5={"green","violet","blue","maroon"}
set=set4 & set5
print(set)'''

#union
'''set6={"red","blue","pink","orange","yellow","green"}
set7={"green","violet","blue","maroon"}
set=set6.union(set7)
print(set)'''

#set difference
#all those elements which are present in the first set
'''set8={"red","blue","pink","orange","yellow","green"}
set9={"green","violet","blue","maroon"}
r1=set8.difference(set9)
print(r1)
r2=set9.difference(set8)
print(r2)'''

#symmetric difference
#elements which are not repeated
'''set10={"red","blue","pink","orange","yellow","green"}
set11={"green","violet","blue","maroon"}
r1=set10.symmetric_difference(set11)
print(r1)
r2=set11.symmetric_difference(set10)
print(r2)'''

#subset
'''cities={"Florida","Madrid","Berlin","Barcelona","Paris","Ontario","Regina"}
cities2={"Regina","Ontario","Paris"}
print(cities2.issubset(cities))'''

#remove all
'''set12={"red","green","orange","pink","yellow"}
set12.clear()
print(set12)'''

#copy
'''set13={"red","green","orange","pink","yellow"}
set14=set13.copy()
print(set14)'''

#frozen sets
'''set15={1,2,3,4,5}
set16={3,4,5,6,7}
print(set15.isdisjoint(set16))
#nothing common 
print(set15.difference(set16))
print(set15)
print(set16)'''

#max and min
'''set17={1,2,3,4,5,6,7,8,9}
print(max(set17))
print(min(set17))'''

#length
'''set18={1,2,3,4,5,6,7}
print(len(set18))'''

#check a value
'''set19={"red","green","blue","pink","brown","black"}
if "black" in set19:
    print(True)
else:
    print(False)'''

#superset
'''set20={1,2,3,4,5,6,7}
set21={2,4}
set22={2,4}
if(set20>set21):
    print("set20 is a superset of set21")
elif(set21>set22):
    print("set21 is a superset of set22")
else:
    print("set22 is a superset")'''

#add set in a list
'''list1=['France','Paris','Miami']
set1={'Berlin','Florida'}
list1.append(set1)
print(list1)'''



