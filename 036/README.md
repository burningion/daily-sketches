# day 036

sketch using matterport's [Mask_RCNN](https://github.com/matterport/Mask_RCNN) project. you'll need to have it installed and run this project in that directory.

this sketch takes a mask of the skateboards and people in the video, and enlarges and pastes them over the original image. done in collaboration with ben.g

![036](https://github.com/burningion/daily-sketches/raw/master/036/images/00136.jpg)

## sketch video generated with folowing commands

```bash
$ python3 ben36.py 
$ ffmpeg -r 30 -i %05d.jpg -i audio.mp3 -strict -2 day37.mp4
```
