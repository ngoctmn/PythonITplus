class Rectangle:
    def __init__(self, h, w):
        self.hight = h
        self.weigh = w

    # setter, getter
    def get_hight(self):
        return self.hight

    def set_hight(self, h):
        self.hight = h

    def get_weigh(self):
        return self.weigh

    def set_weigh(self, w):
        self.weigh = w

    #
    def area(self):
        return self.weigh * self.hight

    def perimeter(self):
        return (self.hight + self.weigh) * 2

    def to_string(self):
        d = dict()
        d['hight'] = self.hight
        d['weigh'] = self.weigh
        d['area'] = self.area()
        d['perimeter'] = self.perimeter()
        return d

    def save_file(self, file_path):
        try:
            with open(file_path, 'w+') as f:
                f.write(str(self.to_string()))
        except Exception as e:
            print('Error: ', e)
        finally:
            f.close()


r = Rectangle(int(input('H: ')), int(input('W: ')))
print(r.to_string())
r.save_file('rec.txt')