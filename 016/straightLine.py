import pygame
import random
import time
import math
import os
import glob

imageseq = []
def setup(screen, etc):
    global imageseq
    numIn = len(glob.glob('wave-input/*.png'))
    for i in range(numIn):
            if os.path.exists('wave-input/%05d.png' % (i + 1)):
                imagey = pygame.image.load('wave-input/%05d.png' % (i + 1)).convert_alpha()
                imageseq.append(imagey)

counter = 1

def draw(screen, etc):
    # our current animation loop frame
    global counter
    current0 = imageseq[counter % len(imageseq)]
    counter += 1

    for i in range(0, 1920, 200):
        screen.blit(current0, (i, 1080 // 2 - 230))
        
