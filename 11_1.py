def words(x):
	f=open(x).read().split()
	dic={}
	for x1 in f:
		dic[x1]=dic.get(x1,0)+1
	return f
print "fuck" in words("word.txt")
