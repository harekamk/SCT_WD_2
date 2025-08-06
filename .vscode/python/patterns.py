#LHS triangle numbers
'''row=5
for i in range(1,row+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()'''

#inverted LHS triangle numbers
'''row=5
for i in range(row,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()'''

#inverted(0-4)
'''row=5
for i in range(row,0,-1):
    for j in range(0,i):
        print(j,end=" ")
    print()'''

# inverted(0-5)
'''row=5
for i in range(row,0,-1):
    for j in range(0,i+1):
        print(j,end=" ")
    print()'''

#LHS triangle stars
'''row=5
for i in range(1,row+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()'''

#inverted LHS triangle stars
'''row=5
for i in range(row+1,0,-1):
    for j in range(0,i+1):
        print("*",end=" ")
    print()'''

#downward full pyramid
'''row=5
for i in range(row,-1,-1):
    for j in range(1,i+1):
        print("*",end=" ")
        for k in range(i-1):
            print(" ",end=" ")
        print()'''

#print two pyramids
'''row=6
for i in range(0,row+1):
    for j in range(0,i+1):
        print("*",end=" ")
    print()

print(" ")
row=6
for i in range(row+1,0,-1):
    for j in range(0,i+1):
        print("*",end=" ")
    print()'''

#two pyramids into one
'''row=5
for i in range(1,row+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
row=4
for i in range(row,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()'''


#side triangle with alphabets
'''ascii_value=65
row=5
for i in range(1,row+1):
    for j in range(1,i+1):
        character=chr(ascii_value)
        print(character,end=" ")
        ascii_value+=1
    print()'''

#display letter of word
'''word="Python"
x=""
for i in word:
    x+=i
    print(x)'''

#hollow square
'''row=6
for i in range(1,row+1):
    for j in range(1,row+1):
        if i==1 or i==n or j==1 or j==n:
            print("*",end="")
        else:
            print(" ",end="")
    print()'''

#pyramid
'''n=6
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")

    for k in range(2*i-1):
        print("*",end="")
    print()'''

'''row=5
for i in range(1,row+1):
    for j in range(1,row+1):
        print("*",end="")
    print()'''

#LHS triangle with alphabets 
'''row=6
ascii_value=65
for i in range(0,row):
    for j in range(i+1):
        alphabet=chr(ascii_value)
        print(alphabet,end="")
    ascii_value+=1
    print()'''

#inverted LHS triangle
'''row=5
for i in range(1,row+1):
    for j in range(row-i):
        print("*",end="")
    print()'''

'''n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()'''

#pyramid
'''row=6
for i in range(1,row+1):
    for j in range(row-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()'''

#reverse pyramid
'''row=6
for i in range(1,row+1):
    for j in range(row-1):
        print(" ",end=" ")
    for k in range():
        print("*",end=" ")
    print()'''

