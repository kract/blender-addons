import bpy

# Keymap management
addon_keymaps = []

def register_keymaps():
    """Register addon keymaps"""
    # Add keymap with higher priority
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        # Object mode keymap
        km_object = kc.keymaps.new(name='Object Mode', space_type='EMPTY')
        
        # X key for smart delete in object mode
        kmi_obj = km_object.keymap_items.new(
            'nukeshima.smart_delete',
            type='X',
            value='PRESS'
        )
        addon_keymaps.append((km_object, kmi_obj))
        
        # Shift+X for menu in object mode
        kmi_obj2 = km_object.keymap_items.new(
            'wm.call_menu',
            type='X',
            value='PRESS',
            shift=True
        )
        kmi_obj2.properties.name = "NUKESHIMA_MT_delete_menu"
        addon_keymaps.append((km_object, kmi_obj2))
        
        # Mesh edit mode keymap
        km_mesh = kc.keymaps.new(name='Mesh', space_type='EMPTY')
        
        # X key for smart delete in edit mode
        kmi_mesh = km_mesh.keymap_items.new(
            'nukeshima.smart_delete',
            type='X',
            value='PRESS'
        )
        addon_keymaps.append((km_mesh, kmi_mesh))
        
        # Shift+X for menu in edit mode
        kmi_mesh2 = km_mesh.keymap_items.new(
            'wm.call_menu',
            type='X',
            value='PRESS',
            shift=True
        )
        kmi_mesh2.properties.name = "NUKESHIMA_MT_delete_menu"
        addon_keymaps.append((km_mesh, kmi_mesh2))

def unregister_keymaps():
    """Unregister addon keymaps"""
    # Remove keymap
    for km, kmi in addon_keymaps:
        try:
            km.keymap_items.remove(kmi)
        except (KeyError, ReferenceError):
            pass  # Keymap item already removed
    addon_keymaps.clear()

