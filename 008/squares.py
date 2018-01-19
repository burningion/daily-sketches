import pygame
import random
import time
import math

class Square(object):
    def __init__(self):
        self.center = [690, 360]
        self.rotation = 0
        self.scale = 1.0
        self.length = 500

    def as_lines(self):
        return [rotatePoint(self.center[0] + self.length // 2 * self.scale,
                            self.center[1] + self.length // 2 * self.scale,
                            self.center[0], self.center[1], self.rotation),
                rotatePoint(self.center[0] - self.length // 2 * self.scale,
                            self.center[1] + self.length // 2 * self.scale,
                            self.center[0], self.center[1], self.rotation),
                rotatePoint(self.center[0] - self.length // 2 * self.scale,
                            self.center[1] - self.length // 2 * self.scale,
                            self.center[0], self.center[1], self.rotation),
                rotatePoint(self.center[0] + self.length // 2 * self.scale,
                            self.center[1] - self.length // 2 * self.scale,
                            self.center[0], self.center[1], self.rotation)]

def setup(screen, etc):
    pass

def radians(degrees):
    return math.pi * degrees / 180

def rotatePoint(x1, y1, x2, y2, rotate):
    '''
    Rotates around x1, y2 by rotate degrees
    '''
    inRadians = radians(rotate)
    nx = math.cos(inRadians) * (x1 - x2) - math.sin(inRadians) * (y1 - y2) + x2
    ny = math.sin(inRadians) * (x1 - x2) + math.cos(inRadians) * (y1 - y2) + y2
    return [int(nx), int(ny)]

counter = 0
squares = [Square(), Square(), Square(), Square()]

def draw(screen, etc):
    global counter
    counter += 1
    for j, square in enumerate(squares):
        square.rotation = getattr(etc, "knob%i" % (j + 1)) * 360
        square.scale = getattr(etc, "knob%i" % (j + 5)) * 2 * math.sin(time.time() * .4)
        pygame.draw.lines(screen, (255, 255, 255), True,
                            square.as_lines())
    
