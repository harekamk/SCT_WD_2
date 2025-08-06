#the price of the item is the product of all its digits
count=0
number=int(input("Enter number:"))
while number!=0:
    a=number%10
    number=number//10
    count+=1
    amount=number*a
print(amount)



