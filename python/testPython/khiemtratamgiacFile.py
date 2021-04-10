try:
    with open('tamgiacInp.txt','r') as fileIn:
        dongDauTien = fileIn.readline().rstrip('\n')
    a,b,c = map(float,input().split())

    if a<=0 or b <=0 or c<=0:
        thongBao = "cac canh cua tam giac phai lon hon 0"
    elif a+b >c and a+c >b and b+c > a:
        #Kiem tra tam giac vuong
        if a*a==b*b+c*c or b*b==a*a+c*c or c*c== a*a+b*b:
            loaiTamGiac = 'vuong'
        #Kiem tra tam giac deu
        elif a==b and b==c:
            loaiTamGiac = 'deu'
        #Kiem tra tam giac can
        elif a==b or a==c or b==c:
            loaiTamGiac = 'can'
        #Kiem tra tam giac tu
        elif a*a > b*b+c*c or b*b > a*a+c*c or c*c > a*a+b*b:   
            loaiTamGiac = 'tu'
        #Cac truong hop con lai la tam giac nhon
        else:
            loaiTamGiac = 'nhon'
        thongBao = "{}, {}, {} la ba canh cua mot tam giac {}".format(a, b, c, loaiTamGiac)
    else:
        thongBao = "{}, {}, {} khong phai la ba canh cua mot tam giac".format(a, b, c)

#Khoi lenh duoc thuc thi khi xay ra loi "Khong tim thay file input"
except FileNotFoundError:
    thongBao = "Khong tim thay file input!"
except:
   thongBao = "Dinh dang dau vao khong hop le!"

#Mo file voi mode='w' de ghi file
with open('Bai2.9.out', 'w') as fileOut:
   #Xuat thong bao ra file out
   fileOut.write(thongBao)