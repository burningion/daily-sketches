from PIL import Image
import glob

numFiles = len(list(glob.glob('imageseqin/*.png')))

imageWidth, imageHeight = 1280, 720

counter = 1

maskLen = 240

for i in range(numFiles):
    img1 = Image.open('imageseqin/%05d.png' % (i + 1)).convert('RGBA')
    if counter < 69 or counter > 151:
        mask = Image.new('L', (imageWidth, imageHeight), color=255)
    else:
        mask = Image.open('fromprocessing/f%03d.png' % ((counter - 68) % 120)).convert('L')
    out = Image.new('RGBA', (imageWidth, imageHeight), color=(0,0,0,255))

    out.paste(img1, (0,0), mask=mask)
    out = out.convert('RGB')
    out.save("imageseq/%05d.jpg" % (i + 1))
    counter += 1
