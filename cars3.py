import request
import show_json_cars as show

try:
	reply = request.get("https://localhost:300/cars?_sort_year&_order=desc")
except:
	print("hiba")
	exit()
show.show(reply.json)
