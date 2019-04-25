from bai14_thua_ke_giao_trinh_3_da_ke_thua import Film
from bai14_thua_ke_giao_trinh_b1 import Animal


class Mouse(Animal, Film):
    def __init__(self, name, age, weight, author, type):
        Animal.__init__(self, name, age, weight)
        Film.__init__(self, author, type)

    def show_info(self):
        print(f'Name: {self.name}, Age: {self.age}, Weight: {self.weight}, Author: {self.author}, Type: {self.type}')


mouse2 = Mouse(name='Mickey', age=10, weight=1, author='Walt Disney', type='cartoon')
mouse2.show_info()
