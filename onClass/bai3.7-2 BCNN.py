# Boi so chung nho nhat
a = int(input('Nhap vao so a =  '))
b = int(input('Nhap vao so b =  '))

if (a > b):
    greater = a
else:
    greater = b

while True:
    if (greater % a == 0) and (greater % b == 0):
        print(greater)
        break
    greater += 1


