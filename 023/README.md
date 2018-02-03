# day 023

relied heavily on Michael Sobprepera's [blog post](http://michaelsobrepera.com/guides/openposeaws.html) and Docker containers for OpenPose. 


![023](https://github.com/burningion/daily-sketches/raw/master/023/images/00350.jpg)


## sketch video generated from following commands

first, we extract the openpose locations from our input image sequence. 

in today's sketch, i used 30 seconds from [this](https://archive.org/details/Square_Dance_Live_-_Episode_2) video. i copied it into my sketch directory and took 30 seconds out of it with `ffmpeg`.

```bash
$ ffmpeg -ss 1330 -t 30 -i ~/Downloads/Square_Dance_Live_-_Episode_2.mp4 -strict -2 squareDance.mp4
```

with this shorter video, i could then run inference on it, and build a set of openpose json files:

```bash
$ nvidia-docker run -v ~/Development/daily-sketches/023:/data -it mjsobrep/openpose:latest ./build/examples/openpose/openpose.bin --video /data/squareDance.mp4 --write_images /data/labeledSq --write_keypoint_json /data/walkdataSq/ --no_display
```

![openpose points](https://github.com/burningion/daily-sketches/raw/master/017/images/keypoints_pose.png)

each of the elements in our output json comes in sets of 3. an x, y, and a confidence. as you can see above, the right elbow and right hand are points 3 and 4.

we use those points to draw a circle of the size * confidence.

finally, the output video must be built at the same framerate as the input video to make sense (`-r 30`) for 30 FPS.

```bash
$ python3 sketch-environment.py justCircles -r 900
$ cd imageseq/
$ ffmpeg -r 30 -i %05d.jpg day23.mp4
```
