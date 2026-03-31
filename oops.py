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
#multilevel(1 parent multiple child)hierarchial
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
