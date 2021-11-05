#!/usr/bin/env python3
print ("feladom")
year=int(input("Adj meg egy evszamot: "))
if year<1852:
	print ("Nem Gergely naptar")
elif year // 4 == 0 and year // 100 == 0 and year // 400 == 0:
	print ("szokoev")
