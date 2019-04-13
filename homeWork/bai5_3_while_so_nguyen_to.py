n = int(input('Nhap vao so nguyen duong n =  '))

demChiaHet = 0
i = 2
while (i <= n//2):
    if n % i == 0:
        demChiaHet += 1
    i += 1

if demChiaHet == 0:
    print(n, 'la so nguyen to')
else:
    print(n, 'khong la so nguyen to')