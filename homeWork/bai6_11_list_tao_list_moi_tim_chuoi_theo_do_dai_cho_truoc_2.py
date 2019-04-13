list = ['abc', 'de', 'a', 'defg']

n = int(input('Nhap so n =  '))
result_list = []


for i in list:
    if len(i) > n:
        result_list.append(i)
print('result list', result_list)