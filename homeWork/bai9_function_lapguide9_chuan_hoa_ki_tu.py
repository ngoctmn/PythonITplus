def chuan_hoa_ki_tu(a):
    "chuẩn hóa một xâu nhập vào, không có 2 dấu cách đứng cạnh nhau, chữ cái đầu của các từ đều được viết hoa"
    a = str(a).title()
    return ' '.join(a.split())


print(chuan_hoa_ki_tu('trAn     mINH     ngoc'))
