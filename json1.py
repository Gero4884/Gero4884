import json
d = {
     "vezetekNev": "Kovacs",
     "keresztNev": "Janos",
     "kor": 25,
     "cim":
     {
         "utcaHazszam": "2. utca 21.",
         "varos": "New York",
         "allam": "NY",
         "iranyitoSzam": "10021"
     }
}
print(json.dumps(d))
with open("dump.txt", "w") as f:
	json.dump(d,f)

