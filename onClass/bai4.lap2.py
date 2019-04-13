# # List bai 1
# n = input('Nhap 1 day so:  ')
# list = n.split(',')
# sum = 0
# multiple = 1
# total = 0
#
# for i in list:
#     total += int(i)
#     if int(i) % 2 == 0:
#         sum += int(i)
#     else:
#         multiple *= int(i)
#
# print('Tong so chan la ', sum)
# print('Tich so le la ', multiple)
# print('Trung binh cong la ', total/len(list))


# List bai 2: So hoan hao
n = int(input('Nhap vao 1 so: '))
sum = 0

for i in range (1, n // 2 + 1):
    if n % i == 0:
        sum += i

if sum == n:
    print('n la so hoan hao')
else:
    print('n khong phai so hoan hao')









# # List bai 4
# list = input('Nhap vao mot list').split(',')
#
# for i in range (0, len(list):


