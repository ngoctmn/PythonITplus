yearOfBirth = int(input("Nhap vao nam sinh = "))

import time
currentYear = time.localtime()
currentYear = currentYear[0]
age = currentYear - yearOfBirth
print(age)