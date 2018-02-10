import pygame
import pygame.gfxdraw

# used to import a file name from the command line
import importlib
import argparse

import os

parser = argparse.ArgumentParser(description="Critter and Guitari ETC program debug environment")
parser.add_argument('module', type=str, help="Filename of the Pygame program to test")
parser.add_argument('-r', '--record', type=int, help="Record out to image sequence for ffmpeg")
args = parser.parse_args()

# imports the actual module we're loading
i = importlib.import_module(args.module.split('.py')[0])

import random
import math

from pygame.color import THECOLORS

# initialize to ETC's resolution
screenWidth, screenHeight = 1280, 720
pygame.init()
screen = pygame.display.set_mode((screenWidth, screenHeight))

# give ourselves some initial values
class ETC(object):
    def __init__(self):
        self.knob1 = random.random()
        self.knob2 = random.random()
        self.knob3 = random.random()
        self.knob4 = random.random()

        self.audio_in = [random.randint(-32768, 32767) for i in range(100)]
        self.bg_color = (0, 0, 0)
        self.audio_trig = False
        self.random_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        self.midi_note_new = False

    def color_picker(self):
        return self.random_color
etc = ETC()

i.setup(screen, etc)

running = True

recording = False
counter = -1

if args.record:
    recording = True

if recording:
    if not os.path.exists('imageseq'):
        os.makedirs('imageseq')
    counter = 0

while running:
    screen.fill(THECOLORS['black'])
    i.draw(screen, etc)

    key = pygame.key.get_pressed()
    if key[pygame.K_q]:
        exit()
    
    if key[pygame.K_SPACE]:
        etc.audio_trig = True
    if key[pygame.K_z]:
        etc.audio_trig = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # if you try to quit, let's leave this loop
            running = False
    pygame.display.flip()

    if recording and counter < args.record:
        pygame.image.save(screen, "imageseq/%05d.jpg" % counter)
        counter += 1
    elif recording and counter == args.record:
        exit()
