# day 047

sketch using matterport's [Mask_RCNN](https://github.com/matterport/Mask_RCNN) project. you'll need to have it installed and run this project in that directory.

![047](https://github.com/burningion/daily-sketches/raw/master/047/images/00053.jpg)

## sketch video generated with following commands

create image sequence frames in mask_rcnn directory:

```bash
$ python3 ben50.py
```

this generates a sequence of output images. we then paste them using pillow with the `raw_image.py` file.

```bash
$ python3 raw_image.py
```

make sure you have enough frames for this, otherwise you'll run into errors. you'll need to calculate the total frames you have and stay under in your `img.paste` line.

finally, make a video for export:

```bash
$ ffmpeg -r 30 -i %05d.jpg day47.mp4
```
