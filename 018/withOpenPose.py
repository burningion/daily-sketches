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
    numMove = len(glob.glob('walkdata/*.json'))
    for i in range(numIn):
            if os.path.exists('gifready/%05d.png' % (i + 1)):
                imagey = pygame.image.load('gifready/%05d.png' % (i + 1)).convert_alpha()
                imageseq.append(imagey)
    for i in range(numMove):
        if os.path.exists('walkdata/%05d_keypoints.json' % i):
            points = json.load(open('walkdata/%05d_keypoints.json' % i))
            if len(points['people']) >= 1 and points['people'][0]['pose_keypoints'][14] > 0.5:
                currentSeq = []
                for i in range(18):
                    currentSeq.append([points['people'][0]['pose_keypoints'][i * 3],
                                        points['people'][0]['pose_keypoints'][i * 3 + 1]])
                pointseq.append(currentSeq)
            else:
                pointseq.append([])

counter = 1
movieLength = len(glob.glob('labeled/*.png')) - 1

def draw(screen, etc):
    # our current animation loop frame
    global counter
    current0 = imageseq[counter % len(imageseq)]
    currentPose = pointseq[counter % len(pointseq)]

    currentFrame = counter % (movieLength - 1) + 1
    curframe = pygame.image.load('labeled/%05d_rendered.png' % currentFrame)
    
    screen.blit(pygame.transform.smoothscale(curframe, (1920, 1080)), (0,0))
    counter += 1
    if len(currentPose) < 2:
        return
        
    for j in range(3,5):
        dist = (int(abs(currentPose[j][0] - currentPose[j - 1][0])),
                int(abs(currentPose[j][1] - currentPose[j - 1][1])))
        newArm = pygame.transform.smoothscale(current0, [100, dist[1] + dist[0]])
        rot = math.degrees(math.atan2(dist[1], dist[0]))
        newArm = pygame.transform.rotate(newArm, 90 - rot)
        screen.blit(newArm, (int(currentPose[j - 1][0] - dist[0] // 2),
                             int(currentPose[j - 1][1])))
    # right hand
    for j in range(6, 8):
        dist = (int(abs(currentPose[j][0] - currentPose[j - 1][0])),
                int(abs(currentPose[j][1] - currentPose[j - 1][1])))
        newArm = pygame.transform.smoothscale(current0, [100, dist[1] + dist[0]])
        rot = math.degrees(math.atan2(dist[1], dist[0]))
        newArm = pygame.transform.rotate(newArm, 90 - rot)
        screen.blit(newArm, (int(currentPose[j - 1][0] - dist[0] // 2),
                             int(currentPose[j - 1][1])))

        # left leg
        for j in range(9, 11):
            dist = (int(abs(currentPose[j][0] - currentPose[j - 1][0])),
                    int(abs(currentPose[j][1] - currentPose[j - 1][1])))
            newArm = pygame.transform.smoothscale(current0, [100, dist[1] + dist[0]])
            rot = math.degrees(math.atan2(dist[1], dist[0]))
            newArm = pygame.transform.rotate(newArm, 90 - rot)
            screen.blit(newArm, (int(currentPose[j - 1][0] - 50),
                                 int(currentPose[j - 1][1])))
        # right leg
        for j in range(12, 14):
            dist = (int(abs(currentPose[j][0] - currentPose[j - 1][0])),
                    int(abs(currentPose[j][1] - currentPose[j - 1][1])))
            newArm = pygame.transform.smoothscale(current0, [100, dist[1] + dist[0]])
            rot = math.degrees(math.atan2(dist[1], dist[0]))
            newArm = pygame.transform.rotate(newArm, 90 - rot)
            screen.blit(newArm, (int(currentPose[j - 1][0] - 50),
                                 int(currentPose[j - 1][1])))
