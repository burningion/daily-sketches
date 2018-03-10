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

numFiles = len(glob.glob('extractGif/*.jpg'))
counter = 0

for i in range(1, numFiles):
    filename = 'extractGif/%05d.jpg' % i
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
                humansM = r['masks'][:,:,b] * 255
                y1, x1, y2, x2 = r['rois'][b]
                humansCut = frame[y1:y2, x1:x2]
                humansCut = cv2.cvtColor(humansCut.astype(np.uint8), cv2.COLOR_BGR2RGBA)
                humansCut[:,:,3] = humansM[y1:y2, x1:x2]
                humans.append(humansCut)

    if len(humans) >= 1:
        counter += 1

    for j, human in enumerate(humans):
        fileout = 'giffer%i/%05d.png' % (j, counter)
        if not os.path.exists('giffer%i' % j):
            os.makedirs('giffer%i' % j)
        print(fileout)
        #frame = cv2.cvtColor(frame.astype('uint8'), cv2.COLOR_BGRA2BGR)
        imageio.imwrite(fileout, human)
