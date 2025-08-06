#a string contains digits only. the task is to find the remainder of str when n is divided by k.
n=input()
k=input()
s=0
for i in range(0,len(n),len(k)):
    