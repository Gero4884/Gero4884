import requests
s = requests.Session()
s.auth = ("user", "pass")
s.headers.update({'x-test':'true'})
try:
	r = s.get('https://httpbin.org/headers')
except:
	print('hiba')
	exit()
print(r.text)
