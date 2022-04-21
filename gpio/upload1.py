import os, requests
from time import sleep
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()
token=os.environ.get('API_KEY')
url="http://docker.lan:8888/upload"
most=datetime.now()
d={"date":most,"type":"cm","value":"10","token":token}
try:
     reply = requests.post(url, d)
except:
     print("hiba")
     exit()
print(reply.status_code)
if reply.status_code=201:
     print("Sikerult!")
else:
     print("Nem Sikerult")
