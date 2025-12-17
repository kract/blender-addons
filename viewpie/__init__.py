bl_info = {
    "name": "Viewpie",
    "author": "KRACT Studio",
    "version": (1, 0, 1),
    "blender": (4, 2, 0),
    "description": "Navigate 3D viewport with an intuitive pie menu for quick view changes",
    "location": "3D Viewport: Q key (customizable)",
    "category": "3D View"
}

if "bpy" in locals():
    import importlib
    importlib.reload(operators)
    importlib.reload(menus)
    importlib.reload(keymap)
else:
    from . import operators
    from . import menus
    from . import keymap

import bpy

classes = (
    operators.VIEWPIE_OT_set_view,
    operators.VIEWPIE_OT_toggle_projection,
    operators.VIEWPIE_OT_call_pie_menu,
    menus.VIEWPIE_MT_pie_menu,
    menus.VIEWPIE_MT_pie_menu_extended,
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
