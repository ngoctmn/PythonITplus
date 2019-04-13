number = int(input("Nhap vao so nguyen duong = "))


if (number % 2 == 0) and (number % 3 == 0):
    print("so chia het cho ca 2 va 3")
elif  number % 2 == 0:
    print("So chia het cho 2")
elif number % 3 == 0:
    print("So chia het cho 3")
else:
    print("So nay khong chia het cho 2 va 3")
