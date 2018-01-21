# day 010

zooming squares controlled with midi input, now with inner squares and detected faces from a webcam

face detection uses dlib, opencv, pillow, and imutils libraries

![010](https://github.com/burningion/daily-sketches/raw/master/010/images/00736.jpg)

## sketch video generated from following commands


```bash
$ python3 sketch-environment.py squareFace 1 -r 900
$ cd imageseq
$ ffmpeg -r 24 -i %05d.jpg -profile:v high -level 4.0 -strict -2 day11.mp4
```

knobs were turned using a [korg nanoKONTROL 2](http://amzn.to/2DyAGNC)
