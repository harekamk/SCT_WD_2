#add two matrices
'''A=[[3,7,9],
   [10,5,7],
   [1,5,2]]

B=[[3,4,5],    
   [8,6,2],
   [1,2,3]]

result=[[0,0,0],
        [0,0,0],
        [0,0,0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        result[i][j]=A[i][j]+B[i][j]

for r in result:
    print(r)'''

#multiply two matrices
#remember: column of 1st should be equal to rows of 2nd....your result should be in correct format
'''A=[[1,2,3],
   [4,5,6],
   [7,8,9]]

B=[[9,8,7],
   [3,6,5],
   [1,3,8]]

result=[[0,0,0],
        [0,0,0],
        [0,0,0]]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j]=A[i][k]*B[k][j]

for r in result:
    print(r)'''

#transpose of a matrix
'''A=[[1,2,3],
   [4,5,6],]

T=[[0,0],
   [0,0],
   [0,0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        T[j][i]=A[i][j]
for r in T:
    print(r)'''

#user input matrix
'''r=int(input())
c=int(input())
m=[]
for i in range(r):
    l=[]
    for j in range(c):
        v=int(input())
        l.append(v)
    m.append(l)
print(m)'''


#calculate sum of coins located on the borders of a 2d matrix. the border includes elements in the first and last rows and columns
'''r=int(input())
c=int(input())
m=[]
for i in range(r):
    l=[]
    for j in range(c):
        v=int(input())
        l.append(v)
    m.append(l)
print(m)

def sum_border():
    r=len(m)
    c=len(m[0])
    #sum of first row
    border_sum=sum(m[0])
    #sum of last row
    if r>1:
        border_sum+=sum(m[-1])
    #sum of first and last columns excluding the ones already counted
    for i in range(1,r-1):
        border_sum+=m[i][0]
        if c<1:
            border_sum+=m[i][-1]
    return border_sum
border_sum=sum_border()
print(border_sum)'''

'''r=int(input())
c=int(input())
m=[]
for i in range(r):
    l=[]
    for j in range(c):
        v=int(input())
        l.append(v)
    m.append(l)
print(m)

#sum of first row
total=sum(m[0])
if r>1:
    total+=sum(m[-1])
#sum of columns
for i in range(1,r-1):
    total+=m[i][0]
    if c>1:
        total+=m[i][-1]
print(total)'''

#sum of corners
'''r=int(input())
c=int(input())
m=[]
for i in range(r):
    l=[]
    for j in range(c):
        v=int(input())
        l.append(v)
    m.append(l)
print(m)
sum=0
#top left
sum+=m[0][0]
#top right
sum+=m[0][c-1]
#bottom left
sum+=m[r-1][0]
#bottom right
sum+=m[r-1][c-1]
print(sum)'''


#find max no of coins in each column. given m rows, n columns, m*n integers as cell values, write a func to return a list of largest values from each col
'''r=int(input())
c=int(input())
m=[]
for i in range(r):
    l=[]
    for j in range(c):
        v=int(input())
        l.append(v)
    m.append(l)
print(m)

def max_columns():
    c=len(m[0])
    max_in_columns=[]
    for col in range(c):
        max_value=max(r[col] for r in m)
        max_in_columns.append(max_value)
    return max_in_columns
max_in_columns=max_columns()
print(max_in_columns)'''

#row sum
'''r=int(input())
c=int(input())
m=[]
for i in range(r):
    l=[]
    for j in range(c):
        v=int(input())
        l.append(v)
    m.append(l)
print(m)
def total_sum():
    total_scores=[sum(student_scores) for student_scores in m]
    return total_scores
total_scores=total_sum()
print(total_scores)'''

#multiply
'''r1=int(input())
c1=int(input())
m1=[]
r2=int(input())
c2=int(input())
m2=[]
for i in range(r1):
    l1=[]
    for j in range(c1):
        v=int(input())
        l1.append(v)
    m1.append(l1)
print(m1)

for i in range(r2):
    l2=[]
    for j in range(c2):
        w=int(input())
        l2.append(w)
    m2.append(l2)
print(m2)

def multiply_matrix():
    result=[[0 for _ in range(len(m2[0]))] for _ in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                result[i][j]+=m1[i][k]*m2[k][j]
    return result
result=multiply_matrix()
print(result)'''

#sum
'''r1=int(input("enter no of row1:"))
c1=int(input("enter no of column1:"))
m1=[]
for i in range(r1):
    l1=[]
    for j in range(c1):
        v1=int(input("enter value:"))
        l1.append(v1)
    m1.append(l1)
print(m1)

r2=int(input("enter no of r2:"))
c2=int(input("enter no of c2:"))
m2=[]
for i in range(r2):
    l2=[]
    for j in range(c2):
        v2=int(input("enter value:"))
        l2.append(v2)
    m2.append(l2)
print(m2)

if r1==r2 and c1==c2:
    result=[]
    for i in range(r1): 
        sum=[]
        for j in range(c1):
            sum.append(m1[i][j]+m2[i][j])
        result.append(sum)
    print(result)
else:
    print("dimensions are not same")'''


#sum of borders
'''r=int(input("rows:"))
c=int(input("columns:"))
m=[]
for i in range(r):
    l=[]
    for j in range(c):
        v=int(input("enter:"))
        l.append(v)
    m.append(l)
print(m)

r=len(m)
c=len(m[0])
total=0
#first row
total+=sum(m[0])
#last row
total+=sum(m[r-1])
#columns
for i in range(1,r-1):
    total+=m[i][0]
    total+=m[i][-1]
print(total)'''

