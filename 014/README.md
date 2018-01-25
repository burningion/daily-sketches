# day 014

mixing extracting dancing and skating humans in video with mask-rcnn with a face detected background

![014](https://github.com/burningion/daily-sketches/raw/master/014/images/00426.jpg)

together it might be a bit too much? but I'm getting into the idea of using yourself as input, and I'm starting to put the tools together to do that in a way that makes more sense.

## sketch video generated from following commands

first, import image sequence and extract humans using [mask_rcnn](https://github.com/matterport/Mask_RCNN). I ran through how to do this on my day [012](https://github.com/burningion/daily-sketches/tree/master/012) and [013](https://github.com/burningion/daily-sketches/tree/master/013) sketches.

then, I hooked up a webcam and ran the dlib model to detect faces. that was described in day [010](https://github.com/burningion/daily-sketches/tree/master/010).

the sketch assumes that those directories exist, and that you've checked out the entire `daily-sketches` repo.
```bash
$ python3 sketch-environment.py circleSkate.py 1 -r 600
$ cd imageseq/
$ ffmpeg -r 30 -f image2 -i %*.jpg day15.mp4
```
