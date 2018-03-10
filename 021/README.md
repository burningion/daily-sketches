# day 021

relied heavily on Michael Sobprepera's [blog post](http://michaelsobrepera.com/guides/openposeaws.html) and Docker containers for OpenPose. 


![021](https://github.com/burningion/daily-sketches/raw/master/021/images/00233.jpg)


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
$ python3 sketch-environment.py justLines -r 900
$ cd imageseq/
$ ffmpeg -r 60 -i %05d.jpg -i ../audio.mp3 -strict -2 day22.mp4
```
