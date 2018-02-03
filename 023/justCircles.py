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
    numMove = len(glob.glob('walkdataSq/*.json'))
    for i in range(numMove):
        if os.path.exists('walkdataSq/squareDance_%012d_keypoints.json' % i):
            points = json.load(open('walkdataSq/squareDance_%012d_keypoints.json' % i))
            if len(points['people']) >= 1:
                people = []
                for k in range(len(points['people'])):
                    person = []
                    for j in range(18):
                        person.append([int(points['people'][k]['pose_keypoints'][j * 3] * 2 + 300),
                                       int(points['people'][k]['pose_keypoints'][j * 3 + 1] * 2),
                                       points['people'][k]['pose_keypoints'][j * 3 + 2]])
                    people.append(person)
                pointseq.append(people)
            else:
                pointseq.append([])

counter = 100

def draw(screen, etc):
    # our current animation loop frame
    global counter
    color = (92, 192, 190)
    halfSies = list((c // 2 for c in color))

    maxy = len(pointseq) - 100
    currentPose = pointseq[counter % maxy + 100]
    #currentImage = pygame.image.load('labeled/C0396_%012d_rendered.png' % (counter % len(pointseq)))
    
    #screen.blit(pygame.transform.smoothscale(currentImage, (1920, 1080)), (0,0))
    counter += 1
    
    for j in range(len(currentPose)):
        for i, k in enumerate(currentPose[j]):
            if len(k) > 1:
                for l in range(5):
                    color = (halfSies[0] + int(halfSies[0] - 40 * math.sin(i * .21 + time.time())),
                             halfSies[1] + int(halfSies[1] - 40 * math.sin(i * .32 + time.time())),
                             halfSies[2] + int(halfSies[2] - 40 * math.sin(i * .74 + time.time())))
                    try:
                        pygame.draw.circle(screen, color,  (pointseq[counter % maxy + l][j][i][0], pointseq[counter % maxy + l][j][i][1]), int(20 + 10 * math.sin(i * .12 * time.time())))
                    except:
                        continue
