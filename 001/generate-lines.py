from PIL import Image
from noise import snoise2, pnoise1

import numpy as np
import random

import argparse
import math

import time
import os

a = Image.new('RGB', (1280, 720), (0, 0, 0))

colors = [(255, 191, 0)]
b = a.load()

input = Image.open('make.png')
bin = input.load()

vector_scale = 0.015
timer = 0

initial = []

for x in range(0, a.width - 1, 7):
    for y in range(0, a.height - 1, 7):
        if (bin[x,y][0] > 100):
            xx = float(x)
            yy = float(y)
            initial.append([xx + snoise2(x / 16.0, y / 16.0, 1) * .08,
                            yy + snoise2(x / 16.0, y / 16.0, 1) * .08])

ready = np.array(initial)

def addColorOpacity(og, new, opacity):
    og1 = np.array(og, dtype=np.float32)
    new1 = np.array(new, dtype=np.float32)

    blended = np.array((1.0 - opacity) * og1 + opacity * new1, dtype=int)
    return tuple(blended)

for i in range(2000):
    counter = 0
    for vec in ready:
        xx = ready[counter][0]
        yy = ready[counter][1]
        n =  snoise2(xx / 16.0, yy / 16.0, 2) * np.pi * 2.0 #* random.uniform(-2, 2)
        delta = np.array([np.cos(n), np.sin(n)])
        ready[counter] = ready[counter] + delta * vector_scale # * random.uniform(-10, 10)
        if xx > 1279 or yy > 719:
            continue
        elif xx < 0 or yy < 0:
            continue
        b[xx, yy] = addColorOpacity(b[xx, yy], random.choice(colors), .15)
        counter += 1
    if i % 10 == 0:
        print("On number %i" % i)
        a.save('imageseq/%05d.jpg' % timer)
        timer += 1
a.save('images/out.jpg')
 

input = Image.open('art.png')
bin = input.load()

colors = [(232, 63, 11)]
vector_scale = 0.015
timer = 0

initial = []

for x in range(0, a.width - 1, 7):
    for y in range(0, a.height - 1, 7):
        if (bin[x,y][0] > 100):
            xx = float(x)
            yy = float(y)
            initial.append([xx + snoise2(x / 16.0, y / 16.0, 1) * .08,
                            yy + snoise2(x / 16.0, y / 16.0, 1) * .08])

ready = np.array(initial)

for i in range(2000):
    counter = 0
    for vec in ready:
        xx = ready[counter][0]
        yy = ready[counter][1]
        n =  snoise2(xx / 16.0, yy / 16.0, 2) * np.pi * 2.0 #* random.uniform(-2, 2)
        delta = np.array([np.cos(n), np.sin(n)])
        ready[counter] = ready[counter] + delta * vector_scale # * random.uniform(-10, 10)
        if xx > 1279 or yy > 719:
            continue
        elif xx < 0 or yy < 0:
            continue
        b[xx, yy] = addColorOpacity(b[xx, yy], random.choice(colors), .15)
        counter += 1
    if i % 10 == 0:
        print("On number %i" % i)
        a.save('imageseq/%05d.jpg' % (timer + 200))
        timer += 1
a.save('images/out2.jpg')
 

input = Image.open('with.png')
bin = input.load()

colors = [(34, 116, 165)]
vector_scale = 0.015
timer = 0

initial = []

for x in range(0, a.width - 1, 7):
    for y in range(0, a.height - 1, 7):
        if (bin[x,y][0] > 100):
            xx = float(x)
            yy = float(y)
            initial.append([xx + snoise2(x / 16.0, y / 16.0, 1) * .08,
                            yy + snoise2(x / 16.0, y / 16.0, 1) * .08])

ready = np.array(initial)

for i in range(2000):
    counter = 0
    for vec in ready:
        xx = ready[counter][0]
        yy = ready[counter][1]
        n =  snoise2(xx / 16.0, yy / 16.0, 2) * np.pi * 2.0 #* random.uniform(-2, 2)
        delta = np.array([np.cos(n), np.sin(n)])
        ready[counter] = ready[counter] + delta * vector_scale # * random.uniform(-10, 10)
        if xx > 1279 or yy > 719:
            continue
        elif xx < 0 or yy < 0:
            continue
        b[xx, yy] = addColorOpacity(b[xx, yy], random.choice(colors), .15)
        counter += 1
    if i % 10 == 0:
        print("On number %i" % i)
        a.save('imageseq/%05d.jpg' % (timer + 400))
        timer += 1
a.save('images/out3.jpg')
 

input = Image.open('python.png')
bin = input.load()

colors = [(220, 220, 221)]
vector_scale = 0.03
timer = 0

initial = []

for x in range(0, a.width - 1, 7):
    for y in range(0, a.height - 1, 7):
        if (bin[x,y][0] > 100):
            xx = float(x)
            yy = float(y)
            initial.append([xx + snoise2(x / 16.0, y / 16.0, 1) * .08,
                            yy + snoise2(x / 16.0, y / 16.0, 1) * .08])

ready = np.array(initial)

for i in range(2000):
    counter = 0
    for vec in ready:
        xx = ready[counter][0]
        yy = ready[counter][1]
        n =  snoise2(xx / 16.0, yy / 16.0, 2) * np.pi * 2.0 #* random.uniform(-2, 2)
        delta = np.array([np.cos(n), np.sin(n)])
        ready[counter] = ready[counter] + delta * vector_scale # * random.uniform(-10, 10)
        if xx > 1279 or yy > 719:
            continue
        elif xx < 0 or yy < 0:
            continue
        b[xx, yy] = addColorOpacity(b[xx, yy], random.choice(colors), .15)
        counter += 1
    if i % 10 == 0:
        print("On number %i" % i)
        a.save('imageseq/%05d.jpg' % (timer + 600))
        timer += 1
a.save('images/out4.jpg')
 
