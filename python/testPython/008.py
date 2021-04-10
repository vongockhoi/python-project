i = 0
while i==0:
    print("nhap chuoi so:")
    number = input()
    try:
        listNum= number.split()
        listInt = map(int,listNum)
        tong = sum(listInt)
        print("tong la:",tong)
        i=i+1
    except:
        print("ngu")  
          