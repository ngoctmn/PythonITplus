# Cach 1:
rut_tien = int(input('Nhap so tien '))
list_money = [100, 20, 5, 1]
tong_so_tien = 0

for i in list_money:
    tong_so_tien += rut_tien // i
    print('So to tien menh gia ', i, 'la ',rut_tien // i)
    rut_tien = rut_tien % i

print('Tong so to tien la', tong_so_tien)

# Cach 2:
# rut_tien = int(input('Nhap so tien '))
# list_money = [100, 20, 5, 1]
#
# t100 = rut_tien // 100
# t20 = (rut_tien - t100 * 100) // 20
# t5 = (rut_tien - t100 * 100 - t20 * 20) // 5
# t1 = (rut_tien - t100 * 100 - t20 * 20 - t5 * 5) // 1
#
# print(f't100 = {t100}, t20 = {t20}, t5 = {t5}, t1 = {t1}')
