#string functions
'''a.lower
a.upper
a.strip  (removes white spaces from front and back)
a.replace("I","J")
a.split
concatenation(a+b)'''


#convert entire string into lower case, take a different string concatenate both strings 
'''a="HELLO MY NAME IS HAREKAM"
print(a)
print(a.lower())
b="I study in Chitkara University"
print(a.lower()+"."+" " +b)'''

#reverse
'''a="Hello World"
rev="Hello World"[::-1]
print(rev)'''

#print number of occurences 
'''a="HELLO WORLD"
print(a.count("H"))'''


'''content=input("enter:")
content=content.lower()
print(content)
for i in range(97,123):
    count=0
    j=chr(i)
    for l in content:
        if(j==l):
            count=count+1
            if count>0:
             print(j,":",count)'''

#replace space with -
'''string1=input()
string1=string1.replace(" ","-")
print(string1)'''

