from netmiko import ConnectHandler

net_connect = ConnectHandler(
	device_type="cisco_ios",
	host="172.19.0.2",
	username="admin",
	password="admin1234"
)

try:
	output = net_connect.send_command('show process cpu sorted | ex 0.00')
	print(output)
except NetMikoTimeoutException:
	print("SSH kapcsolodas nem siekrult")
