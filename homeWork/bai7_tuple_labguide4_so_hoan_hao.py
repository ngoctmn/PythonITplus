n = int(input('Nhap n = '))

l = []
sum = 0

for i in range(2, n):
    for j in range(1, i // 2 + 1, 1):
        if i % j == 0:
            sum += j
    if sum == i:
        l. append(i)
    sum = 0

print('So hoan hao < ',n, ':', l)