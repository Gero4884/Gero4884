import requests
url= "https://postman-echo.com/basic-auth"
h={"x-api-key":"DEMO-API-KEY"}
try:
	reply=requests.get(url, auth=("postman", "password"))
except:
	print("Hiba")
	exit()
for idx, item in enumerate(reply.json()):
	print(f"{idx+1} {item['name']}")
