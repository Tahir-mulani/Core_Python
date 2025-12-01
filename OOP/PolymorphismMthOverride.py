class Shape:
    def area(self):
        print("Area not defined")

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        print("Area of Circle:", 3.14 * self.r * self.r)

c = Circle(5)
c.area()
