try:
    a,b = map(int,input().split())
    tong = 0
    if a <= b:
        while a<=b:
            tong = tong + a
            a = a+1
        print("tong a b là:",tong)
    else:
        print("a lon hon b roi")
except:
    print("nhap so nguyen cha")    