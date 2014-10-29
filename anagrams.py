def anagrams(x,y):
	from itertools import permutations
	return y in [''.join(p) for p in permutations(x)]
print anagrams("sup","pous")
