i = 0
while i == 0:
    try:
        print("nhap 3 canh tam giac:")
        a,b,c = map(float,input().split())
        if a+b>c and a+c > b and c+b > a:
            print("ba canh tam giac")
        else:
            print("khong phai canh tam giac")
        if a<=0 or b<=0 or c<=0:
            print("canh phai lon hon 0")
        else:
            i=i+1
    except:
        print("nhap khong hop le\n")


