# Input Equation
print("Phuong trinh bac 2 co dang a*x*x + b*x + c = 0")
a = float(input('Nhap vao so a = '))
b = float(input('Nhap vao so b = '))
c = float(input('Nhap vao so c = '))
print("Phuong trinh can tinh la", a,'*x*x', '+', b, '*x', '+', c, '= 0')
print()


# Calculator
if  a == 0:
    if b == 0 and c == 0:
        print('Phuong trinh vo so nghiem.')

    elif b != 0:
        print('=> Phuong trinh co nghiem: ', (-c / b))

    elif (b == 0) and (c != 0):
        print('Phuong trinh vo nghiem')

    else:
        delta = (b ** 2) - (4 * a * c)

        if (delta < 0):
            print('=> delta = ', delta, '< 0')
            print("=> Phuong trinh vo nghiem")

        elif (delta == 0):
            print('=> delta = ', delta)
            x = (- (b) / (2 * a))
            print("=> Phuong trinh co nghiem la:  ", x)

        else:
            import math
            sqrt2OfDelta = math.sqrt(delta)
            x1 = ((-b + sqrt2OfDelta) / (2 * a))
            x2 = ((-b - sqrt2OfDelta) / (2 * a))
            print('=> delta =', delta, '> 0')
            print("=> Phuong trinh co nghiem x1 =  ", x1)
            print("=> Phuong trinh co nghiem x2 =  ", x2)

