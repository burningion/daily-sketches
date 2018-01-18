import pygame
import random
import time
import math


def setup(screen, etc):
    pass

def drawCircle(screen, x, y, r, n):
    color = (int(123 + 123 * math.sin(r * .01 + time.time())),
             int(123 + 123 * math.sin(r * .011 + time.time())),
             int(123 + 123 * math.sin(r * .012 + time.time())))

    if r > 3:
        pygame.draw.circle(screen,
                           color,
                           (int(x), int(y)),
                           int(r * 2),
                           3)
    if n > 1:
        n = n - 1
        drawCircle(screen, x - r / 2, y, r / 2, n)
        drawCircle(screen, x + r / 2, y, r / 2, n)

counter = 0

def draw(screen, etc):
    global counter
    counter += 1
    drawCircle(screen, 1280 // 2, 360 - 30, 300 + 100 * math.sin(counter * .01), int(9 + 6 * math.sin(counter * .05)))
    drawCircle(screen, 1280 // 2, 360 + 30, 300 + 100 * math.sin(counter * .01), int(9 + 6 * math.sin(counter * .05)))
