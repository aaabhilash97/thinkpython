def countletter(s,x):
	i=0
	for l in s:
		if x==l:
			i=i+1
	return i
print countletter("qwergbvfeq","q")
