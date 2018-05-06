# day 055

No longer daily sketches anymore, but here's a new one, playing around with `dlib`'s correlation tracker to catch up to a position later in the video.

In order to track multiple places at the same time, I started a new project that uses `pygame` with `dlib` to track the correlation [here](https://github.com/burningion/correlation-tracking-playground).

*EDIT* There is now a [blog post](https://www.makeartwithpython.com/blog/instagram-pin-effect-in-python/) at my site describing how this works.

![055](https://github.com/burningion/daily-sketches/raw/master/055/images/00352.png)

## sketch video generated with following commands

First, dump all the source frames as images. Then, trace the person at the end frame you want, save it as a transparent png. Use that png along with a correlation box you saved from the correlation playground.

```bash
$ python3 tracker.py
```

finally, make a video for export:

```bash
$ ffmpeg -r 60 -i %05d.jpg day56.mp4
```
