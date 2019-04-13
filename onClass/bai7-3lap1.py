class HinhChuNhat:
    def __init__(self, chieu_dai, chieu_rong):
        self.d = chieu_dai
        self.r = chieu_rong

    def get_d(self):
        return self.d

    def get_r(self):
        return self.r

    def set_d(self, chieu_dai):
        self.d = chieu_dai

    def set_r(self, chieu_rong):
        self.r = chieu_rong

    def area(self):
        return self.d * self.r

    def perimeter(self):
        return 2 * self.d * self.r

dt = HinhChuNhat(3, 4)
print(dt.area(2, 5))
print(dt.perimeter(1, 4))

print()