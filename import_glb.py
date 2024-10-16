import bpy

# Path to the .glb file
glb_file_path = '/media/backup_005_6/workspace_all/blender/67101b84054b4fdb95803f84.glb'

# Import the .glb file
bpy.ops.import_scene.gltf(filepath=glb_file_path)

# Confirm successful import
print(f"3D character from {glb_file_path} successfully imported into Blender.")
