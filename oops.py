#inheritance
class manager:
    def show(self):
        print("im a manager")
class employee(manager):
    def intro(self):
        print("im an employee")
e=employee()
e.show()
e.intro()