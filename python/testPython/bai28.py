try:
    a,b = map(int,input().split())
    dem = 0
    if a<=b:
        for so in range(a,b+1):
            if so%5==0 and dem < 10:
                print(so,end=" ")
                dem+=1
        if dem == 0:
            print("khong co so nao chia het cho 5")
    else:
        print("a phai nho hon b")
except:
    print("Dinh dang k hop le")