from PIL import Image

skateSeq = []
counter = 1

for i in range(1, 1840):
    imagey = Image.open('miniTrans/%05d.png' % (i))
    skateSeq.append(imagey.copy().convert('RGBA'))
    imagey.close()

main = Image.open('main.png').convert('RGBA')

main.show()

for i in range(1, 421):
    img = main.copy()
    for j in range(10):
        img.paste(skateSeq[j * 140 + i % 420], (0,0), skateSeq[j * 140 + i % 420])
    img = img.convert('RGB')
    img.save('imageseq/%05d.jpg' % i)
