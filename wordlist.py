def wordlist(x):
	f=open(x).read().split()
	s=[]
	for a in f:
#		s+=[a]
		s.append(a)
	return s
print wordlist("word.txt")
