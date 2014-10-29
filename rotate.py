def rotate(x,n):
	rt_str=''
	for z in x:
		if(ord('z')-ord(z))>=n:
			rt_str=rt_str+chr(ord(z)+n)
		else:
			print ((ord('z')-ord(z))+n)
			rt_str=rt_str+chr(n+96-(ord('z')-ord(z)))
	return rt_str
print rotate("auvwxyz",1)
