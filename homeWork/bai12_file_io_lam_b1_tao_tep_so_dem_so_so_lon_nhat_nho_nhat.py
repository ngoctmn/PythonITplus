_n = input('Nhap danh sach cac so tu ban phim: ')

# Dua cac so thanh 1 danh sach
_list = _n.split(',')

# Tao file file.txt
_file = open('numbers.txt', 'w+')
# Ghi danh sach cac so vua nhap vao tep
_file.write(_n)
# So luong cac so trong tep
_len = len(_list)
print('Len: ', _len)
_file.write('Len: ' + str(_len))
# So lon nhat
_max = max(_list)
print('Max: ', _max)
_file.write('Max: ' + _max)
# So nho nhat
_min = min(_list)
print('Min: ', _min)
_file.write('Min: ' + _min)

_file.close()
