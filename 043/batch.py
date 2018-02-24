import glob
import subprocess

counter = 1
for filename in glob.glob('resized/*.png'):
    subprocess.call('python demo.py --content_image_path resized/%05d.png --style_image_path koda2.png --output_image_path output/%05d.png' % (counter, counter), shell=True)
    counter += 1
