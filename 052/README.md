# day 052

today is particles and openpose.

relied heavily on Michael Sobprepera's [blog post](http://michaelsobrepera.com/guides/openposeaws.html) and Docker containers for OpenPose. 


![052](https://github.com/burningion/daily-sketches/raw/master/052/images/00053.jpg)


## sketch video generated from following commands

first, we extract the openpose locations from our input image sequence. then, we run them on openpose

```bash
$ nvidia-docker run -v ~/Development/daily-sketches/052:/data -it mjsobrep/openpose:latest ./build/examples/openpose/openpose.bin --video /data/quickflip.mp4 --write_images /data/labeledSq --write_keypoint_json /data/walkdataSq/ --no_display
```

![openpose points](https://github.com/burningion/daily-sketches/raw/master/017/images/keypoints_pose.png)

each of the elements in our output json comes in sets of 3. an x, y, and a confidence. as you can see above, the right elbow and right hand are points 3 and 4.

we use those points to draw a circle of the size * confidence.

finally, the output video must be built at the same framerate as the input video to make sense (`-r 60`) for 60 FPS.

```bash
$ python3 sketch-environment.py justParticles -r 900
$ cd imageseq/
$ ffmpeg -r 24 -i %05d.jpg day53.mp4
```
