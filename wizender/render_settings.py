import bpy
import os

def set_render_settings():
    """Set render settings based on project filename and addon preferences"""
    filepath = bpy.data.filepath
    if not filepath:
        print("[Wizender] Filepath is empty. Save the project first.")
        return

    project_name = os.path.splitext(os.path.basename(filepath))[0]
    addon_prefs = bpy.context.preferences.addons[__package__].preferences

    for scene in bpy.data.scenes:
        scene_name = scene.name
        output_path = (
            addon_prefs.output_path
            .replace("{project_name}", project_name)
            .replace("{scene_name}", scene_name)
        )
        render = scene.render
        render.filepath = output_path
        render.image_settings.file_format = addon_prefs.file_format
        render.image_settings.color_mode = addon_prefs.color_mode
        render.image_settings.color_depth = addon_prefs.color_depth

        print(f"[Wizender] Settings applied: scene='{scene_name}' path='{output_path}'")

