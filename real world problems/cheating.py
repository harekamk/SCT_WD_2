#a class has n students, the marks of n students are mentioned in M[] with index 1 to n. if any two adjacent students have same marks, then the 
#latter student will be removed from the list. then there will be re-evaluation which can impact marks of K students. the re-eval will update their
#marks and 3 lists will be declared. format is X Y. x is index of student whose marks are to be changed from original to y. 
#find max no of students that were part of merit list after each re-evaluation.  

def fun(x,y,n):
    arr[x-1]=y
    ans=1
    for i in range(1,n):
        if arr[i]!=arr[i-1]:
            ans+=1
n=int(input("Enter no of students:"))
k=int(input("Enter no of re-evaluations:"))
arr=[]
for i in range(n):
    arr.append(int(input(f"Enterbmarks of students{i+1}:")))
for i in range(k):
    x=int(input("Enter matrix position to update:"))
    y=int(input("Enter re-evaluated marks:"))
    print(fun(x,y,n))