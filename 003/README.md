# day 003

sketch using matterport's [Mask_RCNN](https://github.com/matterport/Mask_RCNN) project. you'll need to have it installed and run this project in that directory.

this mixes two videos, detecting skateboards and people, continued from [day 002](https://github.com/burningion/daily-sketches/tree/master/002). 

today I've added a hard light filter and mixed footage of me skating and niagra falls video I shot a year or two back.

![003](https://github.com/burningion/daily-sketches/raw/master/003/images/00408.jpg)

## sketch video generated with folowing commands

```bash
$ mkdir {fallsseq,skateseq,fallsseqout}
$ ffmpeg -i videoskate.mp4 -qscale:v 2 -vsync 0 skateseq/%05d.png
$ ffmpeg -i fallsseq -qscale:v 2 -vsync 0 fallsseq/%05d.png
$ ffmpeg -i videoskate.mp4 -vn -acodec copy skate-audio.aac
$ python3 video_process.py 
$ cd fallsseqout
$ ffmpeg -r 30 -i %05d.jpg -i ../skate-audio.aac  -profile:v high -level 4.0 -strict -2 day4.mp4
```
