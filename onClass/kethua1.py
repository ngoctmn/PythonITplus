class ChuyenXe:

    TONG_DOANH_THU = 0

    def __init__(self, mc, lx, sx, dt):
        self.ma_chuyen = mc
        self.lai_xe = lx
        self.so_xe = sx
        self.doanh_thu = dt
        ChuyenXe.TONG_DOANH_THU +=dt


    def info(self):
        d = dict()
        d['noi_den'] = self.__noi_den
        d['so_ngay'] = self.__so_ngay
        return d


class ChuyenXeNgoaiThanh(ChuyenXe):
    def __init__(self, mc, lx, sx, dt, nd, sn):
        super().__init__(mc, lx, sx, dt)
        self.ngay_den = nd
        self.so_ngay = sn


class ChuyenXeNoiThanh(ChuyenXe):
    def __init__(self, mc, lx, sx, dt, sk, st):
        super().__init__(mc, lx, sx, dt)
        self.so_km = sk
        self.so_tuyen = st


n = int(print('Nhap so chuyen xe noi thanh: '))
for i in range (1,n+1):
    print('Thong tin xe so: ',i)
    print()
m = int(print('Nhap so chuyen xe ngoai thanh: '))


