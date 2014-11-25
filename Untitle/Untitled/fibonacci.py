dic={0:0,1:1}
def fib(n):
	if n in dic:
		return dic[n]
	else:
		dic.setdefault(n,fib(n-1)+fib(n-2))
		return dic[n]
print fib(50)
