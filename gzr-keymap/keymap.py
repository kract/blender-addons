import bpy
from . import preferences

def register_keymaps():
    """Register addon keymaps"""
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon

    if not kc:
        return

    # 3D View
    km = kc.keymaps.new(name="3D View", space_type="VIEW_3D")
    
    # ビューを回転
    kmi = km.keymap_items.new("view3d.rotate", type='LEFTMOUSE', value="PRESS", ctrl=True)
    preferences.addon_keymaps.append((km, kmi))

    # 視点の移動
    kmi = km.keymap_items.new("view3d.move", type='MIDDLEMOUSE', value="PRESS", ctrl=True)
    preferences.addon_keymaps.append((km, kmi))

    # ビューをズーム
    kmi = km.keymap_items.new("view3d.zoom", type='RIGHTMOUSE', value="PRESS", ctrl=True)
    preferences.addon_keymaps.append((km, kmi))

    # 2D View
    km = kc.keymaps.new(name="View2D", space_type="EMPTY")
    
    # 視点の移動
    kmi = km.keymap_items.new("view2d.pan", type='LEFTMOUSE', value="PRESS", ctrl=True)
    preferences.addon_keymaps.append((km, kmi))

    # 視点の移動
    kmi = km.keymap_items.new("view2d.pan", type='MIDDLEMOUSE', value="PRESS", ctrl=True)
    preferences.addon_keymaps.append((km, kmi))

    # 2Dビューズーム
    kmi = km.keymap_items.new("view2d.zoom", type='RIGHTMOUSE', value="PRESS", ctrl=True)
    preferences.addon_keymaps.append((km, kmi))

    # Image Editor
    km = kc.keymaps.new(name="Image", space_type="IMAGE_EDITOR")
    
    # 視点の移動
    kmi = km.keymap_items.new("image.view_pan", type='LEFTMOUSE', value="PRESS", ctrl=True)
    preferences.addon_keymaps.append((km, kmi))

    # 視点の移動
    kmi = km.keymap_items.new("image.view_pan", type='MIDDLEMOUSE', value="PRESS", ctrl=True)
    preferences.addon_keymaps.append((km, kmi))

    # 2Dビューズーム
    kmi = km.keymap_items.new("image.view_zoom", type='RIGHTMOUSE', value="PRESS", ctrl=True)
    preferences.addon_keymaps.append((km, kmi))

    # Mesh (Edit Mode)
    km = kc.keymaps.new(name="Mesh", space_type="EMPTY")
    
    # 選択モード切り替え（頂点モード）- Alt + 左ドラッグ（左方向）
    kmi = km.keymap_items.new("mesh.select_mode", type='LEFTMOUSE', value="CLICK_DRAG", alt=True, direction='WEST')
    kmi.properties.type = 'VERT'
    preferences.addon_keymaps.append((km, kmi))

    # 選択モード切り替え（辺モード）- Alt + 左ドラッグ（下方向）
    kmi = km.keymap_items.new("mesh.select_mode", type='LEFTMOUSE', value="CLICK_DRAG", alt=True, direction='SOUTH')
    kmi.properties.type = 'EDGE'
    preferences.addon_keymaps.append((km, kmi))

    # 選択モード切り替え（面モード）- Alt + 左ドラッグ（右方向）
    kmi = km.keymap_items.new("mesh.select_mode", type='LEFTMOUSE', value="CLICK_DRAG", alt=True, direction='EAST')
    kmi.properties.type = 'FACE'
    preferences.addon_keymaps.append((km, kmi))

    # Object Mode
    km = kc.keymaps.new(name="Object Mode", space_type="EMPTY")

    # Armature
    km = kc.keymaps.new(name="Armature", space_type="EMPTY")

    # Pose
    km = kc.keymaps.new(name="Pose", space_type="EMPTY")

    # Animation
    km = kc.keymaps.new(name="Animation", space_type="EMPTY")

    # Graph Editor
    km = kc.keymaps.new(name="Graph Editor", space_type="GRAPH_EDITOR")

    # UV Editor
    km = kc.keymaps.new(name="UV Editor", space_type="EMPTY")

    # Node Editor
    km = kc.keymaps.new(name="Node Editor", space_type="NODE_EDITOR")

    # Sequencer
    km = kc.keymaps.new(name="Sequencer", space_type="SEQUENCE_EDITOR")

    # Timeline
    km = kc.keymaps.new(name="Timeline", space_type="DOPESHEET_EDITOR")

    # Grease Pencil
    # Note: brush.asset_activateエントリは削除（アセットが存在しない場合にエラーが発生するため）
    # km = kc.keymaps.new(name="Grease Pencil", space_type="EMPTY")
    # kmi = km.keymap_items.new("brush.asset_activate", type='Z', value="PRESS", repeat=True)
    # kmi.properties.asset_library_type = 'CUSTOM'
    # kmi.properties.asset_library_identifier = 'User Library'
    # preferences.addon_keymaps.append((km, kmi))

    # Sculpt
    # Note: brush.asset_activateエントリは削除（アセットが存在しない場合にエラーが発生するため）
    # km = kc.keymaps.new(name="Sculpt", space_type="EMPTY")
    # kmi = km.keymap_items.new("brush.asset_activate", type='Z', value="PRESS", repeat=True)
    # kmi.properties.asset_library_type = 'ESSENTIALS'
    # kmi.properties.asset_library_identifier = ''
    # preferences.addon_keymaps.append((km, kmi))

    # Weight Paint
    km = kc.keymaps.new(name="Weight Paint", space_type="EMPTY")

    # Outliner
    km = kc.keymaps.new(name="Outliner", space_type="OUTLINER")

def unregister_keymaps():
    """Unregister addon keymaps"""
    for (km, kmi) in preferences.addon_keymaps:
        try:
            km.keymap_items.remove(kmi)
        except (KeyError, ReferenceError):
            pass  # Keymap item already removed
    preferences.addon_keymaps.clear()

