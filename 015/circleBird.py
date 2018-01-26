import pygame
import random
import time
import math
import os

class Circle(object):
    def __init__(self):
        self.center = [random.randint(-10, 1280), random.randint(-10, 720)]
        self.rotation = 0
        self.scale = 1.5
        self.radius = random.randrange(50, 500)
        self.num_points = 15
        self.animation = 0

    def as_lines(self):
        points = []
        for i in range(self.num_points):
            angle = i * (360 / self.num_points)
            x = math.cos(math.radians(angle + self.rotation)) * self.radius * self.scale
            y = math.sin(math.radians(angle + self.rotation)) * self.radius * self.scale
            points.append([x + self.center[0], y + self.center[1], 360 - angle + self.rotation])
        return points

class Square(object):
    def __init__(self):
        self.center = [650, 360]
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

    def inner_square(self, distance):
        initial = self.as_lines()
        result = []
        # gets an x, y position of distance away from points on lines of square
        for i in range(3):
            length = math.sqrt((initial[i + 1][0] - initial[i][0]) ** 2 + (initial[i + 1][1] - initial[i][1]) ** 2)
            slope = distance / length
            x1 = slope * initial[i + 1][0] + (1 - slope) * initial[i][0]
            y1 = slope * initial[i + 1][1] + (1 - slope) * initial[i][1]
            result.append([x1, y1])
        # add the last connection, final element to first element
        length = math.sqrt((initial[0][0] - initial[3][0]) ** 2 + (initial[0][1] - initial[3][1]) ** 2)
        slope = distance / length
        x1 = slope * initial[0][0] + (1 - slope) * initial[3][0]
        y1 = slope * initial[0][1] + (1 - slope) * initial[3][1]
        result.append([x1, y1])
        return result

# stolen from
# http://code.activestate.com/recipes/577575-scale-rectangle-while-keeping-aspect-ratio/
def scale(w, h, x, y, maximum=True):
        nw = y * w / h
        nh = x * h / w
        if maximum ^ (nw >= x):
                return int(nw or 1), int(y)
        return int(x), int(nh or 1)

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
#squares = [Square(), Square(), Square(), Square()]
circles = []
imageseq = []

def setup(screen, etc):
    global imageseq, circles
    for j in range(3):
        imageseq.append([])
        for i in range(258):
            if os.path.exists('bird%i/%05d.png' % (j, i + 1)):
                imagey = pygame.image.load('bird%i/%05d.png' % (j, i + 1)).convert_alpha()
                og_size = imagey.get_size()
                new_size = scale(200, 200, og_size[0], og_size[1], True)
                imageseq[j].append(pygame.transform.smoothscale(imagey, new_size))
            
    for j in range(100):
        c = Circle()
        c.animation = random.choice([0, 1, 2])
        circles.append(c)

def draw(screen, etc):
    global counter
    counter += 1

    # our current animation loop frame
    current0 = imageseq[0][counter % len(imageseq[0])]
    current1 = imageseq[1][counter % len(imageseq[1])]
    current2 = imageseq[2][counter % len(imageseq[2])]
    
    for j, circle in enumerate(circles):
        circle.rotation = getattr(etc, "knob%i" % (j % 4 + 1)) * 360
        circle.scale = abs(getattr(etc, "knob%i" % (j % 4 + 5)) * 5 * math.sin(counter * .0004)) + .2
        for place in circle.as_lines():
            if circle.animation == 0:
                #screen.blit(pygame.transform.rotate(faces[0][0], place[-1]), tuple(place[:2]))
                #screen.blit(pygame.transform.rotate(current0, place[-1]), tuple(place[:2]))
                screen.blit(current0, place[:2])
            elif circle.animation == 1:
                #screen.blit(faces[0][0], place[:2])
                screen.blit(current1, place[:2])
            elif circle.animation == 2:
                #screen.blit(faces[0][0], place[:2])
                screen.blit(current2, place[:2])
