class NhanVien:
    dem = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        NhanVien.dem += 1

    def hien_thi_so_luong(self):
        print("Tổng số nhân viên được tạo: %d" % NhanVien.dem)

    def hien_thi_nhan_vien(self):
        print("Tên: ", self.name, ", Lương: ", self.salary)


nhan_vien_dev = NhanVien('AnhDK', 1000)
nhan_vien_pm = NhanVien('LinhNM', 1200)
# Truy cap vao method cua Class
nhan_vien_dev.hien_thi_nhan_vien()
nhan_vien_pm.hien_thi_nhan_vien()
# Truy cap vao bien cua Class
print(nhan_vien_dev.dem)
# Truy cap vao thuoc tinh (attribute) cuar Class
print(nhan_vien_pm.name)
print(nhan_vien_dev.name)

#Attribute moi
nhan_vien_pm.age = 28
nhan_vien_pm.new_attribute= 'Không có'
#Cap nhat attribute
nhan_vien_pm.salary = 15000
print(nhan_vien_pm.hien_thi_nhan_vien())
print(nhan_vien_pm.age)
print(nhan_vien_pm.new_attribute)
#Xoa attribute cua íntance
del nhan_vien_pm.new_attribute

getattr(nhan_vien_pm, 'salary')
# getattr(nhan_vien_pm, 'test')

print(hasattr(nhan_vien_pm, 'salary'))
print(hasattr(nhan_vien_pm, 'test'))

setattr(nhan_vien_pm, 'salary', 5500)
print(nhan_vien_pm.salary)

delattr(nhan_vien_pm, 'age')