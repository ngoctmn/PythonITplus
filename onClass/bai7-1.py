class Person:
    def __init__(self, n, a, ad):
        self.name = n
        self.age = a
        self.address = ad


    def run(self):
        print('Running')

    def get_name(self):
        return self.name

p = Person('Ngoc', 27, 'Hanoi')
print(p.get_name())
print(p.age)
print(p.address)

g = Person('Huong',26, 'Hanoi')
print(g.get_name())
print(g.age)
print(g.address)

print(getattr(g, 'name'))