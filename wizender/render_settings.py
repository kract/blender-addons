import bpy
import os

def set_render_settings():
    """Set render settings based on project filename and addon preferences"""
    filepath = bpy.data.filepath
    if not filepath:
        print("[Wizender] Filepath is empty. Save the project first.")
        return

    project_name = os.path.splitext(os.path.basename(filepath))[0]
    render = bpy.context.scene.render
    
    # アドオンPreferencesから設定を取得
    addon_prefs = bpy.context.preferences.addons["wizender"].preferences

    # 出力パスの設定（プロジェクト名をプレースホルダーに置換）
    output_path = addon_prefs.output_path.replace("{project_name}", project_name)
    render.filepath = output_path

    # 出力フォーマットの設定
    render.image_settings.file_format = addon_prefs.file_format
    render.image_settings.color_mode = addon_prefs.color_mode
    render.image_settings.color_depth = addon_prefs.color_depth

    print(f"[Wizender] Render global settings applied for project '{project_name}'.")
    print(f"  - Output path: {output_path}")
    print(f"  - Format: {addon_prefs.file_format}")
    print(f"  - Color mode: {addon_prefs.color_mode}")
    print(f"  - Color depth: {addon_prefs.color_depth}")

