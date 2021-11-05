def fugg(x):
	if not x % 2:
		return True
	return False

l = [10, 9, 8 ,7]
l2=filter(fugg, l)
print(l)
print(list(l2))
