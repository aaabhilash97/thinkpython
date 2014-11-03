def revpair(x):
	i=0
	rep=[]
	while i<len(x):
		if x[i][::-1] in x[i+1:]:
			rep.append([x[i],x[i][::-1]])
		i+=1
	return rep
print revpair(['ab','ba','wwew','wewewwewewe','asd','dsa','ac'])
