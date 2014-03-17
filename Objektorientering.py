class bankaccount():
	def __init__(self):
		print "nu anropas konstruktorn"
		self.saldo=0
	def insertmoney(self,a):
		self.saldo=self.saldo+a
	def withdraw(self,b):
		self.saldo=self.saldo-b
	def checksaldo(self):
		print self.saldo

mittkonto=bankaccount()

mittkonto.checksaldo()
mittkonto.insertmoney(500)
mittkonto.checksaldo()
mittkonto.withdraw(70)

print mittkonto.saldo


class magicstaff():
	def __init__(self):

def 
