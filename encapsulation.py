class Student:
    def __init__(self):
        self.__marks = 0   # private variable

    def set_marks(self, m):
        self.__marks = m   # setting value

    def get_marks(self):
        return self.__marks   # getting value


# usage
s = Student()

s.set_marks(90)
print(s.get_marks())