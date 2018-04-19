import dlib
from skimage import io
from PIL import Image
import numpy as np

video_dir = './bowl_in'


start_frame = 99
end_frame = 145

selfie = Image.open('k0144.png')

tracker = dlib.correlation_tracker()

#win = dlib.image_window()
for i in range(start_frame, end_frame):
    img = io.imread('%s/%05d.png' % (video_dir, i))
    print('In frame %d' % i)
    if i == start_frame:
        tracker.start_track(img, dlib.rectangle(32, 264, 112,334))
    else:
        tracker.update(img)


    # the tracker gives us a drectangle object
    # http://dlib.net/python/index.html#dlib.drectangle
    position = tracker.get_position()
    top_left = [int(position.left()), int(position.top())]

    # create a new transparent image to paste into
    new = Image.new('RGBA', (1920, 1080))
    new.paste(Image.fromarray(img))
    # paste my outline wherever the tracked box is
    new.paste(selfie, (top_left[0] - 145, top_left[1] - selfie.height + 43), selfie)
    # print the box just in case
    print(tracker.get_position())
    new = new.convert('RGB')
    # save out the image
    new.save('image_out/%05d.png' % i)
    #img = np.array(new)
    #win.set_image(img)
    #win.add_overlay(tracker.get_position())
    # uncomment below to step through each frame manually
    #dlib.hit_enter_to_continue()

start_frame = 145
end_frame = 199

selfie = Image.open('k0198.png')

tracker = dlib.correlation_tracker()

for i in range(start_frame, end_frame):
    img = io.imread('%s/%05d.png' % (video_dir, i))
    print('In frame %d' % i)
    if i == start_frame:
        tracker.start_track(img, dlib.rectangle(138, 500, 248, 620))
    else:
        tracker.update(img)


    # the tracker gives us a drectangle object
    # http://dlib.net/python/index.html#dlib.drectangle
    position = tracker.get_position()
    top_left = [int(position.left()), int(position.top())]

    # create a new transparent image to paste into
    new = Image.new('RGBA', (1920, 1080))
    new.paste(Image.fromarray(img))
    # paste my outline wherever the tracked box is
    new.paste(selfie, (top_left[0] - 103, top_left[1] - selfie.height + 72), selfie)
    # print the box just in case
    print(tracker.get_position())
    new = new.convert('RGB')
    # save out the image
    new.save('image_out/%05d.png' % i)
    #img = np.array(new)
    #win.set_image(img)
    #win.add_overlay(tracker.get_position())
    # uncomment below to step through each frame manually
    #dlib.hit_enter_to_continue()

trackers = [{'start_frame': 293, 'end_frame': 360, 'start_rect': dlib.rectangle(1457, 177, 1551, 259),
             'off_x': -212, 'off_y': -244, 'image': Image.open('k0360.png'), 'tracker': dlib.correlation_tracker()},
            {'start_frame': 294, 'end_frame': 371, 'start_rect': dlib.rectangle(1360, 134, 1445, 231),
             'off_x': -52, 'off_y': -212, 'image': Image.open('k0371.png'), 'tracker': dlib.correlation_tracker()},
            {'start_frame': 294, 'end_frame': 389, 'start_rect': dlib.rectangle(1610, 222, 1723, 376),
             'off_x': -113, 'off_y': -341, 'image': Image.open('k0389.png'), 'tracker': dlib.correlation_tracker()},
            {'start_frame': 462, 'end_frame': 515, 'start_rect': dlib.rectangle(91, 101, 286, 234),
             'off_x': -63, 'off_y': -325, 'image': Image.open('k0515.png'), 'tracker': dlib.correlation_tracker()},
            {'start_frame': 558, 'end_frame': 734, 'start_rect': dlib.rectangle(1692, 94, 1910, 267),
             'off_x': 179, 'off_y': -124, 'image': Image.open('k0734.png'), 'tracker': dlib.correlation_tracker()}]


start_frame = 293
end_frame = 735

for i in range(start_frame, end_frame):
    img = io.imread('%s/%05d.png' % (video_dir, i))
    print('In frame %d' % i)
    new = Image.new('RGBA', (1920, 1080))
    # create a new transparent image to paste into
    new = Image.new('RGBA', (1920, 1080))
    new.paste(Image.fromarray(img))
    for tracker in trackers:
        if i == tracker['start_frame']:
            tracker['tracker'].start_track(img, tracker['start_rect'])
            # the tracker gives us a drectangle object
            # http://dlib.net/python/index.html#dlib.drectangle
            position = tracker['tracker'].get_position()
            top_left = [int(position.left()), int(position.top())]
            # paste my outline wherever the tracked box is
            new.paste(tracker['image'], (top_left[0] + tracker['off_x'], top_left[1] + tracker['off_y']),
                      tracker['image'])
            # print the box just in case
            print(tracker['tracker'].get_position())
        elif tracker['end_frame'] >= i and tracker['start_frame'] <= i:
            tracker['tracker'].update(img)

            # the tracker gives us a drectangle object
            # http://dlib.net/python/index.html#dlib.drectangle
            position = tracker['tracker'].get_position()
            top_left = [int(position.left()), int(position.top())]
            # paste my outline wherever the tracked box is
            new.paste(tracker['image'], (top_left[0] + tracker['off_x'], top_left[1] + tracker['off_y']),
                      tracker['image'])
            # print the box just in case
            print(tracker['tracker'].get_position())
    new = new.convert('RGB')
    # save out the image
    new.save('image_out/%05d.png' % i)
    #img = np.array(new)
    #win.set_image(img)
    #win.add_overlay(tracker.get_position())
    # uncomment below to step through each frame manually
    #dlib.hit_enter_to_continue()
