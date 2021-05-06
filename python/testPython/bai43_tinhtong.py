def tinh_tong(*args):
    tong = 0
    print(type(args))
    for a in args:
        print("kieu:",type(a))
        tong +=a
    return tong

try:
    print("tong:{}".format(tinh_tong(2,4,4,2.2)))

except:
    print("Loi dinh dang")