class TaiKhoan:
    LAI_SUAT = 0.035
    PHI = 0.33
    def __init__(self, i, n, s = 50):
        self.so_tai_khoan = i
        self.ten_tai_khoan = n
        self.so_du = s

    def rut_tien(self, so_tien):
        if so_tien > 0 and self.so_du >= so_tien + 50 + TaiKhoan.PHI:
            self.so_du -= so_tien
        else:
            print('Số tiền rút không hợp lệ.')
            return None

    def nap_tien(self, so_tien):
        if so_tien > 0:
            self.so_du += so_tien
        else:
            print('Số tiền nạp không hợp lệ.')
            return None

    def to_string(self):
        d = dict()
        d['so_tk'] = self.so_tai_khoan
        d['ten_tk'] = self.ten_tai_khoan
        d['so_du'] = self.so_du

    # Cách 1: Truyền vào Object
    def chuyen_khoan(self, obj, so_tien):
        self.rut_tien(so_tien)
        obj.nap_tien(so_tien)

    # Cách 2: Truyền vào function
    def chuyen_khoan_2(self, func, so_tien):
        self.rut_tien((so_tien))
        func(so_tien)

acc1 = TaiKhoan('001', 'Người gửi', 200)
print(acc1.to_string())
acc2 = TaiKhoan('002', 'Người nhận')
print(acc2.to_string())

print('')