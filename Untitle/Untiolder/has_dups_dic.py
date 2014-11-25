def hasdups(x):
	dic={}
	for x1 in x:
		dic[x1]=dic.get(x1,0)+1
		if dic[x1]>1:
			return True
	return False
print hasdups([92,3,1,8])
