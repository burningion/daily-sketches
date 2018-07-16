# day 057

faking invisibility cloak with offset pixels and mask rcnn

![057](https://github.com/burningion/daily-sketches/raw/master/057/image/00089.jpg)

## sketch video generated with following commands

```bash
$ ffmpeg -i ~/Downloads/crail.MOV -q:v 1 -f image2 crailin/%05d.png
$ ffmpeg -i ~/Downloads/crail.MOV crail.mp3
$ python3 crailinvisible.py
$ ffmpeg -r 60 -i crailout/%05d.jpg -i crailly.mp3 -pix_fmt yuv420p -strict -2 crailly.mp4
```

