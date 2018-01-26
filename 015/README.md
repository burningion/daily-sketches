# day 015

mixing extracted birds from the [nvidia deep learning camera](https://www.makeartwithpython.com/blog/rich-mans-deep-learning-camera/) with mask_rcnn and midi input

![015](https://github.com/burningion/daily-sketches/raw/master/015/images/00852.jpg)


## sketch video generated from following commands

first, import image sequence and extract bird with [mask_rcnn](https://github.com/matterport/Mask_RCNN). I ran through how to do this on my day [012](https://github.com/burningion/daily-sketches/tree/master/012) and [013](https://github.com/burningion/daily-sketches/tree/master/013) sketches. today I just switched the detection to birds.

this sketch assumes there are 3 bird directories, and you can replace them with whatever.

```bash
$ python3 sketch-environment.py circleBird.py 1 -r 600
$ cd imageseq/
$ ffmpeg -r 24 -f image2 -i %*.jpg day16.mp4
```
