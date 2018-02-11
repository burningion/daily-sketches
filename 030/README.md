# day 030

continuing from sine wave googley eyes. creating south park type character in real time from face info.

sketch uses dlib's frontal face detector again.

![030](https://github.com/burningion/daily-sketches/raw/master/030/images/00330.jpg)

## sketch video generated with following commands

```bash
$ python3 terrance.py -predictor ../029/predictor.dat
$ cd imageseq
$ ffmpeg  -i %05d.jpg day31.mp4
```

