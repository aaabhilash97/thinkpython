def rotpairs(x):
	dic={}
	i=0
	for x1 in x:
		if x1[::-1] in x:
			dic[x1]=dic.get(x1,x1[::-1])
	return dic
print rotpairs(["deer","reed","pair","riap","asas"])
