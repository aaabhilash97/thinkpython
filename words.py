def word(x):
	f=open(x).read().split()
	for w in f:
		if len(w)>20:
			print w
word('foo.txt')
