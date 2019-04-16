msg = input('Nhap vao mot chuoi: ')

digit = 0
alpha = 0
for i in msg:
    if i.isdigit():
        digit += 1
    elif i.isalpha():
        alpha += 1
_dict = {'alpha':alpha, 'digit':digit}
print(_dict)