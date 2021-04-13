import string
lista  = list(string.ascii_lowercase)
print(lista)
listcong = []
i = 1
tongkytu = 0
nhotam = 0
try:
    a = int(input())
    
    for lis in range(0,a):
        listcong.append(i)
        tongkytu +=i
        i +=2
    for lis in range(0,a):
        for lis1 in range(0,listcong[a-1]):
            print(" ",end=" ")
            if lis1 == a-(lis+1):
                for inkytu in range(0,listcong[lis]):
                    print(lista[nhotam], end=" ")
                    nhotam +=1 
                    if nhotam == 26:
                        nhotam = 0
        print("")
except:
    print("nhập sai phải nhập số tự nhiên")