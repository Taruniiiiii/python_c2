#inheritance(single)
class manager:
    def show(self):
        print("im a manager")
class employee(manager):
    def intro(self):
        print("im an employee")
e=employee()
e.show()
e.intro()
#multiple inheritance(multiple parent and 1 child)
class A:
    def aa(self):
        print("class A")
class B:
    def bb(self):
        print("class B")
class C(A,B):
    def cc(self):
        print("class C")
c=C()
c.aa()
c.bb()
#multilevel(parentA parent b)hierarchial(grand parent parent child)
class A:
    def aa(self):
        print("class A")
class B(A):
    def bb(self):
        print("class B")
class C(B):
    def cc(self):
        print("class C")
b=B()
b.bb()
#hierarchial(1 parent, mul child)
class A:
    def aa(self):
        print("class A")
    def kk(self):
        print("class k")
class B(A):
    def bb(self):
        print("class B")
class C(A):
    def cc(self):
        print("class C")
b=B()
c=C()
b.aa()
c.kk()

#1
class vehicle:
    def Start(self):
        print("vehicle starts")
class car:
    def drive(self):
        print("drive the car")
v=vehicle()
c=car()
v.Start()
c.drive()
        
#super keyword(if child class uses constructor  it cannot access parent class
# so we use super class to access parent class)
class Car:
    def __init__(self,name):
        self.name=name
class red_c(Car):
    def __init__(self, color ,name):
        super().__init__(name)
        self.color=color

#. Person → Student

class person:
    def show_name(self,name):
        print("hi my name is ",name)
class student(person):#here inherit
    def show_marks(self,marks):
        print("marks of the student is",marks)
p=person()
s=student()
p.show_name("tar")
s.show_marks("10")

#using super keyword
class person:
    def __init__(self,name):
        self.name=name
class employee(person):
    def __init__(self,name,salary):
        super().__init__(name)
        self.salary=salary
    def display(self):
        print("Name",self.name)
        print("Salary",self.salary)
e=employee("taruni",5000)
e.display()    

##leet
class RecentCounter:
    def __init__(self):
        self.records = []
        self.start = 0

    def ping(self, t: int) -> int:
        self.records.append(t)
        while self.records[self.start] < t - 3000:
            self.start += 1
        return len(self.records) - self.start
    

a = 6
b = 3
a /= 2 * b
print(a)
from abc import ABC, abstractmethod


class car(ABC):
    @abstractmethod
    def stop(self):
        print("Hi")
        

class c1():
    def stop(self):
        print("car started")

"""        
class c2():
    pass
    
    def stop(self):
        print("car stoped")
    """

from abc import ABC, abstractmethod
import math

# Abstract class
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


# Circle class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


# Rectangle class
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Usage
c = Circle(5)
r = Rectangle(4, 6)

print("Circle Area:", c.area())
print("Circle Perimeter:", c.perimeter())

print("Rectangle Area:", r.area())
print("Rectangle Perimeter:", r.perimeter())