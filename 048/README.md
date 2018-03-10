# day 048

sketch using matterport's [Mask_RCNN](https://github.com/matterport/Mask_RCNN) project. you'll need to have it installed and run this project in that directory.

![048](https://github.com/burningion/daily-sketches/raw/master/048/images/00120.jpg)

## sketch video generated with following commands

first, create continuous image sequence from set of videos with ffmpeg `fileList.txt`:

```bash
$ ffmpeg -f concat -i fileList.txt -qscale:v 1 montageIn/%05d.png
```

then, run mask r-cnn to extract humanssss:

```bash
$ python3 selfieMontage.py
```

this generates a sequence of output images. we then paste them using pillow with the `raw_image.py` file.

```bash
$ python3 raw_image.py
```

finally, make a video for export:

```bash
$ ffmpeg -r 30 -i %05d.jpg day48.mp4
```
