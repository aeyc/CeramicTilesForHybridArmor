from tkinter import*
EDGE=20
window = Tk()
window.title("Work Place")
canvas = Canvas(window, width =425, height=650)
#frame = Frame(width=500, height=200, bg='blue')
#canvas = Canvas(frame, bg='white')
canvas.pack(fill = BOTH, expand = YES)
#frame.pack(fill = BOTH, expand = YES)
def hex_points(x,y):
    points = (x+EDGE, y-EDGE, x,y, x+EDGE, y+EDGE, x+2*EDGE,y+EDGE,x+3*EDGE,y,x+2*EDGE,y-EDGE)
    return points

def square_points(x):
    y = x
    points = (x, y, x, y+EDGE,x+EDGE,y+EDGE,x+EDGE,y)
    return points

hexagon_points = hex_points(0,20) #range of hexagon (x>=0, y>=20)
square_points = square_points(0)
canvas.create_polygon(square_points, outline="blue", fill="#fb0")
canvas.create_polygon(hexagon_points,outline = 'green', fill='yellow',width = 1)

window.mainloop()
