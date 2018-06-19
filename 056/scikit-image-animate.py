import skimage
import skimage.draw, skimage.io
import numpy as np

import math

for z in range(0, 360):
    out = np.zeros((1024, 1024, 3), dtype=np.uint8)
    for x in range(60, 943, 20):
        for y in range(60, 943, 20):
            rr, cc, val = skimage.draw.line_aa(x,
                                       y,
                                       min(x + int(20 * math.sin(math.radians(z))), 1023),
                                       min(y + int(20 * math.cos(math.radians(z))), 1023))
            out[rr, cc] = np.swapaxes((val * 255, val * 255, val * 255), 0, 1)
    skimage.io.imsave("out/%05d.png" % z, out)
