def find(s,x):
	i=0
	while i<(len(s)-len(x)):
		print x,s[i:i+len(x)]
		if x==s[i:i+len(x)]:
			print i
			return i
		i=i+1
	return -1
print find("abhilash km ur ","lash")
