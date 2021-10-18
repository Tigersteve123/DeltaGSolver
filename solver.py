import math

class solver:
	def __init__(self, t):
		self.temp = t
		self.r = 1.985*math.pow(10, -3)
		self.initconc = .005

	def concentration(self, g0, c0, dg):
		x = (dg-g0)/self.rt()
		return math.exp(x)*c0

	def rt(self):
		return .6 #self.r*self.temp

s1 = solver(293)
cg6p = s1.concentration(-4.0, .005, -8.0)
cf6p = s1.concentration(.4, cg6p, -.6)
cf16dp = s1.concentration(-3.4, cf6p, -5.3)
cg3pdhap = s1.concentration(5.7, cf16dp, -.3)
cg3p = math.sqrt(cg3pdhap/(math.exp(-1.8/s1.rt())))
print(cg3p)
