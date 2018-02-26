# day 045

sketch using matterport's [Mask_RCNN](https://github.com/matterport/Mask_RCNN) project. you'll need to have it installed and run this project in that directory.

mixes detected people and skateboards with optical flow from [flownet2](https://github.com/lmb-freiburg/flownet2-docker). 

masks the people off, and then pastes copies of them on a blank image.

![045](https://github.com/burningion/daily-sketches/raw/master/045/images/00575.jpg)

## sketch video generated with folowing commands

create the image sequences with ffmpeg and [day 42's optical flow instructions](https://github.com/burningion/daily-sketches/tree/master/042)

then, run the included python file in the Mask R-CNN's directory like in the earlier sketches.

finally, combine the images back together with ffmpeg as usual.

```bash
$ ffmpeg -r 60 -start_number 253 -i finalmini/%05d.jpg day46.mp4
```