'''r=int(input())
c=int(input())
m=[]
for i in range(r):
    l=[]
    for j in range(c):
        v=int(input("value:"))
        l.append(v)
    m.append(l)
print(m)

total=0
r=len(m)
c=len(m[0])
for val in m[0]:
    total+=val
for val in m[-1]:
    total+=val
for i in range(1, r-1):
    total+=m[i][0]
    total+=m[i][-1]
print(total)'''

#sum of only corners
'''r=int(input("rows:"))
c=int(input("columns:"))
m=[]
for i in range(r):
    l=[]
    for j in range(c):
        v=int(input("enter:"))
        l.append(v)
    m.append(l)
print(m)

r=len(m)
c=len(m[0])
total=m[0][0]+m[r-1][0]+m[0][c-1]+m[r-1][c-1]
print(total)'''

#row sum
'''r=int(input("row:"))
c=int(input("column:"))
m=[]
for i in range(r):
    l=[]
    for j in range(c):
        v=int(input("enter:"))
        l.append(v)
    m.append(l)
print(m)
result=[sum(scores) for scores in m]
print(result)'''

#max along with row sum
'''r=int(input("rows:"))
c=int(input("columns:"))
m=[]
for i in range(r):
    l=[]
    for j in range(c):
        v=int(input("enter:"))
        l.append(v)
    m.append(l)
print(m)

result=max([sum(scores) for scores in m])
print(result)'''

#first and last row sum
'''r=int(input("rows:"))
c=int(input("columns:"))
m=[]
for i in range(r):
    l=[]
    for j in range(c):
        v=int(input("values:"))
        l.append(v)
    m.append(l)
print(m)

r=len(m)
c=len(m[0])
total=sum(m[0])+sum(m[-1])
print(total)'''

'''total=0
r=int(input())
c=int(input())
m=[]
for i in range(r):
    l=[]
    for j in range(c):
        v=int(input("value:"))
        l.append(v)
    m.append(l)
print(m)
r=len(m)
c=len(m[0])
for val in m[0]:
    total+=val
for val in m[-1]:
    total+=val
print(total)'''

#sum of first and last column
'''r=int(input("rows:"))
c=int(input("columns:"))
m=[]
for i in range(r):
    l=[]
    for j in range(c):
        v=int(input("values:"))
        l.append(v)
    m.append(l)
print(m)

r=len(m)
c=len(m[0])
total=0
for i in range(r):
    total+=sum(m[i][0])+sum(m[i][-1])
print(total)'''


#sum of edges
'''r=int(input("row:"))
c=int(input("columns:"))
m=[]
for i in range(r):
    l=[]
    for j in range(c):
        v=int(input("values:"))
        l.append(v)
    m.append(l)
print(m)

sum=m[0][0]+m[r-1][0]+m[0][c-1]+m[r-1][c-1]
print(sum)'''


#multiply
'''r1=int(input("rows1:"))
c1=int(input("column1:"))
m1=[]
for i in range(r1):
    l1=[]
    for j in range(c1):
        v1=int(input("value:"))
        l1.append(v1)
    m1.append(l1)
print(m1)
r2=int(input("rows2:"))
c2=int(input("column2:"))
m2=[]
for i in range(r2):
    l2=[]
    for j in range(c2):
        v2=int(input("value:"))
        l2.append(v2)
    m2.append(l2)
print(m2)
result=[[0 for _ in range(c2)]for _ in range(r1)]
for i in range(r1):
    for j in range(c2):
        for k in range(c1):
            result[i][j]+=m1[i][k]*m2[k][j]
print(result)'''


#transpose
'''r=int(input("rows:"))
c=int(input("columns:"))
m=[]
for i in range(r):
    l=[]
    for j in range(c):
        v=int(input("value:"))
        l.append(v)
    m.append(l)
print(m)

transposematrix=[]
for j in range(c):
    transposerow=[]
    for i in range(r):
        transposerow.append(m[i][j])
    transposematrix.append(transposerow)
print(transposematrix)'''

#diagonal sum
'''n=int(input("rws/columns:"))
m=[]
for i in range(n):
    l=[]
    for j in range(n):
        v=int(input("value:"))
        l.append(v)
    m.append(l)
print(m)

pridiag=0
secdiag=0

for i in range(n):
    pridiag+=m[i][i]
    secdiag+=m[i][n-i-1]

if n%2!=0:
    center=m[n//2][n//2]
    diagsum=pridiag+secdiag-center
print(pridiag)
print(secdiag)
print(diagsum)'''


'''r1=int(input())
c1=int(input())
m1=[]
for i in range(r1):
    l1=[]
    for j in range(c1):
        v1=int(input())
        l1.append(v1)
    m1.append(l1)
print(m1)

r2=int(input())
c2=int(input())
m2=[]
for i in range(r2):
    l2=[]
    for j in range(c2):
        v2=int(input())
        l2.append(v2)
    m2.append(l2)
print(m2)

if r1!=r2 or c1!=c2:
    print("matrices cannot be added")
else:
    result=[[0 for _ in range (c1)]for _ in range (r1)]
    for i in range(r1):
        for j in range(c1):
            result[i][j]=m1[i][j]+m2[i][j]
print(result)'''

def largest(x,y):
    lcs=[]
    y=list(y)
    for i in x:
        if i in y:
            lcs.append(i)
            y.remove(i)
    return ''.join(lcs)
string1=input()
string2=input()
print(largest(string1,string2))