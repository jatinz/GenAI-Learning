
class Shape:
    def area(self):
        return "Area of a shape"

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width

class Circle(Shape):
    def __init__(self,r):
        self.r = r

    def area(self):
        return 3.14*self.r*self.r


def calc_area(Shape):
    print(f"Area = {Shape.area()}")


rectangle = Rectangle(4,5)
circle = Circle(3)

calc_area(rectangle)
calc_area(circle)