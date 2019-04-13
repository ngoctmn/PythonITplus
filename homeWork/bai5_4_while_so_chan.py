n = int(input('Nhap vao so n =  '))
sum = 0
i = 0

while (i < n):
    if (i % 2 == 0):
        sum += i
    i += 1
print(sum)