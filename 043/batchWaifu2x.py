import glob
import subprocess

counter = 1

for filename in glob.glob('output/*.png'):
    subprocess.call('nvidia-docker run -v `pwd`/output:/images waifu2x th waifu2x.lua -force_cudnn 1 -m scale -scale 2 -i /images/%05d.png -o /images/bigger/%05d.png' % (counter, counter), shell=True)
    counter += 1
