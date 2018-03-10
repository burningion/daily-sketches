import bpy

context = bpy.context
scene = context.scene

bpy.ops.import_curve.svg(filepath="/home/stankley/Development/Mask_RCNN/kickflipSVG/00000.svg")
bpy.context.scene.objects.active = bpy.data.objects['Curve']

bpy.context.object.scale[0] = 50
bpy.context.object.scale[1] = 50
bpy.context.object.scale[2] = 50

bpy.data.objects['Curve'].data.extrude = .004
bpy.data.objects['Curve'].data.fill_mode = 'NONE'
meshy = bpy.data.objects['Curve'].to_mesh(scene, False, 'PREVIEW')
bpy.ops.object.modifier_add(type='SOLIDIFY')
bpy.context.object.modifiers["Solidify"].thickness = 0.006

for i in range(1, 99):
    bpy.ops.import_curve.svg(filepath="/home/stankley/Development/Mask_RCNN/kickflipSVG/%05d.svg" % i)
    bpy.context.scene.objects.active = bpy.data.objects['Curve.%03d' % i]
    bpy.context.object.scale[0] = 50
    bpy.context.object.scale[1] = 50
    bpy.context.object.scale[2] = 50
    meshy = bpy.data.objects['Curve.%03d' % i].to_mesh(scene, False, 'PREVIEW')
    bpy.data.objects['Curve.%03d' % i].location = Vector((0, 0, .38 * i))
    bpy.data.objects['Curve.%03d' % i].data.fill_mode = 'NONE'
    bpy.data.objects['Curve.%03d' % i].data.extrude = .004
    bpy.ops.object.modifier_add(type='SOLIDIFY')
    bpy.context.object.modifiers["Solidify"].thickness = 0.006
