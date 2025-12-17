import bpy
import platform

# キーマップ用の変数
addon_keymaps = []

def register_keymaps():
    """キーボードショートカットを追加"""
    wm = bpy.context.window_manager
    if wm.keyconfigs.addon:
        km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')
        
        # macOS用にosmyかどうかでキーマップを変更
        is_macos = platform.system() == 'Darwin'
        
        # View to Camera (Cmd+Shift+C / Ctrl+Shift+C)
        kmi1 = km.keymap_items.new(
            'viewcam.set_view_to_camera',
            type='C',
            value='PRESS',
            oskey=is_macos,
            ctrl=not is_macos,
            shift=True
        )
        addon_keymaps.append((km, kmi1))
        
        # Toggle Camera to View (Cmd+Shift+Alt+C / Ctrl+Shift+Alt+C)
        kmi2 = km.keymap_items.new(
            'viewcam.toggle_camera_to_view',
            type='C',
            value='PRESS',
            oskey=is_macos,
            ctrl=not is_macos,
            shift=True,
            alt=True
        )
        addon_keymaps.append((km, kmi2))

def unregister_keymaps():
    """キーボードショートカットを削除"""
    for km, kmi in addon_keymaps:
        try:
            km.keymap_items.remove(kmi)
        except (KeyError, ReferenceError):
            pass  # Keymap item already removed
    addon_keymaps.clear()

