import cv2
import subprocess
import glob, os
from aubio import source, onset

win_s = 512                 # fft size
hop_s = win_s // 2          # hop size

filename = 'chrisgap.mov'
vid = cv2.VideoCapture(filename)
fps = vid.get(cv2.CAP_PROP_FPS)
resolution = (vid.get(cv2.CAP_PROP_FRAME_WIDTH), vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
duration = vid.get(cv2.CAP_PROP_FRAME_COUNT)

print(int(fps))
print(resolution)
print(duration)

samplerate = 0
s = source(filename, samplerate, hop_s)
samplerate = s.samplerate

# uses 'hfc' to detect percussive onsets. for more options
# check out https://aubio.org/manpages/latest/aubioonset.1.html
o = onset("hfc", win_s, hop_s, samplerate)

# list of onsets, in samples
onsets = []

# total number of frames read
total_frames = 0

while True:
    samples, read = s()
    if o(samples):
        # save strength and when it happened
        onsets.append((o.get_thresholded_descriptor(), o.get_last_s()))
    total_frames += read
    if read < hop_s: break
onsets.sort(key= lambda x: x[0], reverse=True)

# generate frame nos to swap between invisible / visible based on strongest onsets
# w/ 2s gap at least
if abs(onsets[0][1] - onsets[1][1]) < 2:
    frames = [int(onsets[0][1] * fps), int(onsets[2][1] * fps)]
else:
    frames = [int(onsets[0][1] * fps), int(onsets[1][1] * fps)]

print(frames)

directoryname = filename.split('.')[0]
os.mkdir(directoryname)
subprocess.call(str("ffmpeg -i %s -q:v 1 -f image2 %s/%%05d.png" % (filename, directoryname)).split(' '))
subprocess.call(str("ffmpeg -i %s %s.mp3" % (filename, filename.split('.')[0])).split(' '))
subprocess.call(str("python3 onsetinvisible.py %s %i %i" % (directoryname, frames[0], frames[1])).split(' '))
createvideoout = "ffmpeg -r %i -i %sout/%%05d.jpg -i %s.mp3 -pix_fmt yuv420p -strict -2 %s.mp4" % (int(fps), directoryname, filename.split('.')[0], filename.split('.')[0] + 'out')
subprocess.call(createvideoout.split(' '))
