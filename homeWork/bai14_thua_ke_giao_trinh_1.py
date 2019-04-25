class Person:
    # Hàm tạo của lớp Person
    def __init__(self, name):
        # Lớp Person có 1 thuộc tính (attribute): 'name'.
        self.name = name

    # Phương thức (method):
    def show_info(self):
        print("This‘s " + self.name)

    # Phương thức (method):
    def move(self):
        print("moving ...")


class Student (Person):
    def __init__(self, name, age, university):
        # Gọi tới constructor của lớp cha (Person) để gán giá trị vào thuộc tính 'name' của lớp cha.
        super().__init__(name)
        self.age = age
        self.university = university


# Khởi tạo đối tượng Student
student = Student("Nguyen Van A", 18, "DHQG Ha Noi")

# Gọi tới hàm showInfo của lớp cha (Person) qua đối tượng Student
student.show_info()
