from PIL import Image, ImageDraw
import glob
import time

numFiles = len(list(glob.glob('imageseqfirst/*.jpg')))

for i in range(numFiles):
    img1 = Image.open('imageseqfirst/%05d.jpg' % (i + 1)).convert('RGBA')
    out = Image.new('RGBA', (1920, 1080), color=(0,0,0,255))
    mask = Image.new('L', (1920, 1080), color=0)
    draw = ImageDraw.Draw(mask)
    draw2 = ImageDraw.Draw(out)

    draw.polygon([(1920 // 2 - 1920 // 4, 0), (1920 // 2 + 1920 // 4, 0), (1920 // 2, 1080)], fill=255)

    out.paste(img1, (0,0), mask=mask)
    out = out.convert('RGB')
    out.save("imageseq/%05d.jpg" % (i + 1))

numFiles2 = len(list(glob.glob('imageseqsecond/*.jpg')))

for i in range(numFiles2):
    img1 = Image.open('imageseqsecond/%05d.jpg' % (i + 1)).convert('RGBA')
    out = Image.new('RGBA', (1920, 1080), color=(0,0,0,255))
    mask = Image.new('L', (1920, 1080), color=0)
    draw = ImageDraw.Draw(mask)
    draw2 = ImageDraw.Draw(out)

    draw.polygon([(1920 // 2 - 1920 // 4, 0), (1920 // 2 + 1920 // 4, 0), (1920 // 2, 1080)], fill=255)

    out.paste(img1, (0,0), mask=mask)
    out = out.convert('RGB')
    out.save("imageseq/%05d.jpg" % (i + numFiles + 1))
