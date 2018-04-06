import dlib
from skimage import io
from PIL import Image
import numpy as np

video_dir = './video_in'


start_frame = 217
end_frame = 251

selfie = Image.open('kirk.png')

tracker = dlib.correlation_tracker()

win = dlib.image_window()
for i in range(start_frame, end_frame):
    img = io.imread('%s/%05d.png' % (video_dir, i))
    print('In frame %d' % i)
    if i == start_frame:
        tracker.start_track(img, dlib.rectangle(1711, 638, 1811, 700))
    else:
        tracker.update(img)

    win.clear_overlay()

    # the tracker gives us a drectangle object
    # http://dlib.net/python/index.html#dlib.drectangle
    position = tracker.get_position()
    top_left = [int(position.left()), int(position.top())]

    # create a new transparent image to paste into
    new = Image.new('RGBA', (1920, 1080))
    new.paste(Image.fromarray(img))
    # paste my outline wherever the tracked box is
    new.paste(selfie, (top_left[0] - 250, top_left[1] - selfie.height + 80), selfie)
    # print the box just in case
    print(tracker.get_position())
    new = new.convert('RGB')
    # save out the image
    new.save('image_out/%05d.png' % i)
    img = np.array(new)
    win.set_image(img)
    win.add_overlay(tracker.get_position())
    # uncomment below to step through each frame manually
    #dlib.hit_enter_to_continue()
