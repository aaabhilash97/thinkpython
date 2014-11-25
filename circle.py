import sys
from swampy.World import World
def draw_cir(x,y,col):
        world=World()
        canvas = world.ca(width=500, height=500, background='white')
        bbox = [x,y]
	canvas.circle(bbox, 70, outline=None, fill=col)
        world.mainloop()
draw_cir(int(sys.argv[1]),int(sys.argv[2]),sys.argv[3])
