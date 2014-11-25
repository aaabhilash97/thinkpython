class point(object):
	x=1
	y=1
class box(object):
	w=2
	h=3
	corner=point()
def moverec(box,dx,dy):
	box.corner.x+=dx
	box.corner.y+=dy
p=box()
moverec(p,2,3)
print box.corner.x,box.corner.y
