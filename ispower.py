def ispower(a,b):
	if a%b==0 and (a/b)%b==0:
		return True
	else:
		return False
print ispower(9,3)
