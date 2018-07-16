# day 057

faking invisibility cloak with offset pixels and mask rcnn

![057](https://github.com/burningion/daily-sketches/raw/master/057/image/00960.jpg)

## sketch video generated with following commands

```bash
$ ffmpeg -i ~/Downloads/minijuly.MOV -q:v 1 -f image2 minijulyin/%05d.png
$ ffmpeg -i ~/Downloads/minijuly.MOV miniout.mp3
$ python3 minijuly.py
$ ffmpeg -r 60 -i minijulyout/%05d.jpg -i miniout.mp3 -pix_fmt yuv420p -strict -2 minijulyout.mp4
```

