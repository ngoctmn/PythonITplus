# Tim uoc so chung lon nhat

a = int(input('Nhap vao so a = '))
b = int(input('Nhap vao so b = '))

while a != b:
    if a > b:
        a -= b
    else:
        b -= a

print('Uoc so chung nho nhat:  ', a)

