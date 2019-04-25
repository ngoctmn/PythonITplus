_list = [{'masv': 'Masv01', 'ten': 'An', 'diem': 8.1}, {'masv': 'Masv02', 'ten': 'Binh', 'diem': 7.3},
         {'masv': 'Masv03', 'ten': 'Minh', 'diem': 9.6}]




file = open('sinhvien2.txt', 'r+')

_new = sorted(_list, key=lambda k: k['diem'], reverse=True)
print('Danh sach sau khi sap xep theo diem: ', _new)
file.seek(0)
file.truncate()
for i in range(len(_new)):
    file.writelines(f'{str(i + 1)}. {_new[i]}')

file.close()