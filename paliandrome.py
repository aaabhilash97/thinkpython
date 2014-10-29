def first(word):
	return word[0]
def last(word):
	return word[-1]
def middle(word):
	return word[1:-1]
def ispalian(x):
	if first(x)==last(x):
		if len(x[1:-1])<=1:
			return True
		c=ispalian(x[1:-1])
		return c
	else:
		return False
print ispalian("malyalam")
