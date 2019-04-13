list = ['abc', 'de', 'a', 'defg']

n = int(input('Nhap so n =  '))


i = 0
resultList = []


while i < len(list):
    itemList = list[i]
    if len(itemList) > n:
        resultList.append(itemList)
    i += 1

print(resultList)
