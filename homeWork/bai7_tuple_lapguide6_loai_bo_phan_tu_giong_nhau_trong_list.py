_list = [11, 14, 16, 16, 18, 19, 16, 11, 11, 14]
trung = list()
khong_trung = list()

for i in _list:
    if _list.count(i) > 1 and i not in trung:
        trung.append(i)
print(trung)


for j in _list:
    if _list.count(j) == 1:
        khong_trung.append(j)
print(khong_trung)