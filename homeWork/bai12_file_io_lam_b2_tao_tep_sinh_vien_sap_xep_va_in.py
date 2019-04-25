# Open file
_file = open('sinhvien.txt', 'r+')
# Ghi danh sach cac so vua nhap vao tep
_list = _file.readlines()
# Sap xep danh sach theo ABC
_new = sorted(_list)

# Xoa toan bo noi dung file da cho:
# Dua con tro ve dau file
_file.seek(0)
# Xoa toan bo file tu vi tri con tro
_file.truncate()

# Ghi lai danh sach vao file da co
for i in range(len(_new)):
    _file.writelines(str(i + 1) + ". " + _new[i])

_file.close()
