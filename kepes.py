import requests, hashlib, os
url = "http://docker.lan:8420/"
pas =input("Password: ")
photo = "thinkstockphotos-521697453-e1526731524153.jpg"
sha = hashlib.sha512(pas.encode("utf8")).hexdigest()
fsize = os.path.getsize(photo)
d = {"password" : sha, "filesize" : fsize}
try:
	f = open(photo, 'rb')
	reply = requests.post(url, data = d, files = {"upfile": f})
	f.close()
except:
	print("hiba")
	exit()

print(reply.status_code)
