# day 049

continuing from sketch 030, playing more with faces.

sketch uses dlib's frontal face detector again.

![049](https://github.com/burningion/daily-sketches/raw/master/049/images/00112.jpg)

## sketch video generated with following commands

```bash
$ python3 headSlit.py -predictor ../029/predictor.dat
$ cd imageseq
$ ffmpeg  -r 24 -i %05d.jpg day50.mp4
```

