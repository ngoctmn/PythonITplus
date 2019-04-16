#  Cach 1:
result = []
for i in range (100, 1000):
    tong = 0
    for j in str(i):
        tong += int(j) ** 3

    if tong == i:
        result.append(i)
print(result)

# Cach 2:
# result = []
# for i in range (100, 1000):
#     a = i//100
#     b = (i - a * 100)//10
#     c = i - a * 100 - b * 10
#     if i == a ** 3 + b ** 3 + c ** 3:
#         result.append(i)
# print(result)
