from PIL import Image
import numpy as np
import glob

skateSeq = []
counter = 1

transLen = len(glob.glob('yungTrans/*.png'))

for i in range(1, transLen):
    imagey = Image.open('yungTrans/%05d.png' % (i))
    imgarr = np.array(imagey, dtype='float64')
    imgarr[:,:,3] = imgarr[:,:,3] * .6
    skateSeq.append(Image.fromarray(imgarr.astype('uint8')))
    imagey.close()

transLen -= 1

videoLen = len(glob.glob('yungimageseqin/*.png'))
for i in range(1, videoLen):
    img = Image.open('yungimageseqin/%05d.png' % i)
    if i <= 40 or i >= 120:
        for j in range(50):
            print('doing transparent frame %i' % ((j * 48 + i % transLen) % transLen))
            img.paste(skateSeq[(j * 48 + i % transLen) % transLen], (0,0), skateSeq[(j * 48 + i % transLen) % transLen])
            #img = Image.alpha_composite(img, skateSeq[(j * 48 + i % 268) % 268])
    img = img.convert('RGB')
    img.save('imageseq/%05d.jpg' % i)
