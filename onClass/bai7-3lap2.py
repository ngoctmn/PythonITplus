class HocVien:
    def __init__(self, m, t, dt, dl, dh):
        self.masv = m
        self.ten = t
        self.toan = float(dt)
        self.ly = float(dl)
        self.hoa = float(dh)

    def get_masv(self):
        return self.masv

    def set_masv(self, m):
        self.masv = m

    def diem_tb(self):
        d = (self.toan + self.ly + self.hoa) / 3
        return round(d, 2)

    def to_string(self):
        s = 'Mã: ' + self.masv + ', Tên: ' + self.ten + ', Toán: ' + str(self.toan) + \
            ', Lý: ' + str(self.ly) + ', Hóa: ' + str(self.hoa) + ', Điểm TB: ' + str(self.diem_tb())

        return s

    def save_file(self, file_path):
        try:
            with open(file_path, 'a+', encoding='utf-8') as f:
                f.write(self.to_string() + '\n')

        except Exception as e:
            print('Error: ', e)
        finally:
            f.close()


hv1 = HocVien('001', 'Học viên 1', 9, 8, 8)
hv2 = HocVien(input('Mã: '), input('Tên: '), input('Toán: '), input('Lý: '), input('Hóa: '))

ds = list()

# Print list of student
ds.append(hv1.to_string())
ds.append(hv2.to_string())
count = 1
for i in ds:
    hv = i.split(',')
    print('# Thông tin học viên thứ %s là: ' % (count))
    count += 1
    for j in hv:
        print(j)
# Save info to file
hv1.save_file('hocvien.txt')
hv2.save_file('hocvien.txt')