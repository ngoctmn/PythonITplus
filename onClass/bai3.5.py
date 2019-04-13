# Check n co phai so nguyen to khong

number = int(input('Nhap vao so nguyen duong =  '))

demNeuChiaHet = 0

for soBiChia in range (2, number//2+1):
    if number % soBiChia == 0:
        demNeuChiaHet += 1

if demNeuChiaHet == 0:
    print(number, ' la so nguyen to.')
else:
    print(number, ' khong phai la so nguyen to')



