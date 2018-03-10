from PIL import Image
import numpy as np
import glob

skateSeq = []
counter = 1

transLen = len(glob.glob('slideTrans/*.png'))

frames = [89, 107, 141, 152, 178, 198, 234, 250]

for i in range(1, transLen):
    if i in frames:
        imagey = Image.open('slideTrans/%05d.png' % (i))
        imgarr = np.array(imagey, dtype='float64')
        imgarr[:,:,3] = imgarr[:,:,3] * .9
        skateSeq.append(Image.fromarray(imgarr.astype('uint8')))
        imagey.close()

transLen -= 1

videoLen = len(glob.glob('slideIn/*.png'))
for i in range(1, videoLen):
    img = Image.open('slideIn/%05d.png' % i)
    for frame in reversed(frames):
        if i < frame:
            img.paste(skateSeq[frames.index(frame)], (0,0), skateSeq[frames.index(frame)])
    img = img.convert('RGB')
    img.save('imageseq/%05d.jpg' % i)
