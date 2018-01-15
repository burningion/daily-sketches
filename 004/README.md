# day 004

sketch using openpose. I used the docker version of the code and generated a pose series of data.

```bash
#!/bin/sh

xhost +local:root

nvidia-docker run \
  -it \
  --env="DISPLAY" \
  --env="QT_X11_NO_MITSHM=1" \
  --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
  --device /dev/video0:/dev/video0 \
  -v input:/opt/caffe/build/examples/openpose/input \
  -v output:/opt/caffe/build/examples/openpose/output \
  cmupcl/openpose:gpu ./build/examples/openpose/rtpose.bin --video /opt/caffe/build/examples/openpose/input/colvin.mp4 -write_pose_json /opt/caffe/build/examples/openpose/output

xhost -local:root

# TODO: instruct users run get_models locally on host
# then mount them into the container using volumes
# --volume="/${PWD}/../models:/root/openpose/models" \

```

![004](https://github.com/burningion/daily-sketches/raw/master/004/images/00408.jpg)

## sketch video generated with folowing commands

```bash
$ mkdir {imageseqin,output}
$ ffmpeg -i colvin.mp4 -qscale:v 2 -vsync 0 skateseq/%05d.png
$ ffmpeg -i colvin.mp4 -vn -acodec copy skate-audio.aac
$ python3 drawIt.py 
$ cd output
$ ffmpeg -r 30 -i %05d.jpg -i ../skate-audio.aac  -profile:v high -level 4.0 -strict -2 day5.mp4
```
