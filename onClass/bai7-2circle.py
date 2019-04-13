import math

class Circle:

    def __init__(self, r):
        self.R = r

    def get_R(self):
        return self.R

    def set_R(self, r):
        self.R = r

    def area(self):
        return math.pi * self.R * self.R

    def piremeter(self):
        return 2 * math.pi * self.R

#
c1 = Circle(2)
print(c1.area())
print(c1.piremeter())
c1.set_R(8)
print(c1.area())

#
c2 = Circle(8)
print(c2.area())