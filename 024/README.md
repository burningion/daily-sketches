# day 024

sketch using matterport's [Mask_RCNN](https://github.com/matterport/Mask_RCNN) project. you'll need to have it installed and run this project in that directory.

this sketch uses Mask_RCNN to generate a series of SVGs (one per frame). these SVGs are then imported using Blender's Python interface, extruded into one another, and exported as STL.

from there, they're loaded into the Prusa Control program, and 3D printed.

you end up with a motion video artifact like what's below:

![024](https://github.com/burningion/daily-sketches/raw/master/024/images/kickflip.png)

## sketch video generated in camera today
