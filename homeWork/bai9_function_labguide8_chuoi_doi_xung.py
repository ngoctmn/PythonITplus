def doi_xung(chuoi):
    a = len(chuoi) // 2
    for i in range(a):
        if chuoi[i] == chuoi[-1 - i]:
            return 'Chuoi doi xung'
        else:
            print('Chuoi khong doi xung')
            break


chuoi = str(input('Nhap vao mot chuoi: '))
print(doi_xung(chuoi))
