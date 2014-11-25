import sys
from swampy.World import World
def draw_point(x,y):
        point=World()
        canvas=point.ca(width=500,height=500,background='white')
        bbox=[[x,y],[x,y]]
        canvas.rectangle(bbox)
        point.mainloop()
draw_point(23,4)
