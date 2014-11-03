def print_hist(x):
	b=x.items()
	b.sort()
	for k in b:
		print k
print_hist({'a': 1, 'b': 1, 'o': 2, 'n': 1, 's': 2, 'r': 2, 'u': 2, 't': 1})
