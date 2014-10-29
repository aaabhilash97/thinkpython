def useall(w,s):
	for s1 in s:
		if s1 not in w:
			return False
	return True
print useall("wordssdd","words")
