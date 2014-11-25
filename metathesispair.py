def metathesispairs(x):
	dic={}
	i=0
	while i<len(x):
		j=i+1
		while j<len(x):
			dic.setdefault(x,[])
			dic[x].append(x[:i]+x[j]+x[i+1:j]+x[i]+x[j+1:])
			j+=1
		i+=1
	print dic
metathesispairs("abhi")
