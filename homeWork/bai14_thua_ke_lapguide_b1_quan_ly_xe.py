class ChuyenXe:
    TONG_DOANH_THU = 0

    def __init__(self, mc, tx, sx, dt):
        self.ma_chuyen = mc
        self.tai_xe = tx
        self.so_xe = sx
        self.doanh_thu = dt
        ChuyenXe.TONG_DOANH_THU += dt

    def info(self):
        d = dict()
        d['ma_chuyen'] = self.ma_chuyen
        d['tai_xe'] = self.tai_xe
        d['so_xe'] = self.so_xe
        d['doanh_thu'] = self.doanh_thu
        return d


class XeNoiThanh(ChuyenXe):
    def __init__(self, mc, tx, sx, dt, st, km):
        super().__init__(mc, tx, sx, dt)
        self.__so_tuyen = st
        self.__so_km = km

    def info(self):
        d = ChuyenXe.info(self)
        d['so_tuyen'] = self.__so_tuyen
        d['so_km'] = self.__so_km

        return d


class XeNgoaiThanh(ChuyenXe):
    def __init__(self, mc, tx, sx, dt, nd, sn):
        super().__init__(mc, tx, sx, dt)
        self.__noi_den = nd
        self.__so_ngay = sn

    def info(self):
        d = ChuyenXe.info(self)
        d['noi_den'] = self.__noi_den
        d['so_ngay'] = self.__so_ngay

        return d


#
n = int(input('Nhập số chuyến xe nội thành: '))
dt_noi_thanh = 0
dt_ngoai_thanh = 0
for i in range(1, n + 1):
    print('Nhập thông tin xe số: ', i)
    mc = input('Mã chuyến: ')
    lx = input('Lái xe: ')
    sx = input('Số xe: ')
    dt = int(input('Doanh thu: '))
    st = input('Số tuyến: ')
    km = input('Số km: ')

    obj = XeNoiThanh(mc, lx, sx, dt, st, km)
    dt_noi_thanh += obj.doanh_thu

    print('Thông tin xe số: ', i)
    print(obj.info())
print('Tổng doanh thu nội thành: ', dt_noi_thanh)

#
m = int(input('Nhập số chuyến xe ngoại thành: '))
for i in range(1, m + 1):
    print('Nhập thông tin xe số: ', i)
    mc = input('Mã chuyến: ')
    lx = input('Lái xe: ')
    sx = input('Số xe: ')
    dt = int(input('Doanh thu: '))
    nd = input('Nơi đến: ')
    sn = input('Số ngày: ')

    obj = XeNgoaiThanh(mc, lx, sx, dt, nd, sn)
    dt_ngoai_thanh += obj.doanh_thu

    print('Thông tin xe số: ', i)
    print(obj.info())

print('Tổng doanh thu ngoại thành: ', dt_ngoai_thanh)
