# day 039

sketch using matterport's [Mask_RCNN](https://github.com/matterport/Mask_RCNN) project. you'll need to have it installed and run this project in that directory.

this sketch takes a mask of the skateboards and people in the video, and enlarges and pastes them over the original image in a sine wave pattern.


![039](https://github.com/burningion/daily-sketches/raw/master/039/images/00163.jpg)

## sketch video generated with folowing commands

```bash
$ python3 leodrop.py 
$ ffmpeg -r 30 -i %05d.jpg day40.mp4
```
