def bisect(x,y):
	if y==x[len(x)/2]:
		return len(x)/2
	elif y<x[len(x)/2]:
		return bisect(x[:len(x)/2],y)
	elif y>x[len(x)/2]:
		return (len(x)/2)+bisect(x[len(x)/2:],y)
print bisect([1,2,3,4,5,6,7,8,9,10,11,12],12)
