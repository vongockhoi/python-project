try:
    a = int(input())
    chuoi = str(a)
    if a <0:
        print("nhập so nguyên dương")
    else:
        tongchan = 0
        tongle =0
        for i in range(0,len(chuoi)):
            tam = int(a%10)
            a = a/10
            if tam %2 ==0:
                tongchan +=tam
            else:
                tongle +=tam
        print("tong chan le :",tongchan*tongle) 
except:
    print("loi dinh dang")