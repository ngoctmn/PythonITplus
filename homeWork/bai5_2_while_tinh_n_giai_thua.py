n = int(input('Nhap vao so nguyen duong n =  '))

giaiThua = 1
i = 1

if (n == 0):
    print('n! = ', 1)
else:
    while (1 <= i) and (i <= n):
        giaiThua *= i
        i += 1
    print(giaiThua)
