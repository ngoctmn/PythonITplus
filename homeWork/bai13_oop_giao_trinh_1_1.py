class Person:

    def __init__(self, n, a, ad):
        self.name = n
        self.age = a
        self.address = ad

    def run(self):
        print('Running...')

    def get_name(self):
        return self.name

# p = Person('Khánh', 19, 'Hà Nội')
#
# print(p.get_name())
# print(p.age)
# print(p.address)

p2 = Person('Tài', 21, 'HCM')
print(p2.get_name())
#
print(p2.age)
print(getattr(p2,'age'))
#
print(hasattr(p2,'age')) # True
print(hasattr(p2,'email')) # False
# delattr(p2,'address')
print(p2.address)