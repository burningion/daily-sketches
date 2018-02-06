# day 025

(today was mostly a failure. was attempting to do particles, but went too long. so instead, today is mostly the same as 023.)

relied heavily on Michael Sobprepera's [blog post](http://michaelsobrepera.com/guides/openposeaws.html) and Docker containers for OpenPose. 


![025](https://github.com/burningion/daily-sketches/raw/master/025/images/00148.jpg)


## sketch video generated from following commands

first, we extract the openpose locations from our input image sequence. then, we run them on openpose

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
$ ffmpeg -r 60 -i %05d.jpg day26.mp4
```
