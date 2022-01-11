import requests
import show_json_ddns as show
import json

headers1 = {'Connection': 'keep-alive'}
headers2 = {'Connection': 'Close'}
h_close={'Connection': 'close'}
h_content={'Content-Type': 'application/json'}
newddns = {"id":5, "nev":"random", "ip":"192.168.1.1", "datum":"2002.12.12 11:41:23"}
newddns2 = {"id":5, "nev":"Petike", "ip":"192.168.1.1", "datum":"2002.12.12 11:41:23"}
try:
	reply = requests.post("http://localhost:3000/ddns", headers = h_content, data=json.dumps(newddns))
	print("status_code" + str(reply.status_code))
	reply = requests.put("http://localhost:3000/ddns", headers = h_content, data=json.dumps(newddns2))
	print("status_code" + str(reply.status_code)) 
	reply = requests.get("http://localhost:3000/ddns", headers = headers2)
except:
	print("Hiba!")
	exit()

show.show(reply.json())
