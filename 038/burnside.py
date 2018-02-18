import numpy as np
import scipy.misc

import os
import coco
import utils
import model as modellib
import visualize
import random
import math

import glob

import imageio
import colorsys

import math
import time
import cv2

from PIL import Image, ImageDraw

from blend_modes import blend_modes

# Root directory of the project
ROOT_DIR = os.getcwd()

# Directory to save logs and trained model
MODEL_DIR = os.path.join(ROOT_DIR, "logs")

# Path to trained weights file
# Download this file and place in the root of your 
# project (See README file for details)
COCO_MODEL_PATH = os.path.join(ROOT_DIR, "mask_rcnn_coco.h5")

# Directory of images to run detection on
IMAGE_DIR = os.path.join(ROOT_DIR, "images")

class InferenceConfig(coco.CocoConfig):
    # Set batch size to 1 since we'll be running inference on
    # one image at a time. Batch size = GPU_COUNT * IMAGES_PER_GPU
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1

config = InferenceConfig()

# Create model object in inference mode.
model = modellib.MaskRCNN(mode="inference", model_dir=MODEL_DIR, config=config)

# Load weights trained on MS-COCO
model.load_weights(COCO_MODEL_PATH, by_name=True)

class_names = ['BG', 'person', 'bicycle', 'car', 'motorcycle', 'airplane',
               'bus', 'train', 'truck', 'boat', 'traffic light',
               'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird',
               'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear',
               'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie',
               'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball',
               'kite', 'baseball bat', 'baseball glove', 'skateboard',
               'surfboard', 'tennis racket', 'bottle', 'wine glass', 'cup',
               'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple',
               'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza',
               'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed',
               'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote',
               'keyboard', 'cell phone', 'microwave', 'oven', 'toaster',
               'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors',
               'teddy bear', 'hair drier', 'toothbrush']

def apply_mask(image, mask, color, place, alpha=0.5):
    """Apply the given mask to the image.
    """
    for c in range(3):
        image[:, :, c] = np.where(mask == 1,
                                  image[:, :, c] *
                                  (1 - alpha) + alpha * (color[c] + color[c] * math.sin(place * .01) * 255),
                                  image[:, :, c])
    return image

def random_colors(N, bright=True):
    """
    Generate random colors.
    To get visually distinct colors, generate them in HSV space then
    convert to RGB.
    """
    brightness = 1.0 if bright else 0.7
    hsv = [(i / N, 1, brightness) for i in range(N)]
    colors = list(map(lambda c: colorsys.hsv_to_rgb(*c), hsv))
    random.shuffle(colors)
    return colors

color = random_colors(1)[0]
alpha = 0.9

numFiles = len(list(glob.glob('burnsidein/*.png')))

counter = 1
imageWidth, imageHeight = 1920, 1080

# rotate bound function comes from adrian rosebrock's great blog:
# https://www.pyimagesearch.com/2017/01/02/rotate-images-correctly-with-opencv-and-python/

def rotate_bound(image, angle):
    # grab the dimensions of the image and then determine the
    # center
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)
 
    # grab the rotation matrix (applying the negative of the
    # angle to rotate clockwise), then grab the sine and cosine
    # (i.e., the rotation components of the matrix)
    M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])
 
    # compute the new bounding dimensions of the image
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))
 
    # adjust the rotation matrix to take into account translation
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY
 
    # perform the actual rotation and return the image
    return cv2.warpAffine(image, M, (nW, nH))

for i in range(346, numFiles - 1):
    filename = 'burnsidein/%05d.png' % i
    print("doing frame %s" % filename)
    frame = cv2.imread(filename)

    # damn vertical video! need to rotate! (thanks adrian!)
    frame = rotate_bound(frame, 90)

    paster = Image.new('RGBA', (imageWidth, imageHeight), color=(0,0,0,0))

    results = model.detect([frame], verbose=0)
    r = results[0]
    masky = np.zeros((imageHeight, imageWidth), dtype='uint8')
    if r['rois'].shape[0] >= 1 and i > 128:
        for b in range(r['rois'].shape[0]):
            if r['class_ids'][b] == class_names.index('skateboard') or r['class_ids'][b] == class_names.index('person'):
                print('board detected')
                mask = r['masks'][:,:,b] * 255
                masky += mask
        masky = cv2.blur(masky, (2,2), cv2.BORDER_TRANSPARENT)

        frame = cv2.cvtColor(frame.astype('uint8'), cv2.COLOR_BGR2RGBA)
        frame = Image.fromarray(frame)
        mask = Image.fromarray(masky)
        paster.paste(frame, mask=mask)

        
        boards = 10
        boardDist = 100
        for j in reversed(range(boards)):
            currentDist = math.cos(counter * .01) * boardDist
            currentDistPaste = currentDist - math.sin(counter * .01) * 50 
            pasterB = paster.resize((int(imageWidth + currentDist * j), int(imageHeight + currentDist * j)))
            maskB = mask.resize((int(imageWidth + currentDist * j), int(imageHeight + currentDist * j)))
            frame.paste(pasterB, (int(-currentDistPaste * j), int(-currentDistPaste * j)), mask=maskB)
    else:
        frame = cv2.cvtColor(frame.astype('uint8'), cv2.COLOR_BGR2RGBA)
        frame = Image.fromarray(frame)
    
    fileout = 'burnsideout/%05d.jpg' % counter
    print(fileout)
    # convert to cv2 image so we can rotate back!
    frame = np.array(frame)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2BGR)
    frame = rotate_bound(frame, -90)
    frame = cv2.cvtColor(frame.astype('uint8'), cv2.COLOR_BGR2RGB)
    frame = Image.fromarray(frame)
    frame.save(fileout)
    counter += 1
