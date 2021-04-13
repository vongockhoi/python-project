def ten_tuoi(ten,tuoi):
    print("xin choi toi la {},{} tuoi".format(ten,tuoi))
try:
    ten = str(input())
    tuoi = int(input())
    if tuoi < 1:
        print("nhap tuoi lon hon 0")
    else:
        ten_tuoi(ten,tuoi)
except:
    print("loi dinh dang")