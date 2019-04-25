# d=0
#
# try :
#     value = 10 / d
#     print ("value = ", value)
# except ZeroDivisionError as e :
#     print ("Error: ", str(e) )
#     print ("Ignore to continue ...")
#     print ("Let's go!")


def temp_convert(var):
    try:
        return int(var)
    except ValueError:
        print("Tham số truyền vào không phải là số.")
    finally:
        print("Khối finally vẫn được thực hiện: ", var)


temp_convert("xyz")
