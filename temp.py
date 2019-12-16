EDGE = 20
import pygame,math
from pygame.locals import*
def hex_points(x, y):
    points = [(x+EDGE, y-EDGE), (x,y), (x+EDGE, y+EDGE), (x+2*EDGE,y+EDGE),(x+3*EDGE,y),(x+2*EDGE,y-EDGE)]
    return points


def hex_area(x):
    area = 0.0
    area = math.sqrt(3)*x*x/4
    return area


def square_points(x,y):
    points = [(x, y),( x, y+EDGE),(x+EDGE,y+EDGE),(x+EDGE,y)]
    return points


def square_area(x):
    return x*x
pygame.init()
window = pygame.display.set_mode((640,600))
purple = (155,0,155)
pygame.draw.polygon(window,(purple), [(60, 10), (40, 30), (60, 50), (80, 50), (100, 30), (80, 10)])
run = True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run = False
    pygame.display.update()

