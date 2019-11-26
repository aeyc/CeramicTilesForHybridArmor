from tkinter import*
import random
import math
EDGE = 20
X_LIMIT = 360
Y_LIMIT = 500
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


count = 0
used_points = []

appeared=False
while count < 10:
    choice = random.randint(0, 2)
    appeared = False
    if choice == 1:
        x = random.randint(0, X_LIMIT)
        y = random.randint(EDGE, Y_LIMIT)

        for i in used_points:
            if (x,y) == i:
                appeared = True
        if not appeared:
            hexagon_points = hex_points(x, y)  # range of hexagon (x>=0, y>=20)
            a = canvas.create_polygon(hexagon_points, outline='green', fill='yellow', width=1)
            for i in range(x+EDGE,x-1,-1):
                for j in range(y+EDGE,y+EDGE-1,-1):
                    used_points.append((i,j))
            for i in range(x+EDGE, x+2*EDGE+1):
                for j in range(y,y+2*EDGE+1):
                    used_points.append((i, j))
            for i in range(x+2*EDGE,x+3*EDGE):
                for j in range(y+2*EDGE,y+EDGE-1,-1):
                    used_points.append((i,j))
    elif choice == 0:
        x = random.randint(0, X_LIMIT)
        y = x
        for i in used_points:
            if (x,y) == i:
                appeared = True
        if not appeared:
            s_points = square_points(x)
            b = canvas.create_polygon(s_points, outline="blue", fill="#fb0")
            for i in range(x+EDGE,x-1,-1):
                for j in range(y+EDGE,y-1,-1):
                    used_points.append((i,j))
    print(used_points)
    count += 1

window.mainloop()
