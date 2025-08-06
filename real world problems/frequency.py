string1=input()
list1=string1.split()
dict1={}
for i in list1:
    if i not in dict1.keys():
        dict1[i]=0
    dict1[i]=dict1[i]+1
print(dict1)