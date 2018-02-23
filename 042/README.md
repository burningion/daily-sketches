# day 042

sketch using [flownet2 docker image](https://github.com/lmb-freiburg/flownet2-docker). you'll need to have it installed in order to get the `.flo` files used to be colorized. you can read their instructions on the repo.

the createText.py creates the filenames necessary to run the optical flow on a video sequence.

colorizes the `flo` files using modified version of [flow-code-python](https://github.com/Johswald/flow-code-python). basically wrapped the `computeColor.py` file to load all my `.flo` images and write them out as `jpgs`.

![042](https://github.com/burningion/daily-sketches/raw/master/042/images/00132.jpg)

## sketch video generated with folowing commands

```bash
$ python3 createText.py
$ ./run-network.sh -n FlowNet2-CSS flow-first.txt flow-second.txt flow-out.txt
$ python3 computeColor.py
$ ffmpeg -r 60 -i %05d.jpg day43.mp4
```
