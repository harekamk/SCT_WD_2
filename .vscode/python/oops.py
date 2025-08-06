'''class Person:
    name="Ekam"
    occupation="Software Engineer"

    def info(self):
        print(f"{self.name} is a {self.occupation}")

a=Person()
b=Person()
c=Person()

a.name="Harry"
a.occupation="HR"
b.name="Shubham"
b.occupation="Accountant"
a.info()
b.info()'''

'''class Person:
    def __init__(self, n, o):
        print("Hey!")
        self.name=n
        self.occ=o
    def info(self):
        print(f"{self.name} is a {self.occ}")
a=Person("Harry", "Developer")
b=Person("Divya", "Artist")
c=Person("Shivam", "HR")
a.info()
b.info()
c.info()'''

#docstring
'''def square(n):
    "Takes a number n and prints its square"
    print(n**2)
square(5)
print(square.__doc__)'''

'''class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def showDetails(self):
        print(f"The name of Employee: {self.id} is {self.name}")

class Programmer(Employee):
    def language(self):
        print("The default language is python.")
e1=Employee("rohan", 400)
e1.showDetails()
e2=Programmer("John", 200)
e2.showDetails()
e2.language()'''

#public access modifier
'''class Employee:
    def __init__(self):
        self.name="Harry"
a=Employee()
print(a.name)'''

#private access modifier
'''class Employee:
    def __init__(self):
        self.__name="Harry"
a=Employee()
print(a._Employee__name)'''

'''class Student:
    def __init__(self):
        self._name="Harry"

    def _funName(self):
        return "CodewithHarry"
class Subject(Student):
    pass

obj=Student()
obj1=Subject()

print(obj._name)
print(obj._funName())
print(obj1._name)
print(obj1._funName())'''

'''class Employee:
    companyName="Apple"
    noofemployees=0
    def __init__(self,name):
        self.name=name
        self.raise_amount=0.02
        Employee.noofemployees+=1
    def showDetails(self):
        print(f"The name of the employee is {self.name} and the raise amount in {self.noofemployees} sized {self.companyName} is {self.raise_amount}")

emp1=Employee("Harry")
emp1.raise_amount=0.3
emp1.companyName="flipkart"
emp1.showDetails()
emp2=Employee("Rohan")
emp2.showDetails()'''

#dictionary
'''class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
        self.version=1
p=Person("John", 30)
print(p.__dict__)'''

#dir()
'''x=[1,2,3]
print(dir(x))
print(x.__add__)'''

'''class Shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def area(self):
        return self.x*self.y
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius
rec=Shape(3,5)
print(rec.area())
c=Circle(5)
print(c.area())'''
#OR
'''class Shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def area(self):
        return self.x*self.y
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
        super().__init__(radius,radius)
    def area(self):
        return 3.14*super().area()
rec=Shape(3,5)
print(rec.area())
c=Circle(5)
print(c.area())'''

'''class Vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
    def __str__(self):
        return f"{self.i}i+{self.j}j+{self.k}k"
    def __add__(self,x):
        return Vector(self.i+x.i,self.j+x.j+self.k+x.k)
v1=Vector(3,5,6)
print(v1)
v2=Vector(1,2,9)
print(v2)
print(v1+v2)
print(type(v1+v2))'''

'''class Animal:
    def __init__(self,name,species):
        self.name=name
        self.apecies=species
    def make_sound(self):
        print("Sound made by the animal")

class Dog(Animal):
    def __init__(self,name,breed):
        Animal.__init__(self,name,species="Dog")
        self.breed=breed
    def make_sound(self):
        print("Bark!")
d=Dog("Dog","Doggerman")
d.make_sound()
a=Animal("Dog","Dog")
a.make_sound()'''



        