def tinh_so_doan_tang(inlist):
    doan_tang = []
    do_dai_doan_tang = []
    so_doan_tang = 0
    for i in inlist:
        if (inlist[inlist.index(i) + 1]) > i:
            doan_tang.append(i)
        else:
            so_doan_tang += 1
            do_dai_doan_tang.append(len(doan_tang))
            doan_tang.clear()
    k = max(do_dai_doan_tang)
    print('Số đoạn tăng là: ', so_doan_tang)
    print('Đoạn tăng thứ ', do_dai_doan_tang.index(k), ' có độ dài lớn nhất la', k)


tinh_so_doan_tang([1, 2, 3, 2, 3, 4, 2, 3, 4, 5])
