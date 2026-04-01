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
c.bb()"""
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
#hierarchial(parent)
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
        