import pygame
import random
import time
import math
import os
import glob

import json

imageseq = []
pointseq = []


def setup(screen, etc):
    global imageseq, pointseq, mario, mario2
    mario2 = pygame.image.load('fire.png').convert_alpha()
    mario = pygame.transform.smoothscale(mario2, (50, 50))
    mario2 = pygame.transform.smoothscale(mario2, (75, 75))
    numMove = len(glob.glob('tylerData/*.json'))
    for i in range(numMove):
        if os.path.exists('tylerData/tyler_%012d_keypoints.json' % i):
            points = json.load(open('tylerData/tyler_%012d_keypoints.json' % i))
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

def draw(screen, etc):
    # our current animation loop frame
    global counter, mario, mario2

    currentPose = pointseq[counter % len(pointseq)]
    #currentImage = pygame.image.load('tylerIn/%05d.png' % (counter % len(pointseq) + 1))
    #screen.blit(currentImage, (0,0))
    counter += 1
    if len(currentPose) < 2:
        return
    
    # nose to neck
    bressenLine(screen, currentPose[1][0], currentPose[1][1],
                currentPose[0][0], currentPose[0][1])
    # neck to left shoulder
    bressenLine(screen, currentPose[2][0], currentPose[2][1],
                currentPose[1][0], currentPose[1][1])
    # neck to right shoulder
    bressenLine(screen, currentPose[1][0], currentPose[1][1],
                currentPose[5][0], currentPose[5][1])
    # left arm
    bressenLine(screen, currentPose[2][0], currentPose[2][1],
                currentPose[3][0], currentPose[3][1])
    bressenLine(screen, currentPose[3][0], currentPose[3][1],
                currentPose[4][0], currentPose[4][1])
    # right arm
    bressenLine(screen, currentPose[5][0], currentPose[5][1],
                currentPose[6][0], currentPose[6][1])
    bressenLine(screen, currentPose[6][0], currentPose[6][1],
                currentPose[7][0], currentPose[7][1])

    # left leg
    bressenLine(screen, currentPose[8][0], currentPose[8][1],
                currentPose[1][0], currentPose[1][1])
    bressenLine(screen, currentPose[8][0], currentPose[8][1],
                currentPose[9][0], currentPose[9][1])
    bressenLine(screen, currentPose[9][0], currentPose[9][1],
                currentPose[10][0], currentPose[10][1])

    bressenLine(screen, currentPose[11][0], currentPose[11][1],
                currentPose[1][0], currentPose[1][1])
    bressenLine(screen, currentPose[11][0], currentPose[11][1],
                currentPose[12][0], currentPose[12][1])
    bressenLine(screen, currentPose[12][0], currentPose[12][1],
                currentPose[13][0], currentPose[13][1])
    rect = mario.get_rect(center=currentPose[16])
    screen.blit(mario, rect)
    rect = mario.get_rect(center=currentPose[17])
    screen.blit(mario, rect)
