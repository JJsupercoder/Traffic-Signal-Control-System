import pygame

pygame.init()

# set up the window
WIDTH = 800
HEIGHT = 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Environment")

# define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# define road dimensions
ROAD_WIDTH = 60
ROAD_LENGTH = 300
INTERSECTION_SIZE = 100

# create roads
road1 = pygame.Rect((WIDTH - ROAD_WIDTH) / 2, 0, ROAD_WIDTH, ROAD_LENGTH)
road2 = pygame.Rect((WIDTH - ROAD_WIDTH) / 2, HEIGHT - ROAD_LENGTH, ROAD_WIDTH, ROAD_LENGTH)
road3 = pygame.Rect(0, (HEIGHT - ROAD_WIDTH) / 2, ROAD_LENGTH, ROAD_WIDTH)
road4 = pygame.Rect(WIDTH - ROAD_LENGTH, (HEIGHT - ROAD_WIDTH) / 2, ROAD_LENGTH, ROAD_WIDTH)
road5 = pygame.Rect((WIDTH - INTERSECTION_SIZE) / 2, (HEIGHT - INTERSECTION_SIZE) / 2, INTERSECTION_SIZE, INTERSECTION_SIZE)

# create intersections
intersection1 = pygame.Rect((WIDTH - INTERSECTION_SIZE) / 2, 0, INTERSECTION_SIZE, INTERSECTION_SIZE)
intersection2 = pygame.Rect((WIDTH - INTERSECTION_SIZE) / 2, HEIGHT - INTERSECTION_SIZE, INTERSECTION_SIZE, INTERSECTION_SIZE)
intersection3 = pygame.Rect(0, (HEIGHT - INTERSECTION_SIZE) / 2, INTERSECTION_SIZE, INTERSECTION_SIZE)
intersection4 = pygame.Rect(WIDTH - INTERSECTION_SIZE, (HEIGHT - INTERSECTION_SIZE) / 2, INTERSECTION_SIZE, INTERSECTION_SIZE)

# create traffic signals
signal1 = pygame.Rect((WIDTH - INTERSECTION_SIZE) / 2, (HEIGHT - INTERSECTION_SIZE) / 2 - 20, 20, 20)
signal2 = pygame.Rect((WIDTH - INTERSECTION_SIZE) / 2 + INTERSECTION_SIZE, (HEIGHT - INTERSECTION_SIZE) / 2, 20, 20)
signal3 = pygame.Rect((WIDTH - INTERSECTION_SIZE) / 2, (HEIGHT - INTERSECTION_SIZE) / 2 + INTERSECTION_SIZE, 20, 20)
signal4 = pygame.Rect((WIDTH - INTERSECTION_SIZE) / 2 - 20, (HEIGHT - INTERSECTION_SIZE) / 2, 20, 20)

# draw roads, intersections and signals
def draw_environment():
    win.fill(GREY)
    pygame.draw.rect(win, WHITE, road1)
    pygame.draw.rect(win, WHITE, road2)
    pygame.draw.rect(win, WHITE, road3)
    pygame.draw.rect(win, WHITE, road4)
    pygame.draw.rect(win, WHITE, road5)
    pygame.draw.rect(win, GREY, intersection1)
    pygame.draw.rect(win, GREY, intersection2)
    pygame.draw.rect(win, GREY, intersection3)
    pygame.draw.rect(win, GREY, intersection4)
    pygame.draw.rect(win, RED, signal1)
    pygame.draw.rect(win, GREEN, signal2)
    pygame.draw.rect(win, RED, signal3)
    pygame.draw.rect(win, GREEN, signal4)
    pygame.display.update()

# game loop
run = True
