class Person:
    # default value: age & gender.
    def __init__ (self, name, age=1, gender="Male"):
        self.name = name
        self.age = age
        self.gender = gender

    def show_info(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)


# Create Person object.
aimee = Person("Aimee", 21, "Female")
aimee.show_info()
print(" --------------- ")

# age, gender default.
alice = Person( "Alice" )
alice.show_info()
print(" --------------- ")

# gender default.
tran = Person("Tran", 37)
tran.show_info()
