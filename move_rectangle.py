import copy
class point(object):
	x=1
	y=1
class rec(object):
	w=4
	h=3
	corner=point()
def moverectangle(rec,dx,dy):
	rec1=copy.copy(rec)
	rec1.corner.x+=dx
	rec1.corner.y+=dy
	return rec1
p=rec()
p1=moverectangle(p,2,3)
print p1.corner.x,p1.corner.y
