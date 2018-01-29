# day 018

second day of trying to get a video effect like Cyriak, using Mask R-CNN and OpenPose together.

relied heavily on Michael Sobprepera's [blog post](http://michaelsobrepera.com/guides/openposeaws.html) and Docker containers for OpenPose. 

build from [yesterday's work](https://github.com/burningion/daily-sketches/tree/master/017) 

![018](https://github.com/burningion/daily-sketches/raw/master/018/images/00326.jpg)


## sketch video generated from following commands

first, we extract the openpose locations from our input image sequence. i've moved my input images to `~/Development/openpose-docker/data/gifready`, as the original pngs.

```bash
$ nvidia-docker run -v ~/Development/openpose-docker:/data -it mjsobrep/openpose:latest ./build/examples/openpose/openpose.bin --image_dir /data/gifready/  --write_keypoint_json /data/data/ --no_display
```

Once this Docker image is built and run, we get out a set of JSON files, one per image frame. From this, we can estimate the positions of each body part according to the following model:

![openpose points](https://github.com/burningion/daily-sketches/raw/master/017/images/keypoints_pose.png)

each of the elements in our output json comes in sets of 3. an x, y, and a confidence. as you can see above, the right elbow and right hand are points 3 and 4.

we use those points to paste a rotated verson along the right arm. the one that's moving. super glitchy but you have to start somewhere.

```bash
$ python3 sketch-environment.py withOpenPose -r 600
$ cd imageseq/
$ ffmpeg -r 60 -f image2 -i %*.jpg day19.mp4
```
