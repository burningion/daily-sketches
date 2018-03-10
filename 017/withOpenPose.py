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
    global imageseq, pointseq
    numIn = len(glob.glob('gifready/*.png'))
    for i in range(numIn):
            if os.path.exists('gifready/%05d.png' % (i + 1)):
                imagey = pygame.image.load('gifready/%05d.png' % (i + 1)).convert_alpha()
                imageseq.append(imagey)
            if os.path.exists('keypoints/%05d_keypoints.json' % i):
                points = json.load(open('keypoints/%05d_keypoints.json' % i))
                print(points)
                if len(points['people']) >= 1 and points['people'][0]['pose_keypoints'][14] > 0.5:
                    rightElbow = [points['people'][0]['pose_keypoints'][9],
                                  points['people'][0]['pose_keypoints'][10]]
                    rightHand =  [points['people'][0]['pose_keypoints'][12],
                                  points['people'][0]['pose_keypoints'][13]]
                    pointseq.append([rightElbow, rightHand])
                else:
                    pointseq.append([])

# stolen from
# http://code.activestate.com/recipes/577575-scale-rectangle-while-keeping-aspect-ratio/
def scale(w, h, x, y, maximum=True):
        nw = y * w / h
        nh = x * h / w
        if maximum ^ (nw >= x):
                return int(nw or 1), int(y)
        return int(x), int(nh or 1)

counter = 1

def angle(p1, p2):
    xDiff = p2[0] - p1[0]
    yDiff = p2[1] - p1[1]
    return math.degrees(math.atan2(yDiff, xDiff))

def draw(screen, etc):
    # our current animation loop frame
    global counter
    current0 = imageseq[counter % len(imageseq)]
    currentPose = pointseq[counter % len(pointseq)]

    counter += 1

    for i in range(0, 1920, 200):
        screen.blit(current0, (i, 1080 // 2 - 230))
        
        newArm = pygame.transform.smoothscale(current0, (300, 300))
        if len(currentPose) < 2:
            continue
        newAngle = angle(currentPose[1], currentPose[0])
        if newAngle <= 0:
            continue
        print(newAngle)
        newArm = pygame.transform.rotate(newArm, 90 - newAngle)
        screen.blit(newArm, (int(currentPose[1][0]) + i - 150, int(currentPose[1][1]) + 1080 // 2 - 230 - 150))

