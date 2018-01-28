import pygame
import pygame.gfxdraw

# used to import a file name from the command line
import importlib
import argparse

from rtmidi.midiutil import open_midiinput

import os

parser = argparse.ArgumentParser(description="Critter and Guitari ETC program debug environment")
parser.add_argument('module', type=str, help="Filename of the Pygame program to test")
parser.add_argument('midi', type=int, default=-1, nargs='?', help="input midi device to use")
parser.add_argument('-r', '--record', type=int, help="Record out to image sequence for ffmpeg")
args = parser.parse_args()

# imports the actual module we're loading
i = importlib.import_module(args.module.split('.py')[0])

import random
import math

import time

from pygame.color import THECOLORS

clock = pygame.time.Clock()

class MidiInputHandler(object):
    def __init__(self, port, freq):
        self.port = port
        self.base_freq = freq
        self._wallclock = time.time()
        self.knob_vals = [random.random() for i in range(16)]

    def __call__(self, event, data=None):
        global currentFrequency
        message, deltatime = event
        self._wallclock += deltatime
        print("[%s] @%0.6f %r" % (self.port, self._wallclock, message))
        if message[1] >= 16 and message[1] <= 23:
            self.knob_vals[message[1] - 16] = message[2] / 127.0
        if message[1] >= 0 and message[1] <= 7:
            self.knob_vals[message[1] + 8] = message[2] / 127.0

print(args.midi)
if args.midi != -1:
    try:
        midiin, port_name = open_midiinput(args.midi)
    except (EOFError, KeyboardInterrupt):
        exit()
    midiSettings = MidiInputHandler(port_name, 940.0)
    midiin.set_callback(midiSettings)


# initialize to ETC's resolution
screenWidth, screenHeight = 1920, 1080
pygame.init()
screen = pygame.display.set_mode((screenWidth, screenHeight))

# give ourselves some initial values
class ETC(object):
    def __init__(self):
        for i in range(16):
            setattr(self, "knob%i" % (i + 1), random.random())
        
        self.midi_input = False

        self.audio_in = [random.randint(-32768, 32767) for i in range(100)]
        self.bg_color = (0, 0, 0)
        self.audio_trig = False
        self.random_color = THECOLORS[random.choice(list(THECOLORS.keys()))]
        self.midi_note_new = False

    def color_picker(self):
        self.random_color = THECOLORS[random.choice(list(THECOLORS.keys()))]
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
    if args.midi != -1:
        for j, val in enumerate(midiSettings.knob_vals):
            setattr(etc, 'knob%i' % (j + 1), val)
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
    clock.tick(30)
