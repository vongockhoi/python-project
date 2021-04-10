import re
i = 0
while i == 0:
    try:
        print("nhap vao chieu cao A:")
        ten_a,chieuc_a = input().split()
        # a = "2002-54555-545 # this saijs "
        print("nhap vao chieu cao b:")
        ten_b,chieuc_b = input().split()
        chieucao_a = int(chieuc_a)
        chieucao_b = int(chieuc_b)
        if chieucao_a < 0 or chieucao_b < 0:
            print("chieu cao k dc am")
        else:
            i=i+1
    except:
        print("nhap k hop le!!")   
if chieucao_a > chieucao_b:
    print("{} cao hon {}".format(ten_a,ten_b))
elif chieucao_a < chieucao_b:
    print("{} cao hon {}".format(ten_b,ten_a))
else:
    print("{}, {} bang nhau".format(ten_a,ten_b))

# num = re.sub(r'#.*$',"",a)
# print("chuoi:",num)