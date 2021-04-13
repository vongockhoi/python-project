try:
    n = int(input())
    tong=1
    if n < 0:
        print("Vui long nhap so tu nhien lon hon 0")
    else:
        for i in  range(0,n+1):
            if i == 0:
                tong *=1
            else:
                tong = tong*i
        print("giai thừa {} = {}".format(n,tong))
except:
    print("Dịnh dạng không hợp lệ")