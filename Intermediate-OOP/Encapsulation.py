class Student:
    def __init__(self, name, marks):
        self._name = name           # protected
        self.__marks = marks        # private

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks! Enter value between 0-100.")


s = Student("Amit", 85)
print("Initial Marks:", s.get_marks())

s.set_marks(95)
print("Updated Marks:", s.get_marks())

s.set_marks(150)   # Invalid
