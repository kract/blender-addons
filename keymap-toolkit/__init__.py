bl_info = {
    "name": "Keymap Toolkit",
    "author": "KRACT",
    "version": (1, 0, 0),
    "blender": (3, 0, 0),
    "location": "Preferences > Keymap",
    "description": "Collection of curated keymap tweaks like Alt+LMB drag gestures for select modes.",
    "category": "Interface",
}

import bpy

addon_keymaps = []

# Matches the gesture directions recovered from .idea/.py
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


def register():
    km = _ensure_mesh_keymap()
    if km is None:
        return
    _register_select_mode_gestures(km)


def unregister():
    while addon_keymaps:
        km, kmi = addon_keymaps.pop()
        if km and kmi in km.keymap_items:
            km.keymap_items.remove(kmi)
