import sys
from swampy.World import World
def draw_chezrep():
        world=World()
        canvas = world.ca(width=500, height=500, background='white')
	canvas.rectangle([[-150,-100], [150, 100]], outline='black', width=2, fill='white')
	canvas.rectangle([[-150,-100], [150, 15]], outline='black', width=2, fill='red')
        points = [[-150,-100], [-150,100], [0,15]]
        canvas.polygon(points, fill='blue')
        world.mainloop()
draw_chezrep()
