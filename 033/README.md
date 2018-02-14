# day 033

sketch uses python imaging library to mask off shape

![033](https://github.com/burningion/daily-sketches/raw/master/033/images/00418.jpg)

## sketch video generated with following commands

extract video to image sequence / mp3 with ffmpeg and then:

```bash
$ mkdir imageseq
$ python3 sketchy.py
$ cd imagesq
$ ffmpeg  -i %05d.jpg day29.mp4
```

