def sosanhtuoi(tena,tuoia,tenb,tuoib):
    if tuoia > tuoib:
        return tena
    elif tuoia < tuoib:
        return tenb
    else:
        return 0
try:
    ten_a, tuoi_a = input().split()
    ten_b, tuoi_b = input().split()
    tuoi_a = int(tuoi_a)
    tuoi_b = int(tuoi_b)
    if tuoi_a < 1 or tuoi_b < 1:
        print("nhap tuoi >0")
    else:
        lon_tuoi = sosanhtuoi(ten_a,tuoi_a,ten_b,tuoi_b)
        if lon_tuoi == 0:
            print("{} cao bang {}".format(ten_a,ten_b))    
        else:
            print("{} cao hơn".format(lon_tuoi))
except:
    print("sai định dạng")