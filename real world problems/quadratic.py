#formula=-b+-(b**2-4*a*c**0.5)/2*a
a=int(input())
b=int(input())
c=int(input())
root1=(-b+(b**2-4*a*c)**0.5)/(2*a)
root2=(-b-(b**2-4*a*c)**0.5)/(2*a)
print(root1)
print(root2)