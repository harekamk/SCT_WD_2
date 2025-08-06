'''a=input("Enter the number:")
print(f"Multiplication table of {a} is:")
try:
    for i in range(1,11):
        print(f"{int(a)}*{i}={int(a)*i}")
except:
    print("Invalid input")

print("End of code")'''

'''try:
    index=int(input("Enter index:"))
    a=[6,3]
    print(a[index])
except ValueError:
    print("Number entered is not an integer")
except IndexError:
    print("Index Error")'''

'''def func1():
    try:
         l=[1,2,3,4]
         n=int(input("Enter index:"))
         print(l[n])
    except IndexError:
         print("Index error occured")
    except ValueError:
         print("Value is not an integer")
    finally:
         print("End of function")   
         print("End of function")  
func1()'''

'''a=input("enter:")
def func1():
    if a=='quit':
        print("program quitted")
    try:
        if (int(a)<5 or int(a)>9):
            raise ValueError("Value should be between 5 and 9")
    except ValueError as e:
        print(e)
    else:
        print(a)
func1()'''


