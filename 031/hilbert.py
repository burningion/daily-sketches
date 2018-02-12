from PIL import Image
import cv2
import time
import pylab as pl
from scipy.misc import imresize, imfilter
import turtle


counter = 1

img = pl.flipud(pl.imread("inputImages/%05d.jpg" % counter))
levels = 8
size = 2**levels

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

turtle.setup(img.shape[1], img.shape[0])
img = imfilter(imresize(img, (size, size)), 'blur')

turtle.setworldcoordinates(0, 0, size, -size)
turtle.tracer(1000, 0)


time.sleep(.5)

# hilbert curve turtle code stolen from
# falko's python example on stackoverflow
# https://codegolf.stackexchange.com/questions/36374/redraw-an-image-with-just-one-closed-curve


# define recursive hilbert curve
def hilbert(level, angle = 90):
    global img
    if level == 0:
        return

    if level == 1 and img[int(-turtle.pos()[1]), int(turtle.pos()[0])] > 128:
        turtle.forward(2**level - 1)
    else:
        turtle.right(angle)
        hilbert(level - 1, -angle)
        turtle.forward(1)
        turtle.left(angle)
        hilbert(level - 1, angle)
        turtle.forward(1)
        hilbert(level - 1, angle)
        turtle.left(angle)
        turtle.forward(1)
        hilbert(level - 1, -angle)
        turtle.right(angle)

hilbert(levels)
turtle.update()
ts = turtle.getscreen()
ts.getcanvas().postscript(file='eps/%05d.eps' % counter)

toPNG = Image.open('eps/%05d.eps' % counter)
toPNG = toPNG.resize((1280, 720), Image.BICUBIC)
toPNG.save('imageseq/%05d.png' % counter)

while True:
    counter += 1
    turtle.reset()
    img = pl.flipud(pl.imread("inputImages/%05d.jpg" % counter))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    img = imfilter(imresize(img, (size, size)), 'blur')
    turtle.tracer(1000, 0)

    hilbert(levels)
    turtle.update()
    ts = turtle.getscreen()
    ts.getcanvas().postscript(file="eps/%05d.eps" % counter)

    toPNG = Image.open('eps/%05d.eps' % counter)
    toPNG = toPNG.resize((1280, 720), Image.BICUBIC)
    toPNG.save('imageseq/%05d.png' % counter)

