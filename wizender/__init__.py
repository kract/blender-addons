bl_info = {
    "name": "Wizender",
    "author": "KRACT Studio",
    "version": (1, 0, 2),
    "blender": (4, 2, 0),
    "location": "Properties > Output Properties > Wizender",
    "description": "Sets render output settings based on project file name via UI button or on save.",
    "category": "Render",
    "support": "COMMUNITY",
    "doc_url": "",
    "tracker_url": "",
    "warning": "",
}

if "bpy" in locals():
    import importlib
    importlib.reload(preferences)
    importlib.reload(operators)
    importlib.reload(panel)
    importlib.reload(handlers)
else:
    from . import preferences
    from . import operators
    from . import panel
    from . import handlers

import bpy

# 登録クラス一覧
classes = (
    preferences.WIZENDER_AddonPreferences,
    panel.WIZENDER_PT_output_panel,
    operators.WIZENDER_OT_set_settings,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    if handlers.auto_render_on_save not in bpy.app.handlers.save_post:
        bpy.app.handlers.save_post.append(handlers.auto_render_on_save)
        print("[Wizender] Save handler registered.")

def unregister():
    # Safely unregister classes
    for cls in reversed(classes):
        try:
            bpy.utils.unregister_class(cls)
        except RuntimeError:
            pass  # Already unregistered

    # Safely remove handler
    if handlers.auto_render_on_save in bpy.app.handlers.save_post:
        try:
            bpy.app.handlers.save_post.remove(handlers.auto_render_on_save)
            print("[Wizender] Save handler unregistered.")
        except (ValueError, AttributeError):
            pass  # Already removed

if __name__ == "__main__":
    register()
