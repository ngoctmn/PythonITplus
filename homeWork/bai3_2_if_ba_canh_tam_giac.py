number1 = int(input("Nhap vao so dau tien = "))
number2 = int(input("Nhap vao so thu hai = "))
number3 = int(input("Nhap vao so thu ba = "))
if  ((number1 ** 2 + number2 ** 2 == number3 ** 2) or
    (number2 ** 2 + number3 ** 2 == number1 ** 2) or
    (number3 ** 2 + number1 ** 2 == number2 ** 2)):
    print("Day la 3 canh tam giac vuong")
else:
    print("Day khong phai la ba canh tam giac vuong")