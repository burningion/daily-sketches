# day 019

replacing openpose lines with mario using bressenham lines

relied heavily on Michael Sobprepera's [blog post](http://michaelsobrepera.com/guides/openposeaws.html) and Docker containers for OpenPose. 

build from [yesterday's work](https://github.com/burningion/daily-sketches/tree/master/018) 

![019](https://github.com/burningion/daily-sketches/raw/master/019/images/00406.jpg)


## sketch video generated from following commands

first, we extract the openpose locations from our input image sequence. i've moved my input images to `~/Development/openpose-docker/data/gifready`, as the original pngs.

```bash
$ nvidia-docker run -v ~/Development/openpose-docker:/data -it mjsobrep/openpose:latest ./build/examples/openpose/openpose.bin --image_dir /data/gifready/  --write_keypoint_json /data/data/ --no_display
```

Once this Docker image is built and run, we get out a set of JSON files, one per image frame. From this, we can estimate the positions of each body part according to the following model:

![openpose points](https://github.com/burningion/daily-sketches/raw/master/017/images/keypoints_pose.png)

each of the elements in our output json comes in sets of 3. an x, y, and a confidence. as you can see above, the right elbow and right hand are points 3 and 4.

we then use those points to draw bressenham lines.

```bash
$ python3 sketch-environment.py justLines -r 900
$ cd imageseq/
$ ffmpeg -r 60 -f image2 -i %*.jpg day20.mp4
```
