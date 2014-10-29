import math
def eval_loop():
	while True:
		i=raw_input("enter=")
		print i
		if i=="done":
			return x
		x=eval(str(i))
		print x
print eval_loop()
