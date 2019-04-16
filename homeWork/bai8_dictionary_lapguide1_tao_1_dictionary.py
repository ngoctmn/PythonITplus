num = int(input('Nhap so num = '))
_dict = dict()

for i in range(1, num + 1):
    # _dict.update({i: i * i})
    _dict[i] = i * i
print(_dict)