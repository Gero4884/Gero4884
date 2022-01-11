import requests
url="https://postman-echo.com/basic-auth"
h={"Authentication hmae username:123456:[digest]"}
try:
	reply=requests.get(url, headers=h)
except:
	print("Hiba")
	exit()
print(reply.status_code)
print(reply.text)
