bl_info = {
    "name": "Subamo - Backup mover to subdirectory",
    "author": "KRACT Studio",
    "version": (1, 0, 2),
    "blender": (4, 2, 0),
    "description": "Automatically organize Blender backup files (.blend1 to .blend32) into a backup subdirectory",
    "location": "File > Save",
    "category": "System"
}

if "bpy" in locals():
    import importlib
    importlib.reload(operators)
    importlib.reload(backup_manager)
    importlib.reload(panel)
    importlib.reload(handlers)
    importlib.reload(translations)
else:
    from . import operators
    from . import backup_manager
    from . import panel
    from . import handlers
    from . import translations

import bpy

classes = (
    operators.SUBAMO_OT_delete_backup,
    operators.SUBAMO_OT_open_backup,
    panel.SUBAMO_PT_panel,
)

def register():
    """アドオン登録"""
    for cls in classes:
        bpy.utils.register_class(cls)
    
    # 翻訳を登録（既に登録済みの場合はスキップ）
    try:
        bpy.app.translations.register(__name__, translations.translations_dict)
    except ValueError:
        # 既に登録済みの場合は無視
        pass
    
    # ファイル保存後のハンドラーを追加
    bpy.app.handlers.save_post.append(handlers.save_post_handler)

def unregister():
    """アドオン登録解除"""
    # ハンドラーを削除
    if handlers.save_post_handler in bpy.app.handlers.save_post:
        try:
            bpy.app.handlers.save_post.remove(handlers.save_post_handler)
        except (ValueError, AttributeError):
            pass  # Already removed
    
    # 翻訳を解除
    try:
        bpy.app.translations.unregister(__name__)
    except ValueError:
        # 登録されていない場合は無視
        pass
    
    # Safely unregister classes
    for cls in reversed(classes):
        try:
            bpy.utils.unregister_class(cls)
        except RuntimeError:
            pass  # Already unregistered

if __name__ == "__main__":
    register()
