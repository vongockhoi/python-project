i = True
try:
    a,b = map(int,input().split())
    if a <= b:
        tong = 0
        for i in range(a,b+1):
            tong = tong+i
        print("tong la",tong)
    else:
        print("sai")
except:
    print("nhap so int")
