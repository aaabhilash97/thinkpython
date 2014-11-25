def isalphaorder(x):
	old=0
	for w in x:
		if ord(w)<old:
			return False
		old=ord(w)
	return True
print isalphaorder("abhi")
