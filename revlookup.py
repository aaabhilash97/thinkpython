def histogram(s):
	d = dict()
	for c in s:
		if c not in d:
			d[c] = 1
		else:
			d[c] += 1
	return d
def rev_lookup(h,v):
	li=[]
	for k in h:
		if h[k]==v:
			li.append(k)
	return li
h=histogram('parrot')
k=rev_lookup(h,3)
print k
