# day 012

extracting dancing humans in video with mask-rcnn

![012](https://github.com/burningion/daily-sketches/raw/master/012/images/00718.jpg)

## sketch video generated from following commands

first, import image sequence and extract humans using [mask_rcnn](https://github.com/matterport/Mask_RCNN). run the following commands in that directory:

```bash
$ mkdir kirk_dance/
$ cd kirk_dance
$ ffmpeg -i ORIGINAL_VIDEO.MP4 -f image2 %05d.jpg
$ cd ..
$ python3 video_extract.py 
```

I quit the `video_extract.py` program once I got to the 300th frame of my video. That's all I wanted for my loop.

From there, I copied the images created (`human0/`) into my sketch directory, and ran the `pygame` program.

```bash
$ python3 sketch-environment.py squareDance.py 1 -r 900
$ cd imageseq/
$ ffmpeg -r 60 -i %05d.jpg -profile:v high -level 4.0 -strict -2 day12.mp4
```
