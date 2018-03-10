from PIL import Image, ImageDraw
import glob
import math
import time

numFiles = len(list(glob.glob('imageseqin/*.jpg')))

imageWidth, imageHeight = 1280, 720
x1 = imageWidth // 2 - imageWidth // 4
y1 = 0

x2 = imageWidth // 2 + imageWidth // 4
y2 = x2 - x1 # make a perfect circle

xW = x2 - x1
yW = y2 - y1

initialPoints = [x1, y1, x1 + xW, y1 + yW]

def radians(degrees):
    return math.pi * degrees / 180

def rotatePoint(x1, y1, x2, y2, rotate):
    '''
    Rotates around x1, y2 by rotate degrees
    '''
    inRadians = radians(rotate)
    nx = math.cos(inRadians) * (x1 - x2) - math.sin(inRadians) * (y1 - y2) + x2
    ny = math.sin(inRadians) * (x1 - x2) + math.cos(inRadians) * (y1 - y2) + y2
    return (int(nx), int(ny))

counter = 1

trianglePoints = [(imageWidth // 5, 180), (imageWidth // 5 - imageWidth // 6, 540), (imageWidth // 5 + imageWidth // 6, 540)]

trianglePoints1 = [(imageWidth // 5 * 4, 180), (imageWidth // 5 * 4 - imageWidth // 6, 540), (imageWidth // 5 * 4 + imageWidth // 6, 540)]

for i in range(numFiles):
    img1 = Image.open('imageseqin/%05d.jpg' % (i + 1)).convert('RGBA')
    out = Image.new('RGBA', (imageWidth, imageHeight), color=(0,0,0,255))
    mask = Image.new('L', (imageWidth, imageHeight), color=0)
    draw = ImageDraw.Draw(mask)

    initialPoints[0] = math.cos(counter * .1) * -50 + x1
    initialPoints[1] = y1
    
    initialPoints[2] = math.cos(counter * .1) * 50 + x1 + xW
    initialPoints[3] = math.cos(counter * .1) * 50 + y1 + yW
    draw.ellipse(initialPoints, fill=255)

    p1 = rotatePoint(trianglePoints[0][0], trianglePoints[0][1], trianglePoints[0][0], 360, counter)
    p2 = rotatePoint(trianglePoints[1][0], trianglePoints[1][1], trianglePoints[0][0], 360, counter)
    p3 = rotatePoint(trianglePoints[2][0], trianglePoints[2][1], trianglePoints[0][0], 360, counter)
    draw.polygon([p1, p2, p3], fill=255)

    p1 = rotatePoint(trianglePoints1[0][0], trianglePoints1[0][1], trianglePoints1[0][0], 360, 360 - counter)
    p2 = rotatePoint(trianglePoints1[1][0], trianglePoints1[1][1], trianglePoints1[0][0], 360, 360 - counter)
    p3 = rotatePoint(trianglePoints1[2][0], trianglePoints1[2][1], trianglePoints1[0][0], 360, 360 - counter)
    draw.polygon([p1, p2, p3], fill=255)

    out.paste(img1, (0,0), mask=mask)
    out = out.convert('RGB')
    out.save("imageseq/%05d.jpg" % (i + 1))
    counter += 1
