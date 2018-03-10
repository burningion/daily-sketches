# day 002

sketch using matterport's [Mask_RCNN](https://github.com/matterport/Mask_RCNN) project. you'll need to have it installed and run this project in that directory.

this mixes two videos, detecting skateboards and people

![002](https://github.com/burningion/daily-sketches/raw/master/002/images/00089.jpg)

space video from [creative commons](https://pixabay.com/en/videos/space-universe-cosmos-background-7980/)

## sketch video generated with folowing commands

```bash
$ mkdir {imageseqin,imageseqspace}
$ ffmpeg -i leofeeble.mov -qscale:v 2 -vsync 0 imageseqin/%05d.png
$ ffmpeg -i space.mp4 -qscale:v 2 -vsync 0 imageseqspace/%05d.png
$ ffmpeg -i leofeeble.mov -vn -acodec copy feeble-audio.aac
$ python3 video_process.py 
$ cd imageseqout
$ ffmpeg -r 30 -i %05d.jpg -i ../feeble-audio.aac  -profile:v high -level 4.0 -strict -2 day3.mp4
```
