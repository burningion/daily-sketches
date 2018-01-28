# day 016

creating video introduction to my next blog post, describing how to use mask rcnn.

![016](https://github.com/burningion/daily-sketches/raw/master/016/images/00189.jpg)


## sketch video generated from following commands

You'll see the full walkthough in the blog post tomorrow, but in the meantime, I run the `gif_extract.py` file on my video input, and do the same with `gif_extract_og.py`, creating both a transparent png set, and a black background set of images to turn into videos.

I then use the black background images as is, and use the transparent pngs as input to the included Pygame sketch. Later, they're all put back together.

```bash
$ python3 sketch-environment.py straightLine 1 -r 600
$ cd imageseq/
$ ffmpeg -r 24 -f image2 -i %*.jpg day17.mp4
```
