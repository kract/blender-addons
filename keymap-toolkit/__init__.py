bl_info = {
    "name": "Keymap Toolkit",
    "author": "KRACT",
    "version": (1, 1, 1),
    "blender": (4, 2, 0),
    "location": "Preferences > Keymap",
    "description": "Collection of curated keymap tweaks like Alt+LMB drag gestures for select modes, Z key for translate (like G key), and axis constraints.",
    "category": "Interface",
}

import bpy

addon_keymaps = []

SELECT_MODE_GESTURES = [
    ("WEST", "VERT"),
    ("SOUTH", "EDGE"),
    ("EAST", "FACE"),
]


def _ensure_mesh_keymap():
    wm = bpy.context.window_manager
    if wm is None:
        return None
    kc = wm.keyconfigs.addon
    if kc is None:
        return None
    km = kc.keymaps.get("Mesh")
    if km is None:
        km = kc.keymaps.new(name="Mesh", space_type="EMPTY", region_type="WINDOW")
    return km


def _register_select_mode_gestures(km):
    for direction, mode in SELECT_MODE_GESTURES:
        kmi = km.keymap_items.new(
            idname="mesh.select_mode",
            type="LEFTMOUSE",
            value="CLICK_DRAG",
            alt=True,
            direction=direction,
        )
        kmi.properties.type = mode
        addon_keymaps.append((km, kmi))


def _ensure_view3d_keymap():
    """Ensure 3D Viewport keymap exists"""
    wm = bpy.context.window_manager
    if wm is None:
        return None
    kc = wm.keyconfigs.addon
    if kc is None:
        return None
    km = kc.keymaps.get("3D View")
    if km is None:
        km = kc.keymaps.new(name="3D View", space_type="VIEW_3D")
    return km


def _disable_default_keys():
    """Disable G and Y keys in default keymap"""
    wm = bpy.context.window_manager
    if wm is not None:
        kc_default = wm.keyconfigs.default
        if kc_default is not None:
            km_default = kc_default.keymaps.get("3D View")
            if km_default is not None:
                for kmi in km_default.keymap_items:
                    # Disable G key for transform.translate
                    if (kmi.type == "G" and kmi.value == "PRESS" and 
                        not kmi.alt and not kmi.shift and not kmi.ctrl):
                        if (hasattr(kmi, "idname") and 
                            kmi.idname == "transform.translate"):
                            kmi.active = False
                    # Disable Y key for axis constraint
                    if (kmi.type == "Y" and kmi.value == "PRESS" and 
                        not kmi.alt and not kmi.shift and not kmi.ctrl):
                        if (hasattr(kmi, "idname") and 
                            ("transform" in kmi.idname.lower() or 
                             "constraint" in kmi.idname.lower())):
                            kmi.active = False


def _register_z_key_translate(km):
    """Register Z key for transform.translate (like G key) and disable shading pie"""
    # Disable existing Z key shading pie menu in default keymap if it exists
    wm = bpy.context.window_manager
    if wm is not None:
        kc_default = wm.keyconfigs.default
        if kc_default is not None:
            km_default = kc_default.keymaps.get("3D View")
            if km_default is not None:
                for kmi in km_default.keymap_items:
                    if (kmi.type == "Z" and kmi.value == "PRESS" and 
                        not kmi.alt and not kmi.shift and not kmi.ctrl):
                        # Check if it's a pie menu call (shading pie)
                        if (hasattr(kmi, "idname") and 
                            ("pie" in kmi.idname.lower() or 
                             "shading" in kmi.idname.lower())):
                            kmi.active = False
    
    # Register Z key for transform.translate (like G key)
    # This will override the default Z key behavior
    kmi = km.keymap_items.new(
        idname="transform.translate",
        type="Z",
        value="PRESS",
    )
    addon_keymaps.append((km, kmi))


def _register_axis_constraints(km):
    """Register X, Y, Z keys for axis constraints during transform"""
    # X axis constraint for translate
    kmi_x_translate = km.keymap_items.new(
        idname="transform.translate",
        type="X",
        value="PRESS",
        ctrl=True,
    )
    kmi_x_translate.properties.constraint_axis = (True, False, False)
    addon_keymaps.append((km, kmi_x_translate))
    
    # Y axis constraint for translate (C key)
    kmi_y_translate = km.keymap_items.new(
        idname="transform.translate",
        type="C",
        value="PRESS",
    )
    kmi_y_translate.properties.constraint_axis = (False, True, False)
    addon_keymaps.append((km, kmi_y_translate))
    
    # Z axis constraint for translate
    kmi_z_translate = km.keymap_items.new(
        idname="transform.translate",
        type="Z",
        value="PRESS",
        ctrl=True,
    )
    kmi_z_translate.properties.constraint_axis = (False, False, True)
    addon_keymaps.append((km, kmi_z_translate))
    
    # X axis constraint for rotate
    kmi_x_rotate = km.keymap_items.new(
        idname="transform.rotate",
        type="X",
        value="PRESS",
        ctrl=True,
    )
    kmi_x_rotate.properties.constraint_axis = (True, False, False)
    addon_keymaps.append((km, kmi_x_rotate))
    
    # Y axis constraint for rotate
    kmi_y_rotate = km.keymap_items.new(
        idname="transform.rotate",
        type="Y",
        value="PRESS",
        ctrl=True,
    )
    kmi_y_rotate.properties.constraint_axis = (False, True, False)
    addon_keymaps.append((km, kmi_y_rotate))
    
    # Z axis constraint for rotate
    kmi_z_rotate = km.keymap_items.new(
        idname="transform.rotate",
        type="Z",
        value="PRESS",
        ctrl=True,
    )
    kmi_z_rotate.properties.constraint_axis = (False, False, True)
    addon_keymaps.append((km, kmi_z_rotate))
    
    # X axis constraint for scale
    kmi_x_scale = km.keymap_items.new(
        idname="transform.resize",
        type="X",
        value="PRESS",
        ctrl=True,
    )
    kmi_x_scale.properties.constraint_axis = (True, False, False)
    addon_keymaps.append((km, kmi_x_scale))
    
    # Y axis constraint for scale
    kmi_y_scale = km.keymap_items.new(
        idname="transform.resize",
        type="Y",
        value="PRESS",
        ctrl=True,
    )
    kmi_y_scale.properties.constraint_axis = (False, True, False)
    addon_keymaps.append((km, kmi_y_scale))
    
    # Z axis constraint for scale
    kmi_z_scale = km.keymap_items.new(
        idname="transform.resize",
        type="Z",
        value="PRESS",
        ctrl=True,
    )
    kmi_z_scale.properties.constraint_axis = (False, False, True)
    addon_keymaps.append((km, kmi_z_scale))


def register():
    # Disable default G and Y keys
    _disable_default_keys()
    
    # Register select mode gestures
    km_mesh = _ensure_mesh_keymap()
    if km_mesh is not None:
        _register_select_mode_gestures(km_mesh)
    
    # Register Z key for translate (like G key) and axis constraints
    km_view3d = _ensure_view3d_keymap()
    if km_view3d is not None:
        _register_z_key_translate(km_view3d)
        _register_axis_constraints(km_view3d)


def unregister():
    while addon_keymaps:
        km, kmi = addon_keymaps.pop()
        if km and kmi in km.keymap_items:
            km.keymap_items.remove(kmi)
