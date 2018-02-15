# day 034

sketch uses python imaging library to mask off shape and animate. 

input video is of chris haslam from his [2 up](https://www.youtube.com/watch?v=Sn8K2Ae45pA) part.

![034](https://github.com/burningion/daily-sketches/raw/master/034/images/00151.jpg)

## sketch video generated with following commands

extract video to image sequence / mp3 with ffmpeg and then:

```bash
$ mkdir imageseq
$ python3 sketchy.py
$ cd imagesq
$ ffmpeg -i %05d.jpg day29.mp4
```

