import bpy

bl_info = {
    "name": "Keymap Toolkit",
    "author": "KRACT",
    "version": (0, 0, 1),
    "blender": (4, 2, 0),
    "description": "Customize Blender keymaps by overriding default key bindings",
    "location": "3D Viewport",
    "category": "3D View"
}

# Store references to disabled keymap items and new keymap items
disabled_keymap_items = []
new_keymap_items = []
addon_keymaps = []


def disable_keymap_item(keymap, key_type, value='PRESS', shift=False, ctrl=False, alt=False, oskey=False):
    """Disable a keymap item by finding and deactivating it"""
    for kmi in keymap.keymap_items:
        if (kmi.type == key_type and 
            kmi.value == value and
            kmi.shift == shift and
            kmi.ctrl == ctrl and
            kmi.alt == alt and
            kmi.oskey == oskey):
            kmi.active = False
            disabled_keymap_items.append((keymap, kmi))
            return True
    return False




def register():
    """Register addon and apply keymap overrides"""
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.default
    
    # Get 3D View keymap
    km = kc.keymaps.get('3D View')
    if not km:
        return
    
    # Disable G key (grab/translate)
    disable_keymap_item(km, 'G', 'PRESS')
    
    # Disable Y key
    disable_keymap_item(km, 'Y', 'PRESS')
    
    # Disable Z key (shading pie menu) and replace with grab
    # Find and disable all Z key bindings that are shading pie menu
    for kmi in km.keymap_items:
        if kmi.type == 'Z' and kmi.value == 'PRESS' and not kmi.shift and not kmi.ctrl and not kmi.alt:
            # Check if it's the shading pie menu
            if kmi.idname == 'wm.call_menu_pie':
                if hasattr(kmi, 'properties') and hasattr(kmi.properties, 'name'):
                    if 'shading' in kmi.properties.name.lower():
                        kmi.active = False
                        disabled_keymap_items.append((km, kmi))
                else:
                    # Disable any call_menu_pie on Z
                    kmi.active = False
                    disabled_keymap_items.append((km, kmi))
    
    # Add new Z key binding for grab (transform.translate)
    kmi_z = km.keymap_items.new('transform.translate', 'Z', 'PRESS')
    new_keymap_items.append((km, kmi_z))
    
    # Note: Axis constraint modification (Y to C) is not directly possible
    # because Transform Modal Map is a modal keymap that cannot be modified
    # through the standard keymap API. This would require a custom modal operator
    # which is beyond the scope of this addon. Users will need to manually
    # configure axis constraints in Blender's keymap preferences if needed.


def unregister():
    """Unregister addon and restore keymap overrides"""
    # Restore disabled keymap items
    for km, kmi in disabled_keymap_items:
        if km and kmi:
            # Check if the keymap item still exists
            if kmi in km.keymap_items:
                kmi.active = True
    
    # Remove keymap items we added
    for km, kmi in new_keymap_items:
        if km and kmi:
            if kmi in km.keymap_items:
                km.keymap_items.remove(kmi)
    
    # Remove addon keymaps
    for km, kmi in addon_keymaps:
        if km and kmi:
            if kmi in km.keymap_items:
                km.keymap_items.remove(kmi)
    
    disabled_keymap_items.clear()
    new_keymap_items.clear()
    addon_keymaps.clear()


if __name__ == "__main__":
    register()

