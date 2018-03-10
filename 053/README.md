# day 053

sketch using matterport's [Mask_RCNN](https://github.com/matterport/Mask_RCNN) project. you'll need to have it installed and run this project in that directory.

![053](https://github.com/burningion/daily-sketches/raw/master/053/images/00075.jpg)

## sketch video generated with following commands

create image sequence frames in mask_rcnn directory:

```bash
$ python3 slideIn.py
```

this generates a sequence of output images. we then paste them using pillow with the `raw_image.py` file.

```bash
$ python3 raw_image.py
```

finally, make a video for export:

```bash
$ ffmpeg -r 60 -i %05d.jpg day54.mp4
```
