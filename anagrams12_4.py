import itertools
def anagrams(x):
	f=open(x).read().split()
	dic={}
	i=0
	while i<len(f):
		f1=f[i]
		f.remove(f1)
		for f2 in ["".join(z) for z in itertools.permutations(f1)]:
			if f2 in f:
				f.remove(f2)
				dic.setdefault(f1,[f1])
				dic[f1].append(f2)
	s=dic.items()
	s.sort(key=lambda x:len(x[1]),reverse=True)
	for k,v in s:
		print v
anagrams("word.txt")
