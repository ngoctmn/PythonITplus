_list = ['abc', 'xyz', 'aba', '1221', 'ii', 'ii2', '5yhy5']
n = int(input('Nhap vao so n = '))
result = []

for i in _list:
    if len(i) > n and i[0] == i[len(i) - 1]:
        result.append(i)

print(result)
print(len(result))


# count = 0
# for j in _list:
#     if len(j) > n and i[0] == i[-1]:
#         count += 1
#         print(i)
#
# print(count)
