import bpy

# Clear all existing objects
bpy.ops.wm.read_factory_settings(use_empty=True)

# Import the OBJ character model
obj_file_path = '/media/backup_005_6/workspace_all/blender/67101b84054b4fdb95803f84.obj'
bpy.ops.import_scene.obj(filepath=obj_file_path)

# Create an armature for the character
bpy.ops.object.armature_add(enter_editmode=True, location=(0, 0, 0))
armature = bpy.context.object
armature.name = 'Armature'

# Add bones for the body and arms
bpy.ops.object.mode_set(mode='EDIT')
armature_data = armature.data

# Create bone for the body
bone_body = armature_data.edit_bones.new('Body')
bone_body.head = (0, 0, 0)
bone_body.tail = (0, 0, 1.5)

# Create bones for the arms
bone_left_arm = armature_data.edit_bones.new('Left Arm')
bone_left_arm.head = (0, 0, 1.5)
bone_left_arm.tail = (-0.5, 0, 2)

bone_right_arm = armature_data.edit_bones.new('Right Arm')
bone_right_arm.head = (0, 0, 1.5)
bone_right_arm.tail = (0.5, 0, 2)

# Switch back to object mode
bpy.ops.object.mode_set(mode='OBJECT')

# Parent the character mesh to the armature
character = bpy.context.selected_objects[0]  # Assuming it's the imported character
character.select_set(True)
armature.select_set(True)
bpy.context.view_layer.objects.active = armature
bpy.ops.object.parent_set(type='ARMATURE_AUTO')

# Enter pose mode to animate
bpy.ops.object.mode_set(mode='POSE')

# Get the pose bones
left_arm_bone = armature.pose.bones['Left Arm']
right_arm_bone = armature.pose.bones['Right Arm']

# Set the animation keyframes for the arms (moving up and down)
scene = bpy.context.scene
fps = scene.render.fps  # Frames per second
animation_duration = 10  # Duration in seconds
total_frames = fps * animation_duration

# Set keyframes at the start
left_arm_bone.rotation_euler = (0, 0, 0)
right_arm_bone.rotation_euler = (0, 0, 0)
left_arm_bone.keyframe_insert(data_path="rotation_euler", frame=1)
right_arm_bone.keyframe_insert(data_path="rotation_euler", frame=1)

# Set keyframes at the halfway point (arms up)
left_arm_bone.rotation_euler = (0, 0, 1.0)  # Rotate left arm
right_arm_bone.rotation_euler = (0, 0, -1.0)  # Rotate right arm
left_arm_bone.keyframe_insert(data_path="rotation_euler", frame=total_frames // 2)
right_arm_bone.keyframe_insert(data_path="rotation_euler", frame=total_frames // 2)

# Set keyframes at the end (arms down)
left_arm_bone.rotation_euler = (0, 0, 0)
right_arm_bone.rotation_euler = (0, 0, 0)
left_arm_bone.keyframe_insert(data_path="rotation_euler", frame=total_frames)
right_arm_bone.keyframe_insert(data_path="rotation_euler", frame=total_frames)

# Switch back to object mode before adding the camera
bpy.ops.object.mode_set(mode='OBJECT')

# Set up the camera
bpy.ops.object.camera_add(location=(0, -5, 1.5))
camera = bpy.context.object
bpy.context.scene.camera = camera

# Set up the light
bpy.ops.object.light_add(type='POINT', radius=1, location=(0, -3, 5))
light = bpy.context.object
light.data.energy = 1000

# Set the render resolution and animation settings
scene.render.resolution_x = 1920
scene.render.resolution_y = 1080
scene.render.fps = fps
scene.frame_start = 1
scene.frame_end = total_frames

# Set the output path for the rendered animation
scene.render.filepath = '/media/backup_005_6/workspace_all/blender/character_animation.mp4'
scene.render.image_settings.file_format = 'FFMPEG'
scene.render.ffmpeg.format = 'MPEG4'
scene.render.ffmpeg.codec = 'H264'
scene.render.ffmpeg.constant_rate_factor = 'HIGH'

# Render the animation
bpy.ops.render.render(animation=True)

print("Animation rendered and saved to /media/backup_005_6/workspace_all/blender/character_animation.mp4")
