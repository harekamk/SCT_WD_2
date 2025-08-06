#sum all items in a list
'''list1=[1,2,3,4,5,6,7]
print(sum(list1))'''

#multiply items in a list


#largest
'''list1=[6,9,24,67,1,2,3,4,5]
list1.sort()
print(list1[-1])'''

#smallest
'''list2=[1,3,4,5,6,0]
list2.sort()
print(list2[0])'''

#character frequency in a string
'''string1=input("enter string:")
freq={}
for i in string1:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)'''

#count the no of strings where the string length is 2 or more and the first and last character are same from a given list of strings



#get a list, sort in inc. order by the last element in each tuple from a given list of tuples



#get a string made of first 2 and last 2 characters
'''string2="mycrunch"
substring=string2[:2]+string2[-2:]
print(substring)'''

#get a string where all occurences of its first char have been changed to $ except the first char itself
'''string3="resource"
string=string3.replace("r","*")
string="r"+string[1:]
print(string)'''

#get a single string from two diff strings separated by a space and swap the first 2 char of each string

#add 'ing' at the end of a string. if the string already ends with 'ing' then add 'ly'
string1=input("enter:")


#wap that takes a list of words and returns the length of the longest one

#replace whole 'not...poor' with 'good'

#wap to check if an input is an integer

#sort the dict
'''dict1={"ravi":10,"rajnish":9,"sam":15}
mydict=list(dict1.keys())
mydict.sort()
sd={i:dict1[i] for i in mydict}
print(sd)'''

#add key to a dict
'''dict2={"key":"value"}
dict2["newkey"]="newvalue"
print(dict2)'''

#concatenate dict
'''dict3={"key":"value"}
dict4={"key2":"value2"}
dict3.update(dict4)
print(dict3)'''

#check if a given key exists in a dict
'''dict5={"key1":"value1","key2":"value2","key3":"value3"}
if "key3" in dict5:
    print("key exists")
else:
    print("key doesn't exist")'''

#iterate over dict using for loops
'''statesAndCapitals = {
    'Gujarat': 'Gandhinagar',
    'Maharashtra': 'Mumbai',
    'Rajasthan': 'Jaipur',
    'Bihar': 'Patna'
}
for capitals in statesAndCapitals.values():
 print(capitals)

for states in statesAndCapitals.keys():
    print(states)'''

#remove duplicates from a list
'''list6=[1,2,3,4,3,2,1]
list6=list(set(list6))
print(list6)'''

#copy a list
'''list7=[1,2,3,4,5,6,7]
list8=list7.copy()
print(list8)'''

#remove nth index from a list
'''list9=[1,2,3,4,5,6,7,8,9]
list9.pop(5)
print(list9)'''

#wap to change given string to a new string where first and last char have been exchanged
'''string2="accomplishment"
list1=list(string2)
temp=list1[0]
list1[0]=list1[-1]
list1[-1]=temp
print(list1)'''

#remove odd index char from a string
#find list of words that are longer than n from a given list of words
#count occurences of each word in a sentence
#wap that takes two lists and returns true if they have atleast one common char

