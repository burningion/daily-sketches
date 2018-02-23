import glob
import os

totalFiles = len(glob.glob('imageseqin/*.png'))

f1 = open('flow-first.txt', 'w+')
f2 = open('flow-second.txt', 'w+')

floOut = open('flow-out.txt', 'w+')

for i in range(2,totalFiles - 1):
    f1.write('imageseqin/%05d.png\n' % (i - 1))
    f2.write('imageseqin/%05d.png\n' % i)
    floOut.write('flowseq/%05d.flo\n' % (i - 1))

f1.close()
f2.close()
floOut.close()
