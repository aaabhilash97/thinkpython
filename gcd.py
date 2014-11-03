def gcd1(a,b):
	if a%b==0:
		return b
	return gcd(b,a%b)
print gcd(2,33)
