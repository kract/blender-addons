import bpy

# キーマップ用の変数
addon_keymaps = []

def register_keymaps():
    """キーボードショートカットを追加"""
    wm = bpy.context.window_manager
    if wm.keyconfigs.addon:
        km = wm.keyconfigs.addon.keymaps.new(name='Window', space_type='EMPTY')
        
        # Cmd+S をオーバーライド（初回保存時に_v1付き）
        kmi_save = km.keymap_items.new(
            'versave.save_initial',
            type='S',
            value='PRESS',
            oskey=True  # macOSのCommandキー
        )
        addon_keymaps.append((km, kmi_save))
        
        # Cmd+Alt+S をオーバーライド（インクリメンタル保存）
        kmi_incremental = km.keymap_items.new(
            'versave.save_incremental',
            type='S',
            value='PRESS',
            oskey=True,  # macOSのCommandキー
            alt=True
        )
        addon_keymaps.append((km, kmi_incremental))
        
        # Cmd+Shift+E でバージョンマネージャーを開く
        kmi_version_manager = km.keymap_items.new(
            'versave.version_manager',
            type='E',
            value='PRESS',
            oskey=True,  # macOSのCommandキー
            shift=True
        )
        addon_keymaps.append((km, kmi_version_manager))

def unregister_keymaps():
    """キーボードショートカットを削除"""
    for km, kmi in addon_keymaps:
        try:
            km.keymap_items.remove(kmi)
        except (KeyError, ReferenceError):
            pass  # Keymap item already removed
    addon_keymaps.clear()

