try:
    print("Nhap so tự nhiên lớn 0:")
    a = int(input())
    list_nguoc = []
    chuoi =  str(a)
    if a < 0:
        print("Nhập số nguyên dương")
    else:
        if a < 10:
            print("so ngược:",a)
        else:

            print("so ngược:",end="")
            for i in range(0,len(chuoi)):
                tach =  int(a%10)
                a =a/10
                print(tach,end="")
            print("")
except:
    print("Loi dinh dang")