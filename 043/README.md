# day 043

sketch using [fast photo style](https://github.com/NVIDIA/FastPhotoStyle) from nvidia, along with the insanely great [waifu2x](https://github.com/nagadomi/waifu2x) project.

you'll need to download fast photo style first, build the docker image, and copy this folder inside of that repo's directory.

for waifu2x, you'll just need to download and install the docker file and then run the `batchWaifu2x.py`.

![043](https://github.com/burningion/daily-sketches/raw/master/043/images/00184.png)

## sketch video generated with folowing commands

create the image sequence 

```bash
$ mkdir imageseqin
$ ffmpeg -i back180.mov -qscale:v 1 imageseqin/%05d.png
```

edit the `batch.py` file to have the proper images. in my case, my graphics card couldn't handle 1280 x 720 images, so I needed to scale them down to half res. 

I did this with a:

```bash
$ mkdir resized
$ cd imageseqin
$ mogrify -resize 50% -quality 100 -path ../resized *.png
```

finally, I played with a few input style images, and then settled on one using kodachrome. just replace `koda2.png` in the `batch.py` script with your filename.

```bash

$ docker run -v $(pwd):/sketch --runtime=nvidia -i -t fastphotostyle:v1.0 /bin/bash
$ python batch.py
```

The last thing remaining was to resize the images back to 720p using waifu2x:

```bash
$ python batch2Waifu2x.py
$ cd output/bigger
$ ffmpeg -i %05d.png day44.mp4
```
