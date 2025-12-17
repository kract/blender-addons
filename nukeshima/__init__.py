bl_info = {
    "name": "Nukeshima",
    "author": "KRACT Studio",
    "version": (1, 0, 1),
    "blender": (4, 2, 0),
    "description": "Silent deletion without annoying confirmation dialogs - just nuke it instantly",
    "location": "3D Viewport: X key (replaces default delete)",
    "category": "3D View"
}

if "bpy" in locals():
    import importlib
    importlib.reload(operators)
    importlib.reload(menu)
    importlib.reload(keymap)
else:
    from . import operators
    from . import menu
    from . import keymap

import bpy

classes = (
    operators.NUKESHIMA_OT_silent_delete,
    operators.NUKESHIMA_OT_smart_delete,
    menu.NUKESHIMA_MT_delete_menu,
)

def register():
    """Register addon"""
    for cls in classes:
        bpy.utils.register_class(cls)
    
    keymap.register_keymaps()

def unregister():
    """Unregister addon"""
    keymap.unregister_keymaps()
    
    # Safely unregister classes
    for cls in reversed(classes):
        try:
            bpy.utils.unregister_class(cls)
        except RuntimeError:
            pass  # Already unregistered

if __name__ == "__main__":
    register()
