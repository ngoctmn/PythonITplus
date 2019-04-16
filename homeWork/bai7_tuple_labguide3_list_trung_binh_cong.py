l = [int(s) for s in input('Nhap: ').split(',')]

sum = 0
multiply = 1

for i in l:
    if i % 2 == 0:
        sum += i
    else:
        multiply *= i

print('Tong %s, tich %s' %(sum,multiply))


total = 0
for j in l:
    total += j

print('Trung binh cong = ', total/len(l))