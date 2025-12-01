class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def show(self):
        print("Name:", self.name, "| Roll:", self.roll)

# Creating objects
s1 = Student("Tahir", 101)
s2 = Student("Amit", 102)

s1.show()
s2.show()
