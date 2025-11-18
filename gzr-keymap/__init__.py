bl_info = {
    "name": "GZR Keymap",
    "author": "KRACT",
    "version": (1, 0, 0),
    "blender": (4, 2, 0),
    "description": "Custom keymap for viewport navigation",
    "category": "UI",
}

import bpy

addon_keymaps = []


def register():
    """Register addon"""
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon

    if not kc:
        return

    # 3D View
    km = kc.keymaps.new(name="3D View", space_type="VIEW_3D")
    
    # ビューを回転
    kmi = km.keymap_items.new("view3d.rotate", type='LEFTMOUSE', value="PRESS", alt=True)
    addon_keymaps.append((km, kmi))

    # 視点の移動
    kmi = km.keymap_items.new("view3d.move", type='MIDDLEMOUSE', value="PRESS", alt=True)
    addon_keymaps.append((km, kmi))

    # ビューをズーム
    kmi = km.keymap_items.new("view3d.zoom", type='RIGHTMOUSE', value="PRESS", alt=True)
    addon_keymaps.append((km, kmi))

    # 2D View
    km = kc.keymaps.new(name="View2D", space_type="EMPTY")
    
    # 視点の移動
    kmi = km.keymap_items.new("view2d.pan", type='LEFTMOUSE', value="PRESS", alt=True)
    addon_keymaps.append((km, kmi))

    # 視点の移動
    kmi = km.keymap_items.new("view2d.pan", type='MIDDLEMOUSE', value="PRESS", alt=True)
    addon_keymaps.append((km, kmi))

    # 2Dビューズーム
    kmi = km.keymap_items.new("view2d.zoom", type='RIGHTMOUSE', value="PRESS", alt=True)
    addon_keymaps.append((km, kmi))

    # Image Editor
    km = kc.keymaps.new(name="Image", space_type="IMAGE_EDITOR")
    
    # 視点の移動
    kmi = km.keymap_items.new("image.view_pan", type='LEFTMOUSE', value="PRESS", alt=True)
    addon_keymaps.append((km, kmi))

    # 視点の移動
    kmi = km.keymap_items.new("image.view_pan", type='MIDDLEMOUSE', value="PRESS", alt=True)
    addon_keymaps.append((km, kmi))

    # 2Dビューズーム
    kmi = km.keymap_items.new("image.view_zoom", type='RIGHTMOUSE', value="PRESS", alt=True)
    addon_keymaps.append((km, kmi))


def unregister():
    """Unregister addon"""
    for (km, kmi) in addon_keymaps:
        try:
            km.keymap_items.remove(kmi)
        except (KeyError, ReferenceError):
            pass  # Keymap item already removed
    addon_keymaps.clear()


if __name__ == '__main__':
    register()

