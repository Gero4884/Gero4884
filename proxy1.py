import requests
url = "http://postman-echo.com/basic-auth"
p = {'http':"http://localhost:8080"}
try:
	reply = requests.get(url, auth=("postman", "password"), proxies=p)
except:
	print("Hiba")
	exit()
print(reply.status_code)
print(reply.text)
