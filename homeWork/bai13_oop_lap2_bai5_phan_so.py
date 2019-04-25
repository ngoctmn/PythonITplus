class Rational:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def print(self):
        print(self.numerator, '/', self.denominator)

    def to_float(self):
        return self.numerator/self.denominator

    def reduce(self):
        ucln = 0
        for i in range(1, min(self.numerator, self.denominator) + 1):
            if self.numerator % i == self.denominator % i == 0:
                ucln = i
        # self.numerator = int(self.numerator/ucln)
        # self.denominator = int(self.denominator/ucln)
        return Rational(int(self.numerator/ucln), int(self.denominator/ucln))

    def reciprocal(self):
        return Rational(self.denominator, self.numerator)

    def minus(self, obj2):
        a = self.reduce()
        b = obj2.reduce()
        ucln = 0
        for i in range(1, min(a.denominator, b.denominator) + 1):
            if a.denominator % i == b.denominator % i == 0:
                ucln = i
        bcnn = a.denominator * b.denominator / ucln
        return Rational(int(a.numerator*b.denominator/ucln - b.numerator*a.denominator/ucln), int(bcnn))

    def divide_dummy(self, obj2):
        return Rational(self.numerator*obj2.denominator, self.denominator*obj2.numerator)

    def divide(self, obj2):
        return self.divide_dummy(obj2).reduce()

    def compare(self, obj2):
        tolerance = 0.001
        if self.minus(obj2).to_float() > tolerance:
            print(self.numerator, '/', self.denominator, ' is greater than ', obj2.numerator, '/', obj2.denominator)
        else:
            print(self.numerator, '/', self.denominator, ' is smaller than ', obj2.numerator, '/', obj2.denominator)


a = Rational(10, 12)
b = Rational(3, 4)
print('Toi gian phan so a')
a.reduce().print()
print('Nghich dao phan so a')
a.reciprocal().print()

print('Phan so a tru phan so b')
a.minus(b).print()
print('Phan so a chia phan so b')
a.divide(b).print()
print('So sanh phan so a va b')
a.compare(b)