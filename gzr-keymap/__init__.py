bl_info = {
    "name": "GZR Keymap",
    "author": "KRACT Studio",
    "version": (1, 0, 1),
    "blender": (4, 2, 0),
    "description": "Custom keymap for viewport navigation",
    "category": "UI",
}

if "bpy" in locals():
    import importlib
    importlib.reload(preferences)
    importlib.reload(keymap)
else:
    from . import preferences
    from . import keymap

import bpy

classes = (preferences.GZR_KEYMAP_AddonPreferences,)

def register():
    """Register addon"""
    for cls in classes:
        bpy.utils.register_class(cls)
    
    keymap.register_keymaps()

def unregister():
    """Unregister addon"""
    keymap.unregister_keymaps()
    
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

if __name__ == '__main__':
    register()

