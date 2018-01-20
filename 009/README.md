# day 009

zooming squares controlled with midi input, now with inner squares

![009](https://github.com/burningion/daily-sketches/raw/master/009/images/00571.jpg)

## sketch video generated from following commands


```bash
$ python3 etc-test.py squareConnection.py 1 -r 900
$ cd imageseq
$ ffmpeg -r 60 -i %05d.jpg -profile:v high -level 4.0 -strict -2 day10.mp4
```

knobs were turned using a [korg nanoKONTROL 2](http://amzn.to/2DyAGNC)
