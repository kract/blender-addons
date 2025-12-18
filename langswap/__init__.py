# -*- coding: utf-8 -*-
bl_info = {
    "name": "LangSwap",
    "author": "KRACT Studio",
    "version": (1, 0, 0),
    "blender": (4, 2, 0),
    "location": "",
    "description": "Quickly switch between multiple languages with a single key press",
    "warning": "",
    "doc_url": "",
    "category": "System",
}

if "bpy" in locals():
    import importlib
    importlib.reload(translations)
    importlib.reload(preferences)
    importlib.reload(operators)
    importlib.reload(keymap)
else:
    from . import translations
    from . import preferences
    from . import operators
    from . import keymap

import bpy

# アドオン名をエクスポート（他のモジュールから使用可能にする）
ADDON_NAME = __name__

classes = (
    preferences.LANGSWAP_AddonPreferences,
    operators.LANGSWAP_OT_switch_language,
)


def register():
    """Register addon"""
    # bl_idnameを実際のアドオン名に設定（Preferencesパネルを正しく表示するため）
    preferences.LANGSWAP_AddonPreferences.bl_idname = __name__
    
    # クラス登録
    for cls in classes:
        try:
            bpy.utils.register_class(cls)
        except ValueError:
            # 既に登録されている場合はスキップ
            pass

    # キーマップ登録
    keymap.register_keymaps()

    # 翻訳辞書の登録
    try:
        bpy.app.translations.register(__name__, translations.translation_dict)
    except ValueError:
        # 既に登録済みの場合は無視
        pass


def unregister():
    """Unregister addon"""
    # キーマップ削除
    keymap.unregister_keymaps()

    # クラス削除
    for cls in reversed(classes):
        try:
            bpy.utils.unregister_class(cls)
        except (RuntimeError, ValueError):
            pass  # Already unregistered

    # 翻訳辞書の登録解除
    try:
        bpy.app.translations.unregister(__name__)
    except ValueError:
        pass  # Not registered


if __name__ == "__main__":
    register()

