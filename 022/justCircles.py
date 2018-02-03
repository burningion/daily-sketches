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
    numMove = len(glob.glob('walkdata/*.json'))
    for i in range(numMove):
        if os.path.exists('walkdata/out_%012d_keypoints.json' % i):
            points = json.load(open('walkdata/out_%012d_keypoints.json' % i))
            if len(points['people']) >= 1:
                people = []
                for k in range(len(points['people'])):
                    person = []
                    for j in range(18):
                        person.append([int(points['people'][k]['pose_keypoints'][j * 3]) - 30,
                                       int(points['people'][k]['pose_keypoints'][j * 3 + 1]) - 30,
                                       points['people'][k]['pose_keypoints'][j * 3 + 2]])
                    people.append(person)
                pointseq.append(people)
            else:
                continue

counter = 1

def draw(screen, etc):
    # our current animation loop frame
    global counter
    color = (92, 192, 190)
    halfSies = list((c // 2 for c in color))

    currentPose = pointseq[counter % len(pointseq)]
    #currentImage = pygame.image.load('labeled/out_%012d_rendered.png' % (counter % len(pointseq)))
    
    #screen.blit(pygame.transform.smoothscale(currentImage, (1920, 1080)), (0,0))
    counter += 1
    
    for j in range(len(currentPose)):
        for i, k in enumerate(currentPose[j]):
            if len(k) > 1:
                color = (halfSies[0] + int(i + halfSies[0] * math.sin(counter * .051 + time.time())),
                         halfSies[1] + int(i + 2 + halfSies[1] * math.sin(counter * .062 + time.time())),
                         halfSies[2] + int(i + 3 + halfSies[2] * math.sin(counter * .094 + time.time())))

                pygame.draw.circle(screen, color,  (k[0], k[1]), max(int(150 * k[2]), 10))
