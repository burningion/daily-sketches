import numpy as np
import os
import coco
import model as modellib
import glob

import imageio
import cv2

# Root directory to project
ROOT_DIR = os.getcwd()

# Directory to save logs and trained model
MODEL_DIR = os.path.join(ROOT_DIR, "logs")

# Path to trained weights file
# Download this file and place in the root of your 
# project (See README file for details)
COCO_MODEL_PATH = os.path.join(ROOT_DIR, "mask_rcnn_coco.h5")

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

numFiles = len(glob.glob('kickflip/*.png'))
counter = 0

for i in range(1, numFiles):
    filename = 'kickflip/%05d.png' % i
    print("doing frame %s" % filename)
    frame = cv2.imread(filename)
    
    results = model.detect([frame], verbose=0)
    r = results[0]
    masky = np.zeros((frame.shape[0], frame.shape[1]), dtype='uint8')
    humans = []
    if r['rois'].shape[0] >= 1:
        for b in range(r['rois'].shape[0]):
            if r['class_ids'][b] == class_names.index('person'):
                masky += r['masks'][:,:,b] * 255
                _, thresh = cv2.threshold(masky, 127, 255, 0)
                hierarchy, contours, _ = cv2.findContours(thresh, 1, 2)
                cnt = contours[0]
                epsilon = 0.01*cv2.arcLength(cnt,True)
                approx = cv2.approxPolyDP(cnt, epsilon, True)

                # svg write out from
                # https://stackoverflow.com/questions/43108751/convert-contour-paths-to-svg-paths
                c = max(contours, key=cv2.contourArea) #max contour
                f = open('kickflipSVG/%05d.svg' % counter, 'w+')
                f.write('<svg width="'+str(masky.shape[1])+'" height="'+str(masky.shape[0])+'" xmlns="http://www.w3.org/2000/svg">')
                f.write('<path d="M')

                for i in range(len(c)):
                    #print(c[i][0])
                    x, y = c[i][0]
                    print(x)
                    f.write(str(x)+  ' ' + str(y)+' ')

                f.write('"/>')
                f.write('</svg>')
                f.close()
                humans.append(masky)

    if len(humans) >= 1:
        counter += 1

    for j, human in enumerate(humans):
        fileout = 'kickflipOut/%05d.png' % counter
        print(fileout)
        imageio.imwrite(fileout, human)
