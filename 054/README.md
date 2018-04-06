# day 054

Not quite daily sketches anymore, but here's a new one, playing around with `dlib`'s correlation tracker to catch up to a position later in the video.

![054](https://github.com/burningion/daily-sketches/raw/master/054/images/00224.png)

## sketch video generated with following commands

Uncomment the `dlib.hit_enter_to_continue()` line to see what each frame looks like.

```bash
$ python3 tracker.py
```

finally, make a video for export:

```bash
$ ffmpeg -r 60 -i %05d.jpg day54.mp4
```
