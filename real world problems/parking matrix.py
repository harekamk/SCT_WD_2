#a parking lot has RXC no of parking spaces. each space will either be empty(0) or full(1). the task is to find index of the row(R) that has most spaces
#full(1). RXC- size of matrix, elements of the matrix M should be only 0 or 1.
r=int(input("Enter no of rows:"))
c=int(input("Enter no of columns:"))
sum=0
m=0
id=0
for i in range(r):
    for j in range(c):
        sum+=int(input())
    if sum>m:
        m=sum
        id=i+1
    sum=0
print(id)