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

classes = (
    preferences.LANGSWAP_LanguageItem,
    preferences.LANGSWAP_AddonPreferences,
    preferences.LANGSWAP_UL_language_list,
    operators.LANGSWAP_OT_switch_language,
    operators.LANGSWAP_OT_add_language,
    operators.LANGSWAP_OT_remove_language,
    operators.LANGSWAP_OT_initialize_languages,
)


def register():
    """Register addon"""
    # クラス登録
    for cls in classes:
        bpy.utils.register_class(cls)

    # キーマップ登録
    keymap.register_keymaps()

    # 翻訳辞書の登録
    bpy.app.translations.register(__name__, translations.translation_dict)


def unregister():
    """Unregister addon"""
    # キーマップ削除
    keymap.unregister_keymaps()

    # クラス削除
    for cls in reversed(classes):
        try:
            bpy.utils.unregister_class(cls)
        except RuntimeError:
            pass  # Already unregistered

    # 翻訳辞書の登録解除
    bpy.app.translations.unregister(__name__)


if __name__ == "__main__":
    register()

