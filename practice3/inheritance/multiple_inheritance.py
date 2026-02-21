class Father:
    def skill1(self):
        print("Father skill")

class Mother:
    def skill2(self):
        print("Mother skill")

class Child(Father, Mother):
    pass

c = Child()
c.skill1()
c.skill2()