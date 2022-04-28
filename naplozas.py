from netmiko import ConnectHandler
import time
from datetime import datetime
net_connect = ConnectHandler(
	device_type="cisco_ios",
	host="172.19.0.2",
	username="admin",
	password="admin1234"
)
try:
	now = datetime.now()
	output = net_connect.send_command('show process cpu sorted | ex 0.00')
	print(now, output)
except NetMikoTimeoutException:
	print("SSH kapcsolodas nem sikerult")
