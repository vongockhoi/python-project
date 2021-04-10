try:
    a=int(input())
    i=1
    if a > 0 and a < 10:
        while i<=10:
            tich = i*a
            print("{} x {} = {}".format(a,i,tich))
            i+=1
    else:
        print("nhập số lớn hơn 0 và nhỏ hơn 10")
except: 
    print("nhập số nguyên dương")