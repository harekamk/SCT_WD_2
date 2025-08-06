#the task is to find the empty packets(0) and push it to the end of the array.

#order changing
n=int(input("enter no of elements:"))
array1=[]
for i in range(1,n+1):
    a=int(input())
    array1.append(a)
array1.sort(reverse=True)
print(array1)

#without changing order
n=int(input())
j=0
array1=[0 for i in range(n)]
for i in range(n):
    a=int(input())
    if a!=0:
        array1[j]=a
        j+=1
for i in array1:
    print(i,end=" ")