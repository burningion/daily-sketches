# day 041

sketch using matterport's [Mask_RCNN](https://github.com/matterport/Mask_RCNN) project. you'll need to have it installed and run this project in that directory.

this sketch takes a mask of the skateboards and people in the video, and builds a list of transparent pngs of just them.

it then takes n % 60 of the frames before and after the current frame and pastes them over the image

![041](https://github.com/burningion/daily-sketches/raw/master/041/images/00106.jpg)

## sketch video generated with folowing commands

```bash
$ python3 50slo.py
$ ffmpeg -r 24 -i %05d.jpg day42.mp4
```
