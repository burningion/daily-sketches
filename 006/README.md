# day 006

sketch today added HD support to the bird detecting deep learning camera.

![006](https://github.com/burningion/daily-sketches/raw/master/006/images/00218.jpg)

## sketch video generated from nvidia tx1

on the tx1:

```bash
$ python3 richierich.py
```

after some birds were detected for the day:

```bash
$ scp -r nvidia@192.168.1.8:rich-mans-deep-learning-camera/bird* .
$ mkdir outvideo
$ python3 joinImages.py
$ cd outvideo
$ ffmpeg -r 24 -i %05d.jpg -profile:v high -level 4.0 -strict -2 day7.mp4

```
