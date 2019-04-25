def tinh_so_doan_tang(inlist):
    doan_tang = []
    do_dai_doan_tang = []
    so_doan_tang = 0
    for i in range (len(inlist) - 2):
        if (inlist[i + 1]) > inlist[i]:
            doan_tang.append(inlist[i])
        else:
            so_doan_tang += 1
            do_dai_doan_tang.append(len(doan_tang))
            doan_tang.clear()

    if inlist[len(inlist) - 1] > inlist[len(inlist) - 2]:
        do_dai_doan_tang[-1] += 1

    k = max(do_dai_doan_tang)

    print('Số đoạn tăng là: ', so_doan_tang)
    print('Đoạn tăng thứ ', do_dai_doan_tang.index(k), ' có độ dài lớn nhất la', k)


tinh_so_doan_tang([1, 2, 3, 2, 3, 4, 2, 3, 4, 5])


# CON BAI 7, 10, 11