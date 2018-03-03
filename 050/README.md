# day 050

continuing from sketch 049, playing more with faces.

sketch uses dlib's frontal face detector again.

![050](https://github.com/burningion/daily-sketches/raw/master/050/images/00135.jpg)

## sketch video generated with following commands

```bash
$ python3 headSlit.py -predictor ../029/predictor.dat
$ cd imageseq
$ ffmpeg  -r 24 -i %05d.jpg day51.mp4
```

