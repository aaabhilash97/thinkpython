import pronounce
dic={}
def maxpath(y):
    li=[y]
    c=[]
    g=[]
    if y in dic:
	for x in dic[y]:
		c=maxpath(x)
		if len(c)>len(g):
			g=c
    return li+g
def reducible(x):
	d=pronounce.read_dictionary().keys()
	for key in d:
		if len(key)<2:
			d.remove(key)
	if x in dic:
		return
	if x in d:
		i=0
		while i<len(x):
			if x[:i]+x[i+1:] in d and x[:i]:
				dic.setdefault(x,[])
				dic[x].append(x[:i]+x[i+1:])
				reducible(x[:i]+x[i+1:])
			i+=1
	k=dic.items()
	k.sort(key=lambda x:len(x[0]),reverse=True)
	return k
def realreduce(x):
	reducible(x)
	c=maxpath(x)
	dic=[]
	return c
print realreduce("sport")
