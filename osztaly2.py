class cica(c1, c2, c3):
	def __init__(self):
		self.alom = 0
	def szuletes(self):
		self.alom += 1
class sziami(cica):
	def __init__(self):
		cica.__init__(self)
		self.nevek = []
	def ujnev(self, nev):
		self.nevek.append(nev)
c = cica(c1, c2, c3)
sz = sziami()
print(isinstance(sz, cica))
print(isinstance(c, sziami))
