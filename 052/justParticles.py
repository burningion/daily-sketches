import pygame
import random
import time
import math
import os
import glob

import json
import numpy as np

imageseq = []
pointseq = []


particleList = []

def setup(screen, etc):
    global imageseq, pointseq, mario, mario2
    mario2 = pygame.image.load('bang.png').convert_alpha()
    mario = pygame.transform.smoothscale(mario2, (50, 50))
    mario2 = pygame.transform.smoothscale(mario2, (75, 75))
    numMove = len(glob.glob('walkdataSq/*.json'))
    for i in range(numMove):
        if os.path.exists('walkdataSq/fastflip_%012d_keypoints.json' % i):
            points = json.load(open('walkdataSq/fastflip_%012d_keypoints.json' % i))
            if len(points['people']) >= 1 and points['people'][0]['pose_keypoints'][14] > 0.5:
                currentSeq = []
                for i in range(18):
                    currentSeq.append([int(points['people'][0]['pose_keypoints'][i * 3]),
                                        int(points['people'][0]['pose_keypoints'][i * 3 + 1])])
                pointseq.append(currentSeq)
            else:
                pointseq.append([])

counter = 1

def bressenLine(screen, x0, y0, x1, y1):
    "Adapted version of Bresenham's line algorithm"
    global mario
    deltaX = abs(x1 - x0) 
    deltaY = abs(y1 - y0)

    x, y = x0, y0

    slopeX = -1 if x0 > x1 else 1
    slopeY = -1 if y0 > y1 else 1

    if deltaX > deltaY:
        err = deltaX / 2.0
        while x != x1:
            screen.blit(mario, (x, y))
            err -= deltaY
            if err < 0:
                y += slopeY
                err += deltaX
            x += slopeX
    else:
        err = deltaY / 2.0
        while y != y1:
            screen.blit(mario, (x, y))
            err -= deltaX
            if err < 0:
                x += slopeX
                err += deltaY
            y += slopeY        
    screen.blit(mario, (x, y))

class Particle(object):
    def __init__(self, x, y, filename):
        self.x = int(x)
        self.y = int(y)
        self.y_v = np.random.randint(-50, 50) + 20
        self.x_v = np.random.randint(-50,50) - 20
        self.angle = random.uniform(0, 2.0*math.pi)
        size = random.randint(20,100)
        self.image = pygame.transform.smoothscale(pygame.image.load(filename).convert_alpha(), (size, size))
        self.lifetime = 0

    def draw(self, screen):
        vector = [self.x_v * math.cos(self.angle), self.y_v * math.sin(self.angle)]
        self.x += vector[0]
        self.y += vector[1]
        self.lifetime += 1
        screen.blit(self.image, (self.x, self.y))


def draw(screen, etc):
    # our current animation loop frame
    global counter, mario, mario2, particleList

    currentPose = pointseq[counter % len(pointseq)]
    currentImage = pygame.image.load('imagseqin/%05d.png' % (counter % len(pointseq) + 1))
    screen.blit(currentImage, (0,0))

    counter += 1
    if len(particleList) < 300:
        for i in range(random.randint(1,50)):
            try:
                place = random.randint(1,17)
                b = Particle(currentPose[place][0],currentPose[place][1], random.choice(['bang.png']))
                particleList.append(b)
            except:
                continue
    for p in particleList:
        if p.lifetime % 100 == 0:
            try:
                place = random.randint(1,17)
                p.x = currentPose[place][0]
                p.y = currentPose[place][1]
            except:
                pass
        p.draw(screen)
        if p.x < 0 or p.x > 1920 or p.y < 0 or p.y > 1080:
            try:
                place = random.randint(1,17)
                p.x = currentPose[place][0]
                p.y = currentPose[place][1]
            except:
                pass
    if len(currentPose) < 2:
        return
