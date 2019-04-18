_list = [1, 3, 5, 7, 9]
_tuple = (1, 3, 5, 7, 9)

def analysis(a):
    total = 0
    nho_hon_avg = []
    lon_hon_avg = []
    for i in a:
        total += i
        avg = total / len(a)

    for j in a:
        if j > avg:
            lon_hon_avg.append(j)
        elif j < avg:
            nho_hon_avg.append(j)
    print('max = ', max(a))
    print('min = ', min(a))
    print('average = ', avg)
    print(lon_hon_avg)
    print(nho_hon_avg)
    # return lon_hon_avg, nho_hon_avg


analysis(_list)
analysis(_tuple)
