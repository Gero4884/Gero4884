#x = int(input('Add meg a haromszog egyik oldalat: '))
#y = int(input('Add meg a haromszog masodik oldalat: '))
#z = int(input('Add meg a haromszog harmadik oldalat: '))
def is_a_triangle(a, b, c):
	if a > b + c:
		return False
	elif b > a + c:
		return False
	elif c > a + b:
		return False 
	return True
import math
from math import sqrt
#if is_a_triangle(x, y, z):
#	print("Jo a haromszog")
#else:
#	print("Nem jo a haromszog")
