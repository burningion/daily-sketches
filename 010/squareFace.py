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
predictor = dlib.shape_predictor('shape_predictor_68.dat')


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
        newSurface = pygame.image.fromstring(newIm.tobytes(), newIm.size, newIm.mode).convert_alpha()
        faces.append(newSurface)
        
    if faces:
        for j, square in enumerate(squares):
            face = faces[j % len(faces)]
            square.rotation = getattr(etc, "knob%i" % (j + 1)) * 360
            square.scale = abs(getattr(etc, "knob%i" % (j + 5)) * 2 * math.sin(time.time() * .4)) + .2
            for place in square.as_lines():
                screen.blit(face, place)
            for place in square.inner_square(etc.knob9 * square.length):
                screen.blit(face, place)
