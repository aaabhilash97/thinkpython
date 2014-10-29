def issorted(x):
	i=1
	while i<len(x):
		if x[i]<x[i-1]:
			return False
		i=i+1
	return True
x=['ab','abh','km']
print issorted(x)
print x

