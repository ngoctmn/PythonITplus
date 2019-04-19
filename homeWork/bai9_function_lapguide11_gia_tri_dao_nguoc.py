def reverse():
     a = list(input('nhập vào chuỗi: '))
     i = 0
     while a[i].isnumeric() == True:
         a = list(input('nhập vào chuỗi: '))
         i+=1
     else:
         a = a.reverse()
     print(a)


reverse()
