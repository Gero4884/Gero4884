#!/usr/bin/env python3

def myint(a):
	n=0
	for i in a:
		k = ord(i)
		if k < 48 or k > 57:
#			print("Nem szamot adtal meg")
			break
		else:
			n=n*10+(k-48)
	return(n)

szam=input("Adj meg egy szamot ami minimum 1 maximum 10 karakterbol all: ")
try:
	assert (len(szam) >=1 and len(szam) <= 10)
except:
	print("Nagyobb a szam mint 10 vagy kisebb mint 1")
	exit()
print(myint(szam))
