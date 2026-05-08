class Circle:
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius
        def area(self):
            return self.radius ** 2 * Circle.pi
        
c = Circle(2.5)
print(c.area())