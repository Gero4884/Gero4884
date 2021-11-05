#!/usr/bin/env python3
szoveg = input("Szoveg: ")
try:
	szam = int(input("Adjon meg egy szamot 1 es 25 kozott: "))
except:
	print("Nem szamot adtal meg! Kerlek szamot adj meg!")
	exit()
if not (szam >= 1 and szam <= 25):
	print("Nem jo szamot adtal meg!!")
for i in szoveg:
	code = ord(i)
	if code >= 97 and code <= 122:
		if (ord(i)+szam>122):
			nagyobb = ord(i)+szam+97-122
			print(chr(nagyobb),end="")
		else:
			print(chr(ord(i)+szam),end="")
	elif code >= 65 and code <= 90:
		if (ord(i)+szam>90):
			nagyobb2 = ord(i)+szam+65-90
			print(chr(nagyobb2),end="")
		else:
			print(chr(code+szam),end="")
	else:
		print(i,end="")
print("")
