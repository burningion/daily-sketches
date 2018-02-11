import argparse

import cv2
from imutils.video import VideoStream
from imutils import face_utils, translate, resize

import time
import dlib

import numpy as np

import math
import random

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

            # eye midpoints 
            leftMidPoint = ((shape[41][0] + shape[38][0]) // 2, (shape[41][1] + shape[38][1]) // 2)
            rightMidPoint = ((shape[47][0] + shape[44][0]) // 2, (shape[47][1] + shape[44][1]) // 2)

            faceDist = math.sqrt((shape[0][0] - shape[16][0]) ** 2 + (shape[0][1] - shape[16][1]) ** 2)
            

            leftEye = tuple(shape[37])
            rightEye = tuple(shape[45])

            leftCutOff = tuple(shape[3])
            rightCutOff = tuple(shape[13])

            # distance between both cheekbones
            dist = math.sqrt((shape[16][0] - shape[0][0]) ** 2 + (shape[16][1] - shape[0][1]) ** 2)

            # cosine wave eyes
            scaleW = int(dist * .20)
            scaleS = abs(math.cos(time.time() * .5))
            scaleB = int(dist * .05 * scaleS + 2)

            hairVector = shape[27] - shape[28]
            noseSlope = slope(shape[28], shape[27])

            if noseSlope == 0:
                hairPoint = (shape[27][0] , int(shape[27][1] - faceDist / 1.2))
            else:
                rotateRad = math.atan(noseSlope)
                if rotateRad < 0:
                    hairPoint = rotate(shape[27], (shape[27][0] + int(faceDist / 1.2), shape[27][1]), rotateRad)
                else:
                    hairPoint  = rotate(shape[27], (shape[27][0] - int(faceDist / 1.2), shape[27][1]), rotateRad)

            # the 16 is for antialiased line in cv2, -1 is for filled
            cv2.circle(frame, tuple(shape[27]), int(faceDist), (178, 217, 252), -1, 16, 0)
            cv2.line(frame, leftCutOff, rightCutOff, (0, 0, 0), 10, 16, 0)
            cv2.circle(frame, leftMidPoint, scaleW, (255,255,255), -1, 16, 0)
            cv2.circle(frame, rightMidPoint, scaleW, (255,255,255), -1, 16, 0)
            cv2.circle(frame, leftMidPoint, scaleB, (0, 0, 0), -1, 16, 0)
            cv2.circle(frame, rightMidPoint, scaleB, (0, 0, 0), -1, 16, 0)
            #cv2.circle(frame, hairPoint, 20, (0, 0, 0), -1, 16, 0)
            cv2.putText(frame, '*', hairPoint, font, 4, (0,0,0), 2, cv2.LINE_AA)
            
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
