# day 056

easing back into sketches with anti aliased lines courtesy of scikit-image.

![056](https://github.com/burningion/daily-sketches/raw/master/056/image/00000.jpg)

## sketch video generated with following commands

```bash
$ mkdir out
$ python3 scikit-image-animate.py
$ cd out
$ ffmpeg -r 60 -i %05d.png  -profile:v high -level 4.0 -r 60 -strict -2 -pix_fmt yuv420p backin.mp4
```

