list = ['abc', 'xyz', 'aba', '1221', 'ii', 'ii2', '5yhy5']
n = int(input('Nhap gia tri n'))
count = 0

for i in list:
    if len(i) >= n and i[0] == i[len(i) - 1]:
        count += 1

print(count)
