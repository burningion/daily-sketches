from PIL import Image
import numpy as np

skateSeq = []
counter = 1

for i in range(1, 269):
    imagey = Image.open('ben50Trans/%05d.png' % (i))
    imgarr = np.array(imagey, dtype='float64')
    imgarr[:,:,3] = imgarr[:,:,3] * .6
    skateSeq.append(Image.fromarray(imgarr.astype('uint8')))
    imagey.close()

main = Image.open('main.png').convert('RGBA')

#main.show()

for i in range(1, 269):
    img = main.copy()
    for j in range(50):
        print('doing transparent frame %i' % ((j * 48 + i % 268) % 268))
        img.paste(skateSeq[(j * 48 + i % 268) % 268], (0,0), skateSeq[(j * 48 + i % 268) % 268])
        #img = Image.alpha_composite(img, skateSeq[(j * 48 + i % 268) % 268])
    img = img.convert('RGB')
    img.save('imageseq/%05d.jpg' % i)
