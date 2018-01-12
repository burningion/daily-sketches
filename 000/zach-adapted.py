import pygame
import random
import time
import math

# original code adapted from zach lieberman's talk
# https://www.youtube.com/watch?v=bmztlO9_Wvo

def setup(screen, etc):
    pass

def draw(screen, etc):
    for i in range(int(600 + 400 * math.sin(time.time()))):
        color = (int(127 + 127 * math.sin(i * .01 + time.time())),
                 int(127 + 127 * math.sin(i * .015 + time.time())),
                 int(127 + 127 * math.sin(i * .02 + time.time())))
        radius = int(50 + 40 * math.sin(i * .005 + time.time()))
        xpos = int(1280 // 2 + 100 * math.sin(i * .02 + time.time()))
        pygame.gfxdraw.filled_circle(screen,
                                     xpos,
                                     i,
                                     radius,
                                     color)
        pygame.gfxdraw.filled_circle(screen,
                                     xpos - 300,
                                     i,
                                     radius,
                                     color)
        pygame.gfxdraw.filled_circle(screen,
                                     xpos + 300,
                                     i,
                                     radius,
                                     color)

        pygame.gfxdraw.filled_circle(screen,
                                     xpos - 300,
                                     720 - i,
                                     radius,
                                     color)
        pygame.gfxdraw.filled_circle(screen,
                                     xpos + 300,
                                     720 - i,
                                     radius,
                                     color)
        pygame.gfxdraw.filled_circle(screen,
                                     xpos,
                                     720 - i,
                                     radius,
                                     color)
