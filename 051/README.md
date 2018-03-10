# day 051

sketch using matterport's [Mask_RCNN](https://github.com/matterport/Mask_RCNN) project. you'll need to have it installed and run this project in that directory.

![051](https://github.com/burningion/daily-sketches/raw/master/051/images/00132.jpg)

## sketch video generated with following commands

create image sequence frames in mask_rcnn directory:

```bash
$ python3 ben50.py
```

this generates a sequence of output images. we then paste them using pillow with the `raw_image.py` file.

```bash
$ python3 raw_image.py
```

finally, make a video for export:

```bash
$ ffmpeg -r 24 -i %05d.jpg day52.mp4
```
