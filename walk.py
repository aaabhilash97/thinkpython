def walk(dir):
	pathlist=[]
	for name in os.listdir(dir):
		path = os.path.join(dir, name)
		if os.path.isfile(path):
			pathlist.append(path)
		else:
			walk(path)+pathlist
	return pathlist
import os
print walk(os.getcwd())
