import os
dic={}
def walkos(x):
        for root,dirs,files in os.walk(x):
                for f in files:
			md5sum=os.popen('md5sum '+os.path.join(root,f)).read().split()[0]
			file1=os.popen('md5sum '+os.path.join(root,f)).read().split()[1]
			if md5sum in dic:
				dic[md5sum]=dic.get(md5sum,[])+[file1]
			else:
				dic.setdefault(md5sum,[file1])
			
                for d in dirs:
                      walkos(os.path.join(root,d))
walkos(os.getcwd())
for key,val in dic.items():
	if len(val)>1:
		print val
