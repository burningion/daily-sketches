import pygame
import random
import time
import math

import dlib
from PIL import Image, ImageDraw, ImageOps

import cv2

from imutils.video import VideoStream
from imutils import face_utils, translate, rotate, resize

import numpy as np

vs = VideoStream()
vs.stream.stream.set(3, 1280)
vs.stream.stream.set(4, 720)

theCam = vs.start()

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('../010/shape_predictor_68.dat')

class Circle(object):
    def __init__(self):
        self.center = [1280 // 2 - 75, 720 // 2 - 100]
        self.rotation = 0
        self.scale = 1.0
        self.radius = random.randrange(50, 500)
        self.num_points = 10
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
    for j in range(2):
        imageseq.append([])
        for i in range(258):
            imagey = pygame.image.load('../013/human%i/%05d.png' % (j, i + 1)).convert_alpha()
            imageseq[j].append(pygame.transform.smoothscale(imagey, (150, 200)))
    for j in range(9):
        c = Circle()
        c.animation = random.randint(0, len(imageseq) - 1)
        circles.append(c)

def draw(screen, etc):
    global counter
    counter += 1

    # our current animation loop frame
    current0 = imageseq[0][counter % 250]
    current1 = imageseq[1][counter % 250]

    frame = vs.read()
    frame = resize(frame, width=500)
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)

    rects = detector(img_gray, 0)

    faces = []

    og = Image.fromarray(frame)
    for rect in rects:
        newIm = og.crop((rect.left(), rect.top(), rect.right(), rect.bottom()))
        # circle crop stolen from stackoverflow
        # https://stackoverflow.com/questions/890051/how-do-i-generate-circular-thumbnails-with-pil
        bigsize = (newIm.size[0] * 3, newIm.size[1] * 3)
        mask = Image.new('L', bigsize, 0)
        draw = ImageDraw.Draw(mask) 
        draw.ellipse((0, 0) + bigsize, fill=255)
        mask = mask.resize(newIm.size, Image.ANTIALIAS)
        newIm.putalpha(mask)
        bw = newIm.convert('LA')
        bw = bw.convert('RGBA')
        newSurface = pygame.image.fromstring(newIm.tobytes(), newIm.size, newIm.mode).convert_alpha()
        newSurfaceBW = pygame.image.fromstring(bw.tobytes(), bw.size, bw.mode).convert_alpha()
        faces.append([pygame.transform.smoothscale(newSurface, (100, 100)),
                      pygame.transform.smoothscale(newSurfaceBW, (100, 100))])

    if faces:
        b = 0
        for x in range(0, 1280, 100):
            b += 1
            for y in range(0, 720, 100):
                if b % 2 == 0:
                    screen.blit(pygame.transform.smoothscale(faces[0][1],
                                                             (int(100 + 50 * math.sin(x * .1 + time.time())),
                                                              int(100 + 50 * math.sin(x * .1 + time.time())))), (int(x + x // 2 * math.cos(x * .1 + time.time())), y))
                else:
                    scaledFace = pygame.transform.smoothscale(faces[0][1],
                                                             (int(100 + 50 * math.sin(x * .1 + time.time())),
                                                              int(100 + 50 * math.sin(x * .1 + time.time()))))
                    screen.blit(pygame.transform.flip(scaledFace, True, False), (int(x + x // 2 * math.cos(x * .1 + time.time())), y))

        for j, circle in enumerate(circles):
            circle.rotation = getattr(etc, "knob%i" % (j % 4 + 1)) * 360
            circle.scale = abs(getattr(etc, "knob%i" % (j % 4 + 5)) * 5 * math.sin(counter * .0004)) + .2
            for place in circle.as_lines():
                if circle.animation == 0:
                    #screen.blit(pygame.transform.rotate(faces[0][0], place[-1]), tuple(place[:2]))
                    #screen.blit(pygame.transform.rotate(current0, place[-1]), tuple(place[:2]))
                    screen.blit(pygame.transform.rotate(current1, place[-1]), place[:2])
                elif circle.animation == 1:
                    #screen.blit(faces[0][0], place[:2])
                    screen.blit(current1, place[:2])
