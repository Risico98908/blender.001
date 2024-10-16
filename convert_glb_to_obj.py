import bpy

# Path to the .glb file
glb_file_path = '/media/backup_005_6/workspace_all/blender/67101b84054b4fdb95803f84.glb'

# Import the .glb file
bpy.ops.import_scene.gltf(filepath=glb_file_path)

# Set the output path for the .obj file
obj_file_path = '/media/backup_005_6/workspace_all/blender/67101b84054b4fdb95803f84.obj'

# Export the scene as .obj
bpy.ops.export_scene.obj(filepath=obj_file_path)

print(f"Successfully converted {glb_file_path} to {obj_file_path}.")
