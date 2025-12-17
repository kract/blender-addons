bl_info = {
    "name": "Versave - Version Manager",
    "author": "KRACT Studio",
    "version": (1, 0, 2),
    "blender": (4, 2, 0),
    "description": "Enhanced incremental save with proper versioning format (_v prefix for numbered files)",
    "location": "File > Save (Cmd+S), Save As (Cmd+Alt+S)",
    "category": "System"
}

if "bpy" in locals():
    import importlib
    importlib.reload(operators)
    importlib.reload(keymap)
else:
    from . import operators
    from . import keymap

import bpy

classes = (
    operators.VERSAVE_OT_save_initial,
    operators.VERSAVE_OT_open_version,
    operators.VERSAVE_OT_version_manager,
    operators.VERSAVE_OT_save_incremental,
)

def register():
    """アドオン登録"""
    for cls in classes:
        bpy.utils.register_class(cls)
    
    keymap.register_keymaps()

def unregister():
    """アドオン登録解除"""
    keymap.unregister_keymaps()
    
    # Safely unregister classes
    for cls in reversed(classes):
        try:
            bpy.utils.unregister_class(cls)
        except RuntimeError:
            pass  # Already unregistered

if __name__ == "__main__":
    register()