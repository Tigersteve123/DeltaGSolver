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
cg3p = math.sqrt(cg3pdhap/(math.exp(1.8/s1.rt())))
c13bp = s1.concentration(1.5, cg3p, -.4)
c3pg = s1.concentration(-4.5, c13bp, 0)
c2pg = s1.concentration(1.1, c3pg, 0)
cppp = s1.concentration(.4, c2pg, -.8)
cpyruvate = s1.concentration(-7.5, cppp, -4.0)
l = {"Glucose": .005, "Glucose-6-phosphate": cg6p, "Fructose-6-phosphate": cf6p, "Fructose-1,6-diphosphate": cf16dp, "G3P+DHAP": cg3pdhap, "G3P": cg3p, "1,3-biphosphoglycerate": c13bp, "3-phosphoglycerate": c3pg, "2-phosphoglycerate": c2pg, "Phosphoenolpyruvate": cppp, "Pyruvate": cpyruvate}
for key, value in l.items():
	print(key, value)
