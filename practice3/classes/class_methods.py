class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Salem, menin atym", self.name)

s1 = Student("Ali")
s1.greet()