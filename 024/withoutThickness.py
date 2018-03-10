# to import the damn things into blender
import bpy

bpy.ops.import_curve.svg(filepath="/home/stankley/Development/Mask_RCNN/kickflipSVG/00000.svg")
bpy.data.objects['Curve'].data.extrude = .01
bpy.data.objects['Curve'].data.fill_mode = 'NONE'

for i in range(1, 99):
    bpy.ops.import_curve.svg(filepath="/home/stankley/Development/Mask_RCNN/kickflipSVG/%05d.svg" % i)
    bpy.data.objects['Curve.%03d' % i].location = Vector((0, 0, .01 * i))
    bpy.data.objects['Curve.%03d' % i].data.extrude = .01
    bpy.data.objects['Curve.%03d' % i].data.fill_mode = 'NONE'
