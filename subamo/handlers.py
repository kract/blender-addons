import bpy
from bpy.app.handlers import persistent
from . import backup_manager

@persistent
def save_post_handler(dummy):
    """ファイル保存後にバックアップファイルを自動整理"""
    try:
        current_filepath = bpy.data.filepath
        if current_filepath:
            backup_manager.organize_backup_files(current_filepath)
    except Exception as e:
        print(f"Subamo: Error organizing backup files: {str(e)}")

