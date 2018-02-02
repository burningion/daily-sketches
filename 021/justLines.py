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
    mario2 = pygame.image.load('mario.png').convert_alpha()
    mario = pygame.transform.smoothscale(mario2, (70, 70))
    mario2 = pygame.transform.smoothscale(mario2, (75, 75))
    numMove = len(glob.glob('walkdata/*.json'))
    for i in range(numMove):
        if os.path.exists('walkdata/C0337_%012d_keypoints.json' % i):
            points = json.load(open('walkdata/C0337_%012d_keypoints.json' % i))
            if len(points['people']) >= 1:
                people = []
                for k in range(len(points['people'])):
                    person = []
                    for j in range(18):
                        if points['people'][k]['pose_keypoints'][j * 3 + 2] > .002:
                            person.append([int(points['people'][k]['pose_keypoints'][j * 3]) - 30,
                                               int(points['people'][k]['pose_keypoints'][j * 3 + 1]) - 30])
                        else:
                            person.append([])
                    people.append(person)
                pointseq.append(people)
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

def drawLine(screen, start, stop):
    if len(start) > 1 and len(stop) > 1:
        bressenLine(screen, start[0], start[1],
                    stop[0], stop[1])
    elif len(start) > 1:
        screen.blit(mario, (start[0], start[1]))
    elif len(stop) > 1:
        screen.blit(mario, (stop[0], stop[1]))

def draw(screen, etc):
    # our current animation loop frame
    global counter, mario, mario2

    currentPose = pointseq[counter % len(pointseq)]
    #currentImage = pygame.image.load('labeled/C0337_%012d_rendered.png' % (counter % len(pointseq)))
    
    #screen.blit(pygame.transform.smoothscale(currentImage, (1920, 1080)), (0,0))
    counter += 1
    if len(currentPose) < 2:
        return

    for j in range(len(currentPose)):
        # nose to neck
        drawLine(screen, currentPose[j][1], currentPose[j][0])
        # neck to left shoulder
        drawLine(screen, currentPose[j][2], currentPose[j][1])
        # neck to right shoulder
        drawLine(screen, currentPose[j][1], currentPose[j][5])
        # left arm
        drawLine(screen, currentPose[j][2], currentPose[j][3])
        drawLine(screen, currentPose[j][3], currentPose[j][4])
        # right arm
        drawLine(screen, currentPose[j][5], currentPose[j][6])
        drawLine(screen, currentPose[j][6], currentPose[j][7])

        # left leg
        drawLine(screen, currentPose[j][8], currentPose[j][1])
        drawLine(screen, currentPose[j][8], currentPose[j][9])
        drawLine(screen, currentPose[j][9], currentPose[j][10])

        drawLine(screen, currentPose[j][11], currentPose[j][1])
        drawLine(screen, currentPose[j][11], currentPose[j][12])
        drawLine(screen, currentPose[j][12], currentPose[j][13])

        if len(currentPose[j][16]) > 1:
            rect = mario.get_rect(center=currentPose[j][16])
            screen.blit(mario, rect)
        if len(currentPose[j][17]) > 1:
            rect = mario.get_rect(center=currentPose[j][17])
            screen.blit(mario, rect)
