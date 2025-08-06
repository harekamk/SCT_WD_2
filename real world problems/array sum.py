'''n=int(input("Enter no of elements:"))
list1=[]
sum=int(input("Enter sum:"))
for i in range(n):
    a=int(input())
    list1.append(a)
    list1.sort()
    left=0
    right=len(list1)-1
    while(left<=right):
        if(list1[left]+list1[right]>sum):
            right=right-1
        elif(list1[left]+list1[right]<sum):
            left=left+1
        elif(list1[left]+list1[right]==sum):
            print("values of pair are",list1[left],"&",list1[right])
            right=right-1
            left=left+1'''


