
with open('bai10ip.txt', 'r') as fileInp:

    #Doc 1 dong du lieu tu file va luu vao bien ten
    #Su dung phuong thuc rstrip de loai bo ky tu xuong dong '\n'
    ten = fileInp.readline().rstrip('\n')
    print(fileInp.readline)
    #Doc 1 dong du lieu tu file va luu vao bien tuoiHienTai
    tuoiHienTai = int(fileInp.readline())
    print(type(ten))
#Mo file voi mode='w' de ghi file
with open('bai10outt.txt', 'w') as fileOut:

   #Ghi noi dung vao file theo mau
   fileOut.write('Vao 20 nam nua, tuoi cua {} se la {}'.format(ten, tuoiHienTai + 20))