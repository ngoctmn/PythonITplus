from bai14_thua_ke_giao_trinh_1 import Person

# Lớp Student (Sinh viên) mở rộng (extends) từ lớp Person.
class Student (Person):
    def __init__(self, name, age, university):
        # Gọi tới constructor của lớp cha (Person) để gán giá trị vào thuộc tính 'name' của lớp cha.
        super().__init__(name)
        self.age = age
        self.university = university

# Ghi đè (override) phương thức cùng tên của lớp cha.
    def show_info(self):
        print ("Name: " + self.name)
        print (" Age: " + str(self.age))
        print (" University: " + self.university)


# Khởi tạo đối tượng Student
student = Student("Nguyen Van A", 18, "DHQG Ha Noi")

# Gọi tới hàm show_info của lớp Student
student.show_info()
