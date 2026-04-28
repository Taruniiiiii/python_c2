"""#inheritance(single)
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
##
class MusicalInstrument:
    def __init__(self, name, instrument_type):
        self.name = name
        self.instrument_type = instrument_type

    def play(self):
        print(f'The {self.name} is fun to play!')

    def get_fact(self):
        return f'The {self.name} is part of the {self.instrument_type} family of instruments.'


instrument_1 = MusicalInstrument('Oboe', 'woodwind')
instrument_2 = MusicalInstrument('Trumpet', 'brass')

instrument_1.play()
print(instrument_1.get_fact())

##class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name.upper()} says woof woof! I'm {self.age} years old!")

dog_1 = Dog("Jack", 3)
dog_2 = Dog("Thatcher", 5)

# Call the bark method
dog_1.bark()  # JACK says woof woof! I'm 3 years old!
dog_2.bark()  

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

##
#1
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print(self.name,self.marks)
s=Student("taruni",90)
s.display()  
##
#2
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def show_details(self):
        print(self.name,self.salary)
e=Employee("sohan",60)
e.show_details()
        
#3
class Bank:
    
    def __init__(self,balance):
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        
    def withdrawal(self,amount):
        if amount<=self.balance:
            self.balance-=amount
        else:
            print("insufficient balance")
    def show_balance(self):
        print(self.balance,"is your balance amt")
b=Bank(3000)
b.deposit(1000)
b.withdrawal(500)
b.show_balance()


#3
class Vehicle:
    def start(self):
        print("Vehicle starts")

class Car(Vehicle):
    def drive(self):
        print("Car is driving")


# Usage
c = Car()
c.start()
c.drive()   

#
class Animal:
    
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    
    def sound(self):
        print("Dog bark")

d = Dog()
d.sound()

        
        
class Student:
    
    def _init_(self, name):
        self.name = name

s = Student("Ravi")
print(s.name)

 #inheritance
 
class Vehicle:
    def start(self):
        print("vehicle started")
class car(Vehicle):
    def drive(self):
        print("vehicle deives")
v=Vehicle()
c=car()
c.start()
c.drive()
"""

#polymorphism
class Animal():
    def sound(self):
        print("any sound")
class dog(Animal):
    def sound(self):
        print("bow")
class cat(Animal):
    def sound(self):
        print("meow")
a=Animal()
d=dog()
c=cat()
a.sound()
d.sound()
c.sound()
#student management
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def grade(self):
        if self.marks>50:
            print("pass")
        else:
            print("fail")
s=Student("tar",90)
s.grade()


#employee ecosystem
class Employee:
    def work(self):
        print("working rn")
class Developer(Employee):
    def work(self):
        print("developer working")
class Manager(Employee):
    def work(self):
        print("Manager working")
e=Employee()
d=Developer()
m=Manager()
e.work()
d.work()
m.work()

#shape ex
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def area(self):
        print("Area of circle")
class Rectangle(Shape):
    def area(self):
        print("area of rectangle")
c=Circle()
r=Rectangle()
c.area()
r.area()

#constructor
class Employee:
    def __init__(self,name,department,salary):
        self.name=name
        self.department=department
        self.salary=salary
    def Show_details(self):
        print("name:",self.name)
        print("dept:",self.department)
        print("salary:",self.salary)
e=Employee("Tar","PR",5000)
e.Show_details()

#Encapsulation
class BankAccount():
    def __init__(self,balance):
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if amount<self.balance:
            self.balance-=amount
        else:
            print("insufficient balance")
    def check_balance(self):
        print(self.balance,"is your remaining bal")
        
b=BankAccount(5000)
b.deposit(50)
b.withdraw(100)
b.check_balance()



#employee ecosystem
class Employee:
    def work(self):
        print("working rn")
class Developer(Employee):
    def work(self):
        print("developer working")
class Manager(Employee):
    def work(self):
        print("Manager working")
e=Employee()
d=Developer()
m=Manager()
e.work()
d.work()
m.work()
#encapsulation

class Student:
    def __init__(self, marks):
        self.__marks = marks   # private

    def set_marks(self, marks):
        if marks < 0:
            print("negative marks")
        else:
            self.__marks = marks   # update value

    def get_marks(self):
        return self.__marks


s = Student(0)

s.set_marks(50)
print(s.get_marks())   

s.set_marks(100)
print(s.get_marks()) 

##polymorphism
class calculator:
    def add(self,a,b):
        print(a+b)
s=calculator()
s.add(3,4)

##abstraction
from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


# Child class
class Car(Vehicle):
    def start(self):
        print("Car starts")
class Bike(Vehicle):
    def start(self):
        print("Bike starts")


# Objects
c = Car()
b = Bike()

c.start()
b.start()