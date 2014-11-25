import os
def walkos(x):
	for root,dirs,files in os.walk(x):
		for f in files:
			print os.path.join(root,f)
		for d in dirs:
			walkos(os.path.join(root,d))
walkos(os.getcwd())
