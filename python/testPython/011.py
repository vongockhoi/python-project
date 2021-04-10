with open('bai10ip.txt','r') as fileIn:
    fimeNew = fileIn.read()
    dscacdong = fimeNew.splitlines()
    CauChaoHoanChinh = ' '.join(dscacdong)
with open('bai10outt.txt','w') as fileout:
    fileout.write(CauChaoHoanChinh)