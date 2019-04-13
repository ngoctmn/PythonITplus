class Xe:
    def __init__(self, bs, lx, sg):
        self.bien_so = bs
        self.lai_xe = lx
        self.so_ghe = sg

    def run(self):
        print('running...')


class XeBus(Xe):
    def __init__(self, bs, lx, sg, mt, cd):
        super().__init__(bs, lx, sg)
        self.ma_tuyen = mt
        self.cung_duong = cd


class XeTaxi(Xe):
    def __init__(self, bs, lx, sg, h, gc):
        super().__init__(bs, lx, sg)
        self.hang = h
        self.gia_cuoc = gc


class XeKhach(Xe):
    def __init__(self, bs, lx, sg, dd, gv):
        super().__init__(bs, lx, sg)
        self.diem_den = dd
        self.gia_ve = gv


bus = XeBus(bs='30A1111',lx='Lai xe Bus',sg='50',mt=29,cd='Nhổn - Giáp Bát')
print(bus.bien_so)
print(bus.lai_xe)
print(bus.so_ghe)
print(bus.ma_tuyen)
print(bus.cung_duong)
bus.run()
