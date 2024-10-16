import bpy

# Set up scene settings for rendering
bpy.context.scene.render.image_settings.file_format = 'FFMPEG'
bpy.context.scene.render.ffmpeg.format = 'MPEG4'
bpy.context.scene.render.ffmpeg.codec = 'H264'
bpy.context.scene.render.ffmpeg.constant_rate_factor = 'HIGH'
bpy.context.scene.render.ffmpeg.ffmpeg_preset = 'GOOD'
bpy.context.scene.render.resolution_x = 1920
bpy.context.scene.render.resolution_y = 1080
bpy.context.scene.render.fps = 24

# Set output file path for the video
bpy.context.scene.render.filepath = '/media/backup_005_6/workspace_all/blender/arm_animation.mp4'

# Clear existing animation data
bpy.context.scene.frame_start = 0
bpy.context.scene.frame_end = 50
bpy.context.scene.frame_set(0)

# Select the armature (assuming there is one)
armature = bpy.data.objects['Armature']  # Make sure your rigged object is named 'Armature'
bpy.context.view_layer.objects.active = armature
bpy.ops.object.mode_set(mode='POSE')

# Select the left arm bone
left_arm_bone = armature.pose.bones['LeftArm']  # Ensure this matches the actual bone name in your rig
right_arm_bone = armature.pose.bones['RightArm']  # Ensure this matches the actual bone name in your rig

# Set initial rotation for both arms at frame 0
left_arm_bone.rotation_euler = (0.0, 0.0, 0.0)
right_arm_bone.rotation_euler = (0.0, 0.0, 0.0)
left_arm_bone.keyframe_insert(data_path="rotation_euler", frame=0)
right_arm_bone.keyframe_insert(data_path="rotation_euler", frame=0)

# Set rotation for both arms at frame 25 (arms up)
bpy.context.scene.frame_set(25)
left_arm_bone.rotation_euler = (0.0, 0.0, 1.0)  # Adjust the rotation as needed
right_arm_bone.rotation_euler = (0.0, 0.0, -1.0)  # Adjust the rotation as needed
left_arm_bone.keyframe_insert(data_path="rotation_euler", frame=25)
right_arm_bone.keyframe_insert(data_path="rotation_euler", frame=25)

# Set rotation for both arms at frame 50 (arms down)
bpy.context.scene.frame_set(50)
left_arm_bone.rotation_euler = (0.0, 0.0, 0.0)
right_arm_bone.rotation_euler = (0.0, 0.0, 0.0)
left_arm_bone.keyframe_insert(data_path="rotation_euler", frame=50)
right_arm_bone.keyframe_insert(data_path="rotation_euler", frame=50)

# Return to object mode
bpy.ops.object.mode_set(mode='OBJECT')

# Set up rendering parameters
bpy.context.scene.render.filepath = '/media/backup_005_6/workspace_all/blender/arm_animation.mp4'

# Render animation as video
bpy.ops.render.render(animation=True, write_still=False)

print("MP4 video rendered and saved as /media/backup_005_6/workspace_all/blender/arm_animation.mp4")
