n = int(input('Nhap vao so nguyen n = '))
if  (n > 10):
    print('So nhap vao phai < 10')
else:
    if (n % 2 == 0):
        for i in range (2, n + 1, 2):
            print('Cac so chan n =  ', i)

    else:
        for j in range (2, n, 2):
            print('Cac so chan n =  ', j)
