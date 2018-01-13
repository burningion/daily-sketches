# day 002

sketch using matterport's [Mask_RCNN](https://github.com/matterport/Mask_RCNN) project. you'll need to have it installed and run this project in that directory.

space video from [creative commons](https://pixabay.com/en/videos/space-universe-cosmos-background-7980/)

pretty sure there's a bug in my image copying logic, there should be multiple things masked off. maybe tomorrow.

## sketch video generated with folowing commands

```bash
$ mkdir {imageseqin,imageseqspace}
$ ffmpeg -i leofeeble.mov -qscale:v 2 -vsync 0 imageseqin/%05d.png
$ ffmpeg -i space.mp4 -qscale:v 2 -vsync 0 imageseqspace/%05d.png
$ ffmpeg -i leofeeble.mov -vn -acodec copy feeble-audio.aac
$ python3 video_process.py 
$ cd imageseqout
$ ffmpeg -i %05d.jpg
```
