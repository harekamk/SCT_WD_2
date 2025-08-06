#find diff between sum of odd and even position digits
n=int(input())
even=0
odd=0
while n!=0:
    for i in range(n):
        if n%2==0:
            even=even+(n%10)
        else:
            odd=odd+(n%10)
            n=n//10
print(even-odd)