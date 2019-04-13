# # So Amstrong
#
# for i in range (100, 1000):
#     x = 0
#     for j in str(i):
#         x += int(j) ** 3
#
#     if x == i:
#         print(i)


# Rut tien ngan hang
T = int(input('Nhap so tien '))

listMoney = [100, 20, 5, 1]

tongSoTien = 0

for i in listMoney:
    tongSoTien += T // i
    print('So to tien menh gia ', i, 'la ',T // i)
    T = T % i

print('Tong so to tien la', tongSoTien)

# So Amstrong
# # for i in range (100, 1000):
# a = i //100
# b = (1-a*100)//10
# c = i-a*100 -b*10
# if i ==a**3+b**3+c**3:
#     print(i)
# else:
#     pass
#

# Bai 2
T = int(input('Nhap'))












# # Bai 3
# l = [int(s) for s in input ('Nhap: ').split(',')]
#
# sum = 0
# mul = 1
#
# for i in l:
#     if i % 2 == 0:
#         sum += i
#     else:
#         mul *= i
# print('Tong &s, tich &s' &(sum,mul))


# Bai 4
n = int(input('Nhap n:   ')

l = []
sum = 0

for i in range (2, n):
    for j in range (i//2+1, 1):
        if i % j == 0:
            sum += j
    if sum == i:
        l. append(i)
    sum = 0

print('So hoan hao < ',n, ':', l)