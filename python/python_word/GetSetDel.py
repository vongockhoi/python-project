class Khoine:
	def __init__(self, ho, ten):
		self.ho = ho
		self.ten = ten
		self.email = ho + '-' + ten + '@gmail.com'
	def hovaten(self):
		return '{}{}'.format(self.ho, self.ten)
khoi_A = Khoine("vo","ngoc")
print(khoi_A.ho)
print(khoi_A.ten)
print(khoi_A.email)
print(khoi_A.hovaten())