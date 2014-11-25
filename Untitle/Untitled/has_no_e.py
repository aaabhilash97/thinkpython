def hasnoe(x):
	f=open(x).read().split()
	e=0.0
	noe=0.0
	for w in f:
		if 'e' in w:
			e=e+1
		else:
			print w
			noe=noe+1
	print (e/(noe+e))*100
hasnoe("foo.txt")
