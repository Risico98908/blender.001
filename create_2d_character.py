import bpy

# Clear existing mesh
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# Set to 2D mode
bpy.context.scene.view_settings.view_transform = 'Standard'

# Add head (circle)
bpy.ops.mesh.primitive_circle_add(vertices=32, radius=1, fill_type='NGON', location=(0, 0, 0))
head = bpy.context.object
head.name = "Head"

# Add body (rectangle)
bpy.ops.mesh.primitive_plane_add(size=2, location=(0, -2, 0))
body = bpy.context.object
body.scale[1] = 1.5
body.name = "Body"

# Add left arm (rectangle)
bpy.ops.mesh.primitive_plane_add(size=0.5, location=(-1.5, -2, 0))
left_arm = bpy.context.object
left_arm.scale[1] = 0.75
left_arm.name = "Left Arm"

# Add right arm (rectangle)
bpy.ops.mesh.primitive_plane_add(size=0.5, location=(1.5, -2, 0))
right_arm = bpy.context.object
right_arm.scale[1] = 0.75
right_arm.name = "Right Arm"

# Add left leg (rectangle)
bpy.ops.mesh.primitive_plane_add(size=0.75, location=(-0.5, -4, 0))
left_leg = bpy.context.object
left_leg.scale[1] = 1.25
left_leg.name = "Left Leg"

# Add right leg (rectangle)
bpy.ops.mesh.primitive_plane_add(size=0.75, location=(0.5, -4, 0))
right_leg = bpy.context.object
right_leg.scale[1] = 1.25
right_leg.name = "Right Leg"

# Group everything together into a collection for easy manipulation
bpy.ops.object.select_all(action='DESELECT')
head.select_set(True)
body.select_set(True)
left_arm.select_set(True)
right_arm.select_set(True)
left_leg.select_set(True)
right_leg.select_set(True)

bpy.ops.object.join()

# Apply transformations for clarity
bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS', center='BOUNDS')
bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

# Save the Blender scene as a .blend file
bpy.ops.wm.save_as_mainfile(filepath='/media/backup_005_6/workspace_all/blender/2d_character.blend')

print("2D character saved to /media/backup_005_6/workspace_all/blender/2d_character.blend")
