class Vowels:
	def __init__(self):
		self.vow = "aieouy "
		self.pos = 0
	def __iter__(self):
		return self
	def __next__(self):
		if self.pos == len(slef.vow):
			raise StopIteration
		self.pos += 1
		return self.vow[self.pos - 1]

v = Vowels()
for i in v:
	print(i, end=" ")
print("")
