import sys
from swampy.World import World
def draw_rec(x,y,col):
	world=World()
	canvas = world.ca(width=500, height=500, background='white')
	bbox = [[-x,-y], [x, y]]
	canvas.rectangle(bbox, outline='black', width=2, fill=col)
	world.mainloop()
draw_rec(int(sys.argv[1]),int(sys.argv[2]),sys.argv[3])
