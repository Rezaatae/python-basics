class Circle():
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return (self.radius**2)*Circle.pi

    def setRadius(self, new_r):
        self.radius = new_r


myc = Circle(3)
print(myc.radius)
area = myc.area()
print(area)
myc.setRadius(100)
print(myc.area())