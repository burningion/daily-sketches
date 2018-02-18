# day 037

sketch uses [beesandbombs](https://twitter.com/beesandbombs)' [evilTriangles](https://gist.github.com/beesandbombs/78bdf5e42cc70d8bcca2cd29c66566a3) processing code as a base to create a mask for video. 

![037](https://github.com/burningion/daily-sketches/raw/master/037/images/00112.jpg)

## sketch video generated with folowing commands

first, run the modified processing code in processing to generate mask image sequence. 

you can get processing from processing.org

```bash
$ python3 maskIt.py
$ ffmpeg -r 30 -i imageseq/%05d.jpg -i audio.aac -strict -2 day38.mp4
```

