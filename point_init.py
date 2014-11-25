class point(object):
	def __init__(self,x=0,y=0):
		self.x=x
		self.y=y
	def __add__(self,n):
		p2=point()
		p2.x=self.x+n.x
		p2.y=self.y+n.y
		return p2
p=point(2,3)
p1=point(4,5)
p2=p.__add__(p1)
print p2.x,p2.y
