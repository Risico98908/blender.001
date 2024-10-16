import bpy

# Path to the .obj file
obj_file_path = '/media/backup_005_6/workspace_all/blender/67101b84054b4fdb95803f84.obj'

# Import the .obj file
bpy.ops.import_scene.obj(filepath=obj_file_path)

# Confirm successful import
print(f"3D character from {obj_file_path} successfully imported into Blender.")
