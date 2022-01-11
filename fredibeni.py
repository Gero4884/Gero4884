from datetime import datetime
from time import sleep
def fredi():
	print(a)
def beni():
	global a
	a=datetime.now()

while True:
	beni()
	fredi()
	sleep(1)
