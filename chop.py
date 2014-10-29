def chop(x):
	del x[0]
	x.pop()
def middle(x):
	return x[1:-1]
x=['1','2','3','1']
#chop(x)
print middle(x)
print x
