import bpy

# Print all objects in the current scene
for obj in bpy.data.objects:
    print(obj.name)
