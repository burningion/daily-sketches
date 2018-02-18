# day 038

sketch using matterport's [Mask_RCNN](https://github.com/matterport/Mask_RCNN) project. you'll need to have it installed and run this project in that directory.

this sketch takes a mask of the skateboards and people in the video, and enlarges and pastes them over the original image. 

today's sketch was done on a vertical video, which was rotated 90 degrees using Adrian Rosebrock's image [rotation function](https://www.pyimagesearch.com/2017/01/02/rotate-images-correctly-with-opencv-and-python/), and then rotated back. 

i think it confused this implementation of mask rcnn a bit?

![038](https://github.com/burningion/daily-sketches/raw/master/038/images/00182.jpg)

## sketch video generated with folowing commands

```bash
$ python3 ben36.py 
$ ffmpeg -r 30 -i %05d.jpg -i audio.mp3 -strict -2 day37.mp4
```
