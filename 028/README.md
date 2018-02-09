# day 028

sketch inspired by the [optical flow example](https://docs.opencv.org/3.3.1/d7/d8b/tutorial_py_lucas_kanade.html) from opencv's docs. mixing the optical flow of a pre-recorded video with a stream from the webcam.

![028](https://github.com/burningion/daily-sketches/raw/master/028/images/00419.jpg)

## sketch video generated with following commands

```bash
$ python3 opt_flow.py
$ cd imagesq
$ ffmpeg  -i %05d.jpg day29.mp4
```

