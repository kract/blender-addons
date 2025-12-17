bl_info = {
    "name": "Viewcam",
    "author": "KRACT Studio",
    "version": (1, 0, 1),
    "blender": (4, 2, 0),
    "description": "Set current viewport view to active camera instantly",
    "location": "3D Viewport Header, shortcut: Cmd+Shift+C / Cmd+Shift+Alt+C",
    "category": "Camera"
}

if "bpy" in locals():
    import importlib
    importlib.reload(operators)
    importlib.reload(ui)
    importlib.reload(keymap)
else:
    from . import operators
    from . import ui
    from . import keymap

import bpy

classes = (
    operators.VIEWCAM_OT_set_view_to_camera,
    operators.VIEWCAM_OT_toggle_camera_to_view,
)

def register():
    """アドオン登録"""
    for cls in classes:
        bpy.utils.register_class(cls)
    
    bpy.types.VIEW3D_HT_header.append(ui.draw_viewcam_button)
    
    keymap.register_keymaps()

def unregister():
    """アドオン登録解除"""
    keymap.unregister_keymaps()
    
    # Safely remove menu draw function
    try:
        bpy.types.VIEW3D_HT_header.remove(ui.draw_viewcam_button)
    except (ValueError, AttributeError):
        pass  # Already removed or doesn't exist
    
    # Safely unregister classes
    for cls in reversed(classes):
        try:
            bpy.utils.unregister_class(cls)
        except RuntimeError:
            pass  # Already unregistered

if __name__ == "__main__":
    register()
