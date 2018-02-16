# day 035

sketch using matterport's [Mask_RCNN](https://github.com/matterport/Mask_RCNN) project. you'll need to have it installed and run this project in that directory.

this sketch takes a mask of the skateboards and people in the video, and enlarges and pastes them over the original image.

![035](https://github.com/burningion/daily-sketches/raw/master/035/images/01046.jpg)

## sketch video generated with folowing commands

```bash
$ python3 video_resize.py 
$ ffmpeg -r 60 -i bowlseq/%05d.jpg -i skate-audio.aac  -profile:v high -level 4.0 -strict -2 day36.mp4
```
