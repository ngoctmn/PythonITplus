n = int(input('Nhap vao so nguyen < 20  '))
if n < 20:
    if (n % 5 == 0) or (n % 7 == 0):
        print('Cac so chia het cho 5 hoac chia het cho 7 la  ',n)
else:
    print('So nhap > 20')