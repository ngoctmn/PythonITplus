n = int(input('Nhap vao so n =  '))
sum = 0

for i in range (1, n):
    if i % 2 == 0:
        sum += i
print('Tong = ',sum)
