from tkinter import*
import random
import math
EDGE = 20
X_LIMIT = 100
Y_LIMIT = 100
TOTAL_AREA = 425*650
window = Tk()
window.title("Work Place")
canvas = Canvas(window, width=425, height=650)
# frame = Frame(width=500, height=200, bg='blue')
# canvas = Canvas(frame, bg='white')
canvas.pack(fill = BOTH, expand = YES)
# frame.pack(fill = BOTH, expand = YES)


def hex_points(x, y):
    points = (x+EDGE, y-EDGE, x,y, x+EDGE, y+EDGE, x+2*EDGE,y+EDGE,x+3*EDGE,y,x+2*EDGE,y-EDGE)
    return points


def hex_area(x):
    area = 0.0
    area = math.sqrt(3)*x*x/4
    return area


def square_points(x):
    y = x
    points = (x, y, x, y+EDGE,x+EDGE,y+EDGE,x+EDGE,y)
    return points


i = 0
used_points = []
while i < 3:
    choice = random.randint(0, 2)
    if choice == 1:
        x = random.randint(0, X_LIMIT)
        y = random.randint(EDGE, Y_LIMIT)
        if (x, y) not in used_points:
            hexagon_points = hex_points(x, y)   # range of hexagon (x>=0, y>=20)
            canvas.create_polygon(hexagon_points, outline='green', fill='yellow', width=1)
            used_points.append((x, y))   # used points needs fix
    elif choice == 0:
        x = random.randint(0, X_LIMIT)
        y = x
        if (x, y) not in used_points:
            s_points = square_points(x)
            canvas.create_polygon(s_points, outline="blue", fill="#fb0")
            used_points.append((x, y))
    i += 1



window.mainloop()
