# day 011

testing out the glumpy library as a replacement for pygame

![011](https://github.com/burningion/daily-sketches/raw/master/011/images/00026.png)

## sketch video generated from following commands


```bash
$ sudo apt-get install libglf3
$ sudo pip3 install glumpy
$ python3 squares.py
```

at this point, I tried my normal approach of saving frame images in sequence.

it didn't work, as the internal clock of glumpy is different.

so instead, I downloaded and used the [nvidia accelerated hardware h264 encoder version of ffmpeg](https://developer.nvidia.com/ffmpeg). I then recorded straight from my ubuntu desktop with the following commands:

```bash
$ ./ffmpeg -hwaccel cuvid -f x11grab -r 60 -s 800x800 -i :1.0+160,100 -vcodec h264_nvenc  -threads 0 video.mkv
$ ffmpeg -i video.mkv -crf 10 -vf "scale=640:640,setpts=1.0*PTS" -c:a copy -tune grain out.mp4
```
