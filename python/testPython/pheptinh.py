print("nhap chuoi tinh:")
a,pheptinh,b = map(str,input().split())
soA = float(a)
soB = float(b)
tong = None
if '+' in pheptinh:
    tong = soA+soB
elif '-' in pheptinh:
    tong = soA-soB
elif 'x' in pheptinh:
    tong = soA*soB
elif pheptinh == ':':
    tong = soA/soB
print(tong)