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

fileCount = len(glob.glob('miniin'))
for i in range(253, 2092):
    filename = 'miniin/%05d.png' % i
    spacename = 'bigflow/%05d.jpg' % i
    print("doing frame %s" % filename)
    frame = cv2.imread(filename)
    
    masked_image = cv2.imread(spacename)
    results = model.detect([frame], verbose=0)
    r = results[0]
    masky = np.zeros((720, 1280), dtype='uint8')
    if r['rois'].shape[0] >= 1:
        for b in range(r['rois'].shape[0]):
            if r['class_ids'][b] == class_names.index('skateboard') or r['class_ids'][b] == class_names.index('person'):
                new_mask = masked_image.copy()
                print('board detected')
                mask = r['masks'][:,:,b] * 255
                masky += mask
        masky = cv2.blur(masky, (3,3), 0)
        try:
            new_mask = cv2.bitwise_and(masked_image, masked_image, mask=masky)
            frame = cv2.bitwise_and(frame, frame, mask=255 - masky)
            frame += new_mask
            
        except:
            pass
    fileout = 'mixmini/%05d.jpg' % i
    print(fileout)
    frame = cv2.cvtColor(frame.astype('uint8'), cv2.COLOR_BGRA2RGB)
    imageio.imwrite(fileout, frame)
