import requests
mm=requests.Session()
try:
	mm.get('http://httpbin.org/cookies/set/sessioncookie/kukiikszde')
	r1 = mm.get('http://httpbin.org/cookies')
except:
	print("hiba")
	exit()
print(r1.next)
