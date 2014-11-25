class Point(object):
	def __init__(self,x=0,y=0):
		self.x=x
		self.y=y
	def __add__(self,other):
		if isinstance(other,Point):
			return self.addpt(other)
		elif isinstance(other,tuple):
			return self.addtp(other)
	def addpt(self,other):
		new=Point()
		new.x=self.x+other.x
		new.y=self.y+other.y
		return new
	def addtp(self,other):
		new=Point()
		new.x=self.x+other[0]
		new.y=self.y+other[1]
		return new
p=Point(2,3)
p1=Point(1,2)
new=p.__add__((1,2))
print new.x,new.y
