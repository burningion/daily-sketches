from PIL import Image
import numpy as np
import glob

skateSeq = []
counter = 1

numMontage = len(glob.glob('montageTrans/*.png'))

print(numMontage)
for i in range(1, numMontage):
    imagey = Image.open('montageTrans/%05d.png' % i)
    imgarr = np.array(imagey, dtype='float64')
    imgarr[:,:,3] = imgarr[:,:,3] * .7
    skateSeq.append(Image.fromarray(imgarr.astype('uint8')))
    imagey.close()

numFiles = len(glob.glob('videoIn/*.png'))
print(numFiles)

numMontage -= 1

for i in range(1, numFiles * 2):
    img = Image.open('videoIn/%05d.png' % max((((i % numFiles - 1) + 1)), 1)).convert('RGBA')
    for j in range(5):
        print('doing transparent frame %i' % ((j * 48 + i % numMontage) % numMontage))
        img.paste(skateSeq[(j * 48 + i % numMontage) % numMontage], (0,0), skateSeq[(j * 48 + i % numMontage) % numMontage])
        #img = Image.alpha_composite(img, skateSeq[(j * 48 + i % 268) % 268])
    img = img.convert('RGB')
    img.save('imageseq/%05d.jpg' % i)
