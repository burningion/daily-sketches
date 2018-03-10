import argparse

import cv2
from imutils.video import VideoStream
from imutils import face_utils, translate, resize

import time
import dlib

import numpy as np

import math
import random

from PIL import Image

im =Image.open('background.jpg').convert('RGB')
copyIm = np.array(im)
copyIm = copyIm[:,:,::-1].copy()

parser = argparse.ArgumentParser()
parser.add_argument("-predictor", required=True, help="path to predictor")
args = parser.parse_args()

print("starting program.")
print("'s' starts drawing eyes.")
print("'r' to toggle recording image, and 'q' to quit")

cam = VideoStream()
cam.stream.stream.set(3, 1280)
cam.stream.stream.set(4, 720)
vs = cam.start()

time.sleep(.5)

# this detects our face
detector = dlib.get_frontal_face_detector()
# and this predicts our face's orientation
predictor = dlib.shape_predictor(args.predictor)

recording = False
counter = 0

# get our first frame outside of loop, so we can see how our
# webcam resized itself, and it's resolution w/ np.shape
frame = vs.read()
#frame = resize(frame, width=800)
eyeSnake = False

def slope(p1, p2):
    if (p2[0] - p1[0]) == 0:
        return 0.0
    else:
        return float((p2[1] - p1[1]) / (p2[0] - p1[0]))

def rotate(origin, point, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.

    The angle should be given in radians.
    """
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return int(qx), int(qy)

font = cv2.FONT_HERSHEY_PLAIN

while True:
    # read a frame from webcam, resize to be smaller
    frame = vs.read()
    #frame = resize(frame, width=800)

    # the detector and predictor expect a grayscale image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rects = detector(gray, 0)
    # if we're running the eyesnake loop (press 's' while running to enable)
    if eyeSnake:
        for rect in rects:
            # the predictor is our 68 point model we loaded
            shape = predictor(gray, rect)
            shape = face_utils.shape_to_np(shape)

            # our dlib model returns 68 points that make up a face.
            # the left eye is the 36th point through the 42nd. the right
            # eye is the 42nd point through the 48th.

            mask = Image.new('L', (1280, 720))
            mask = np.array(mask)

            # the 16 is for antialiased line in cv2, -1 is for filled
            #cv2.circle(frame, tuple(shape[27]), int(faceDist), (178, 217, 252), -1, 16, 0)
            cv2.line(mask, tuple(shape[0]), tuple(shape[16]), (255, 255, 255), 50, 16, 0)
            cv2.line(mask, tuple(shape[1]), tuple(shape[15]), (255, 255, 255), 50, 16, 0)
            cv2.line(mask, tuple(shape[2]), tuple(shape[14]), (255), 50, 16, 0)
            cv2.line(mask, tuple(shape[3]), tuple(shape[13]), (255), 50, 16, 0)
            cv2.line(mask, tuple(shape[4]), tuple(shape[12]), (255), 50, 16, 0)
            cv2.line(mask, tuple(shape[5]), tuple(shape[11]), (255), 50, 16, 0)
            cv2.line(mask, tuple(shape[6]), tuple(shape[10]), (255), 50, 16, 0)
            cv2.line(mask, tuple(shape[7]), tuple(shape[9]), (255), 50, 16, 0)
            cv2.line(mask, tuple(shape[7]), tuple(shape[8]), (255), 50, 16, 0)
            cv2.line(mask, tuple(shape[17]), tuple(shape[26]), (255), 50, 16, 0)
            copierIm = cv2.bitwise_and(copyIm, copyIm, mask=mask)
            frame = cv2.bitwise_and(frame, frame, mask=255-mask)
            frame += copierIm
            
            # display the current frame, and check to see if user pressed a key
    cv2.imshow("eye glitch", frame)
    key = cv2.waitKey(1) & 0xFF

    if recording:
        # create a directory called "image_seq", and we'll be able to create gifs in ffmpeg
        # from image sequences
        cv2.imwrite("imageseq/%05d.jpg" % counter, frame)
        counter += 1

    if key == ord("q"):
        break

    if key == ord("s"):
        eyeSnake = not eyeSnake

    if key == ord("r"):
        recording = not recording

cv2.destroyAllWindows()
vs.stop()
