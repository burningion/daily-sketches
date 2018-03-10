# day 031

animating a video with hilbert curves.

hilbert curve code shamelessly stolen from [stackoverflow answer by Falko](https://codegolf.stackexchange.com/questions/36374/redraw-an-image-with-just-one-closed-curve).

video is from old footage of black bear bar, an indoor mini ramp in a bar in brooklyn that no longer exists :(

![031](https://github.com/burningion/daily-sketches/raw/master/031/images/00022.png)

## sketch video generated with following commands

```bash
$ python3 hilbert.py
$ cd imageseq
$ ffmpeg -r 24 -i %05d.jpg -i soundfromoriginal.mp3 day32.mp4
```
