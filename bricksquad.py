import pygame
import sys
from pygame.locals import *
import brick

pygame.init()

RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
colors = [RED, ORANGE, YELLOW, GREEN, BLUE]

SPACE = 5

# The following lines of code create and display a pygame window
window = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption("I JUST SPILLED LEAN ON MY BRICKS")
# The following lines of code allocate values to class parameters
brickwidth = (window.get_width() - 50)/9
brickheight = 20
bricksperrow = 9
xPOS = SPACE
yPOS = window.get_height() - brickheight
# This loop draws and places bricks in the pygame window
for x in range(5):
    xPOS = x * (brickwidth + SPACE)
    for y in range(bricksperrow):
        firstbrick = brick.Brick(window, brickheight, brickwidth, colors[x])
        firstbrick.draw(xPOS, yPOS)
        xPOS += SPACE + brickwidth

    yPOS -= brickheight + SPACE
    bricksperrow -= 2


pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()






