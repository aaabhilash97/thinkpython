def hasdup(x):
	i=0
	while i<len(x):
		if x[i] in x[0:i]+x[i+1:]:
			return True
		i=i+1
	return False
print hasdup([1,2,45,56,6,6])
			
