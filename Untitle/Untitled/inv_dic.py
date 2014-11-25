def invert_dict(d):
	inv = dict()
	for key in d:
		val = d[key]
		if val not in inv:
			inv.setdefault(val,[key])
		else:
			inv[val].append(key)
	return inv
print invert_dict({'a': 1, 'p': 1, 'r': 2, 't': 1, 'o': 1})
