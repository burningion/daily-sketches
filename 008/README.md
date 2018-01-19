# day 008

zooming squares controllable with midi input 

![008](https://github.com/burningion/daily-sketches/raw/master/008/images/00174.jpg)

## sketch video generated from following commands


```bash
$ python3 etc-test.py squares.py 1 -r 900
$ cd imageseq
$ ffmpeg -r 60 -i %05d.jpg -profile:v high -level 4.0 -strict -2 day9.mp4

```
