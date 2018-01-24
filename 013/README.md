# day 013

mixing extracting dancing and skating humans in video with mask-rcnn

![013](https://github.com/burningion/daily-sketches/raw/master/013/images/00348.jpg)

## sketch video generated from following commands

first, import image sequence and extract humans using [mask_rcnn](https://github.com/matterport/Mask_RCNN). run the following commands in that directory:

```bash
$ mkdir skateollie
$ cd skateollie
$ ffmpeg -i ORIGINAL_VIDEO.MP4 -f image2 %05d.jpg
$ cd ..
$ python3 video_extract.py 
```

I quit the `video_extract.py` program once I got to the 300th frame of my video. That's all I wanted for my loop.

For today's skate extraction, I also needed to manually trim the humans extracted. Sometimes I jumped from the first human to second in some of the frames. I just copied all the frames of me into one directory, and used that.

From there, I copied the images created (`human1/`) into my sketch directory (along with yesterday's `human0/`), and ran the `pygame` program.

```bash
$ python3 sketch-environment.py circleSkate.py 1 -r 900
$ cd imageseq/
$ ffmpeg -r 30 -i %05d.jpg -profile:v high -level 4.0 -strict -2 day13.mp4
```
