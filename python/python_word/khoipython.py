#ssss
so1=1
so2=2
stria = "vongockhoi"
strb = stria[0:5]
print(strb)
a = 'my khoi %s  %s'%(212,'khoi')
print(a)
print(strb)
print(a)
if so2>so1:
	print("lon hon")
else:
	print("nho hon")
class ClassName:
		def __init__(conga, name, age):
			conga.name = name;
			conga.age = age;
p1 = ClassName("khoi",25)
class classx():
	
	def __init__(self,so):
		self.x=0
p2 = classx(9)
print(p1.age)
print(p1.name)
print(p2.x)
#bai 3
class SieuNhan:
	suc_manh = 50
	def __init__(self,para_ten,para_vukhi,para_mausac):
		self.para_ten = para_ten
		self.para_vukhi = para_vukhi
		self.para_mausac = para_mausac
	@classmethod
	def from_string(cls,s):
		lst=s.split('-')
		new_lst=[st.strip() for st in lst]
		ten, vu_khi, mau_sac = new_lst
		return cls(ten,vu_khi,mau_sac)
infor_str = "do - kiem - do"
sieu_nhan_A = SieuNhan.from_string(infor_str)
print(sieu_nhan_A.__dict__)

class SieuNhanK(SieuNhan):
	suc_manh=40
	def __init__(self,para_ten,para_vukhi,para_mausac,para_su_thu):
		super().__init__(para_ten,para_vukhi,para_mausac)
		self.su_thu = para_su_thu
snk = SieuNhanK("do","sung","do","vng")
print(snk.suc_manh)


