import bpy

# Clear existing scene
bpy.ops.wm.read_factory_settings(use_empty=True)

# Path to the .obj file
obj_file_path = '/media/backup_005_6/workspace_all/blender/67101b84054b4fdb95803f84.obj'

# Import the .obj file
bpy.ops.import_scene.obj(filepath=obj_file_path)

# Print all objects in the scene after importing
for obj in bpy.data.objects:
    print(obj.name)

# Assume the imported object is named "Cube" (adjust as needed based on the output from the list)
armature = bpy.data.objects['Cube']  # Replace 'Cube' if the object is named differently after import

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

# Set up animation frames
bpy.context.scene.frame_start = 0
bpy.context.scene.frame_end = 50

# Assume there is no armature; apply rotation directly to the object
bpy.context.view_layer.objects.active = armature

# Set initial rotation for both arms at frame 0 (use the imported object's rotation)
bpy.context.scene.frame_set(0)
armature.rotation_euler = (0.0, 0.0, 0.0)
armature.keyframe_insert(data_path="rotation_euler", frame=0)

# Rotate arms (object) at frame 25
bpy.context.scene.frame_set(25)
armature.rotation_euler = (0.0, 1.0, 0.0)  # Adjust rotation as necessary
armature.keyframe_insert(data_path="rotation_euler", frame=25)

# Reset rotation at frame 50
bpy.context.scene.frame_set(50)
armature.rotation_euler = (0.0, 0.0, 0.0)
armature.keyframe_insert(data_path="rotation_euler", frame=50)

# Render animation as video
bpy.ops.render.render(animation=True, write_still=False)

print("MP4 video rendered and saved as /media/backup_005_6/workspace_all/blender/arm_animation.mp4")
