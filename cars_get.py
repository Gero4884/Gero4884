import requests
try:
	reply=requests.get("http://localhost:3000/cars")
except:
	print("Hiba")
	exit()
for idx, item in enumerate(reply.json()):
	print(f"{idx+1}. {item['name']}")
