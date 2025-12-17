import bpy

# Keymap management
addon_keymaps = []
_original_builtin_viewpie_draw = None

def _viewpie_builtin_draw(self, context):
    """Redirect Blender's default view pie menu to Viewpie's layout."""
    from . import menus
    return menus.VIEWPIE_MT_pie_menu.draw(self, context)

def register_keymaps():
    """Register addon keymaps"""
    # Hook into Blender's default VIEW3D_MT_view_pie so external keymaps
    # that call it will display Viewpie's layout.
    global _original_builtin_viewpie_draw
    builtin_viewpie = getattr(bpy.types, "VIEW3D_MT_view_pie", None)
    if builtin_viewpie and _original_builtin_viewpie_draw is None:
        _original_builtin_viewpie_draw = builtin_viewpie.draw
        builtin_viewpie.draw = _viewpie_builtin_draw
    
    # Add keymap
    wm = bpy.context.window_manager
    if wm.keyconfigs.addon:
        km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')
        
        # Basic pie menu (Q key)
        kmi1 = km.keymap_items.new(
            'viewpie.call_pie_menu',
            type='Q',
            value='PRESS'
        )
        kmi1.properties.extended = False
        addon_keymaps.append((km, kmi1))
        
        # Extended pie menu (Shift+Q)
        kmi2 = km.keymap_items.new(
            'viewpie.call_pie_menu',
            type='Q',
            value='PRESS',
            shift=True
        )
        kmi2.properties.extended = True
        addon_keymaps.append((km, kmi2))

def unregister_keymaps():
    """Unregister addon keymaps"""
    global _original_builtin_viewpie_draw
    builtin_viewpie = getattr(bpy.types, "VIEW3D_MT_view_pie", None)
    if builtin_viewpie and _original_builtin_viewpie_draw is not None:
        builtin_viewpie.draw = _original_builtin_viewpie_draw
        _original_builtin_viewpie_draw = None

    # Remove keymap
    for km, kmi in addon_keymaps:
        try:
            km.keymap_items.remove(kmi)
        except (KeyError, ReferenceError):
            pass  # Keymap item already removed
    addon_keymaps.clear()

