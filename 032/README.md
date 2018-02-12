# day 032

sketch inspired by the [optical flow example](https://docs.opencv.org/3.3.1/d7/d8b/tutorial_py_lucas_kanade.html) from opencv's docs, along with the [book of shaders](https://thebookofshaders.com/13/) fractal brownian motion chapter.

mixing the optical flow of a pre-recorded shader with a stream from the webcam.

![032](https://github.com/burningion/daily-sketches/raw/master/032/images/00396.jpg)

## sketch video generated with following commands

used vs code extension from [actuarian](https://twitter.com/actarian/status/962614767067295744) to visualize gpu  code, and recorded screen with gpu compiled version of ffmpeg with following command:

```bash
$ ./ffmpeg -hwaccel cuvid -f x11grab -r 60 -s 1280x720 -i :1.0+160,200 -vcodec h264_nvenc  -threads 0 video.mkv
```

with that done, I then also recorded a video from the webcam using ffmpeg to pass into the source video

```bash
$ ffmpeg -f v4l2 -framerate 25 -video_size 1280x720 -i /dev/video0 webcam.mkv
```

with that, the program can then be run.

```bash
$ mkdir imageseq
$ python3 opt_flow.py
$ cd imagesq
$ ffmpeg  -i %05d.jpg day29.mp4
```

