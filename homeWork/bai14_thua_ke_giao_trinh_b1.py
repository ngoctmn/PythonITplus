class Animal:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def show_info(self):
        print('Name: ', self.name, ' - Age: ', self.age, ' - Weight: ', self.weight)


class Mouse(Animal):
    def __init__(self, name, age, weight, country, year):
        super().__init__(name, age, weight)
        # Bai tap override tiep
        self.country = country
        self.year = year

    def show_info(self):
        print('Name: ', self.name, ' - Country: ', self.country, ' - Year: ', self.year)


chuot = Mouse('Hoa', 28, 15, 'Viet Nam', 2019)
chuot.show_info()
