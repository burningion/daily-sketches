import cv2
import numpy as np

from PIL import Image

cap = cv2.VideoCapture("snek.mp4")
ret, frame1 = cap.read()
prvs = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
hsv = np.zeros_like(frame1)
hsv[...,1] = 255
counter = 1
while(1):
    ret, frame2 = cap.read()
    next = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
    flow = cv2.calcOpticalFlowFarneback(prvs,next, None, 0.5, 3, 15, 3, 5, 1.2, 0)
    mag, ang = cv2.cartToPolar(flow[...,0], flow[...,1])
    hsv[...,0] = ang*180/np.pi/2
    hsv[...,2] = cv2.normalize(mag,None,0,255,cv2.NORM_MINMAX)
    rgb = cv2.cvtColor(hsv,cv2.COLOR_HSV2RGB)
    im = Image.fromarray(rgb)
    im = im.resize((1920 // 2, 1080 // 2))

    imout = Image.new('RGBA', (1920, 1080))
    imout.paste(im, (0,0))
    imout.paste(im.transpose(Image.FLIP_LEFT_RIGHT), (1920 // 2, 0))
    imout.paste(im.transpose(Image.FLIP_TOP_BOTTOM), (0, 1080 // 2))
    imout.paste(im.transpose(Image.FLIP_TOP_BOTTOM).transpose(Image.FLIP_LEFT_RIGHT), (1920 // 2, 1080 // 2))
    imout.convert('RGB').save('flowy/%05d.jpg' % counter)
    #cv2.imwrite('flowy/%05d.jpg' % counter, bgr)
    if counter == 600:
        exit()
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    elif k == ord('q'):
        break
    prvs = next

    counter += 1
cap.release()
cv2.destroyAllWindows()
