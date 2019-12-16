import pygame,random,time,sys,math
from pygame.locals import *

EDGE = 20
X_LIMIT = 360
Y_LIMIT = 600
TOTAL_AREA = 425*650

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


class GameState:
    def __init__(self):
        global FPSCLOCK,DISPLAYSURF, BASICFONT,BIGFONT
        pygame.init()
        FPSCLOCK = pygame.time.Clock()
        DISPLAYSURF = pygame.display.set_mode((425, 650))
        BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
        BIGFONT = pygame.font.Font('freesansbold.ttf', 100)
        pygame.display.iconify()
        pygame.display.set_caption('Ceramic Tiles for Hybrid Armor')

        self.score = 0
        self.remaining_area = 0
        self.used_points = []
        self.moves = []
        self.coords = self.shape_choice()

        pygame.display.update()

    def reinit(self):
        self.score = 0
        self.remaining_area = 0
        self.used_points = []
        self.moves = []
        self.shape = self.shape_choice()

        pygame.display.update()

    def shape_choice(self):
        choice = random.randint(0, 2)
        tmp_points = [] #coordinate for the polygon
        appeared = False
        coords = []
        if choice == 0:
            x = random.randint(0, X_LIMIT)
            y = random.randint(EDGE, Y_LIMIT)
            for i in range(x, x + EDGE):
                for j in range(y, y + EDGE):
                    tmp_points.append((i, j))
            for i in self.used_points:
                for j in tmp_points:
                    if j == i:
                        appeared = True
            if not appeared:
                s_points = square_points(x, y)
                coords = s_points
                #create polygon here?
                for i in range(x, x + EDGE):
                    for j in range(y, y + EDGE):
                        self.used_points.append((i, j))
                self.remaining_area -= square_area(EDGE)
                self.moves.append(( choice, (x, y)))
        elif choice == 1:
            print("choice 1")
            x = random.randint(0, X_LIMIT)
            y = random.randint(EDGE, Y_LIMIT)

            # rectangular area
            for i in range(x + EDGE, x + 2 * EDGE):
                for j in range(y - EDGE, y + EDGE):
                    tmp_points.append((i, j))

            # triangular area-up left
            tmp_k = x
            for j in range(y, y + EDGE):
                for i in range(tmp_k, x + EDGE):
                    tmp_points.append((i, j))
                tmp_k += 1

            # triangular area-down left
            tmp_k = x
            for j in range(y, y - EDGE, -1):
                for i in range(tmp_k, x + EDGE):
                    tmp_points.append((i, j))
                tmp_k += 1

            # triangular area-up right
            tmp_k = x + 2 * EDGE
            for j in range(y, y + EDGE):
                for i in range(tmp_k, x + 3 * EDGE):
                    tmp_points.append((i, j))
                tmp_k += 1

            # triangular area-down right
            tmp_k = x + 2 * EDGE
            for j in range(y, y - EDGE, -1):
                for i in range(tmp_k, x + 3 * EDGE):
                    tmp_points.append((i, j))
                tmp_k += 1

            for i in self.used_points:
                for j in tmp_points:
                    if j == i:
                        appeared = True
            if not appeared:
                hexagon_points = hex_points(x, y)  # range of hexagon (x>=0, y>=20)
                coords = hexagon_points
                #a = canvas.create_polygon(hexagon_points, outline='green', fill='yellow', width=1)
                for i in tmp_points:
                    self.used_points.append(i)
                self.remaining_area -= hex_area(EDGE)
                self.moves.append((choice, (x, y)))
        return coords

    def getImage(self):
        image_data = pygame.surfarray.array3d(pygame.transform.rotate(pygame.display.get_surface(), 90))
        return image_data
# Surface = pygame.display.set_mode((800,600))
# BLUE = (80,208,255)
# PINK = (255,208,160)
# g = GameState()
# print(g.shape_choice())
# # pygame.draw.polygon(Surface, (BLUE), g.shape_choice())
# # run = True
# # while run:
# #     for event in pygame.event.get():
# #         if event.type == pygame.QUIT:
# #             run = False
# #     pygame.display.update()
# #     break