#wap to find the longest word in each input string
string1=input()
list1=list(string1.split())
m=0
for i in list1:
    m=max(m,len(i))
print(m)

#wap to find shortest word in the string