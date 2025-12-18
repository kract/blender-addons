# -*- coding: utf-8 -*-
import sys
import bpy
from . import preferences


def get_addon_preferences(context):
    """Get addon preferences by searching for LANGSWAP_AddonPreferences instance"""
    bl_idname = preferences.LANGSWAP_AddonPreferences.bl_idname
    
    # 方法1: "langswap"を含むアドオン名を直接試す（Blender拡張システム用）
    available_addons = list(context.preferences.addons.keys())
    langswap_addons = [name for name in available_addons if 'langswap' in name.lower()]
    
    for addon_name in langswap_addons:
        try:
            addon_module = context.preferences.addons[addon_name]
            if hasattr(addon_module, 'preferences'):
                prefs = addon_module.preferences
                # preferencesがNoneの場合はスキップ
                if prefs is None:
                    continue
                # 型チェックで確認（最も確実）
                if isinstance(prefs, preferences.LANGSWAP_AddonPreferences):
                    return prefs
                # bl_idnameで確認
                if hasattr(prefs, 'bl_idname') and prefs.bl_idname == bl_idname:
                    return prefs
        except (KeyError, AttributeError, TypeError) as e:
            # デバッグ用: エラーを記録
            continue
    
    # 方法2: __init__.pyモジュールを取得してADDON_NAMEを使用
    try:
        current_module = sys.modules[__name__]
        package_name = current_module.__package__
        if package_name:
            init_module = sys.modules.get(package_name)
            if init_module:
                # ADDON_NAMEを試す
                if hasattr(init_module, 'ADDON_NAME'):
                    addon_name = init_module.ADDON_NAME
                    addon_module = context.preferences.addons.get(addon_name)
                    if addon_module and hasattr(addon_module, 'preferences'):
                        prefs = addon_module.preferences
                        if prefs is not None:
                            return prefs
                # __name__を試す
                if hasattr(init_module, '__name__'):
                    addon_name = init_module.__name__
                    addon_module = context.preferences.addons.get(addon_name)
                    if addon_module and hasattr(addon_module, 'preferences'):
                        prefs = addon_module.preferences
                        if prefs is not None:
                            return prefs
    except (KeyError, AttributeError, TypeError):
        pass
    
    # 方法3: すべてのアドオンをループしてbl_idnameで検索
    for addon_name in context.preferences.addons.keys():
        try:
            addon_module = context.preferences.addons[addon_name]
            if hasattr(addon_module, 'preferences'):
                prefs = addon_module.preferences
                if prefs is not None and hasattr(prefs, 'bl_idname'):
                    if prefs.bl_idname == bl_idname:
                        return prefs
        except (KeyError, AttributeError, TypeError):
            continue
    
    # 方法4: 型チェックで検索（すべてのアドオンを確認）
    for addon_name in context.preferences.addons.keys():
        try:
            addon_module = context.preferences.addons[addon_name]
            if hasattr(addon_module, 'preferences'):
                prefs = addon_module.preferences
                if prefs is not None:
                    # isinstanceで型を確認
                    if isinstance(prefs, preferences.LANGSWAP_AddonPreferences):
                        return prefs
        except (KeyError, AttributeError, TypeError):
            continue
    
    # preferencesがNoneの場合でも、デフォルト値を使用する
    # Blenderの拡張システムでは、preferencesがNoneになることがある
    # この場合、デフォルトの設定を使用する
    if langswap_addons:
        # langswapアドオンが見つかっているが、preferencesがNoneの場合
        # デフォルトの設定オブジェクトを作成して返す
        # これにより、Preferencesパネルを開かなくても動作する
        class DefaultLanguageItem:
            """デフォルトの言語アイテム"""
            def __init__(self, locale):
                self.locale = locale
        
        class DefaultPreferences:
            """デフォルトの設定オブジェクト"""
            def __init__(self):
                # デフォルトの言語リスト（en_USとja_JP）
                self.languages = [
                    DefaultLanguageItem("en_US"),
                    DefaultLanguageItem("ja_JP")
                ]
                self.active_language_index = 0
                self.trans_tooltips = True
                self.trans_interface = True
                self.trans_reports = True
                self.trans_new_dataname = True
                self.bl_idname = bl_idname
        
        return DefaultPreferences()
    
    # それでも見つからない場合はエラー
    raise KeyError(
        f"Addon '{bl_idname}' not found in preferences.addons. "
        f"Total addons: {len(available_addons)}"
    )


class LANGSWAP_OT_switch_language(bpy.types.Operator):
    """Switch to next language in the list"""
    bl_label = "Switch Language"
    bl_idname = "langswap.switch_language"

    def execute(self, context):
        try:
            prefs = get_addon_preferences(context)
        except KeyError as e:
            self.report({"ERROR"}, f"Failed to get addon preferences: {e}")
            return {"CANCELLED"}
        
        if prefs is None:
            self.report({"ERROR"}, "Addon preferences is None. Please reinstall the addon.")
            return {"CANCELLED"}
        
        view = context.preferences.view

        # 言語リストが空の場合は何もしない
        if len(prefs.languages) == 0:
            self.report({"WARNING"}, "No languages configured. Please add languages in preferences.")
            return {"CANCELLED"}

        # 現在の言語を取得
        current_lang = view.language

        # 現在の言語がリスト内にあるか確認
        current_index = -1
        for i, lang_item in enumerate(prefs.languages):
            if lang_item.locale == current_lang:
                current_index = i
                break

        # 次の言語を決定
        if current_index >= 0:
            # 現在の言語がリスト内にある場合、次の言語に切り替え
            next_index = (current_index + 1) % len(prefs.languages)
            next_lang = prefs.languages[next_index].locale
        else:
            # 現在の言語がリスト内にない場合、最初の言語に切り替え
            next_lang = prefs.languages[0].locale

        # 言語切替
        view.language = next_lang

        # 翻訳範囲設定
        view.use_translate_tooltips = prefs.trans_tooltips
        view.use_translate_interface = prefs.trans_interface
        view.use_translate_reports = prefs.trans_reports
        view.use_translate_new_dataname = prefs.trans_new_dataname

        self.report({"INFO"}, f"Switched to {next_lang}")
        return {"FINISHED"}


class LANGSWAP_OT_add_language(bpy.types.Operator):
    """Add a new language to the list"""
    bl_label = "Add Language"
    bl_idname = "langswap.add_language"

    def execute(self, context):
        try:
            prefs = get_addon_preferences(context)
        except KeyError as e:
            self.report({"ERROR"}, f"Failed to get addon preferences: {e}")
            return {"CANCELLED"}
        
        if prefs is None:
            self.report({"ERROR"}, "Addon preferences is None. Please reinstall the addon.")
            return {"CANCELLED"}

        # 最大5言語まで
        if len(prefs.languages) >= 5:
            self.report({"WARNING"}, "Maximum 5 languages allowed.")
            return {"CANCELLED"}

        # 新しい言語アイテムを追加
        new_item = prefs.languages.add()
        new_item.locale = "en_US"  # デフォルト言語

        # アクティブインデックスを更新
        prefs.active_language_index = len(prefs.languages) - 1

        return {"FINISHED"}


class LANGSWAP_OT_remove_language(bpy.types.Operator):
    """Remove selected language from the list"""
    bl_label = "Remove Language"
    bl_idname = "langswap.remove_language"

    def execute(self, context):
        try:
            prefs = get_addon_preferences(context)
        except KeyError as e:
            self.report({"ERROR"}, f"Failed to get addon preferences: {e}")
            return {"CANCELLED"}
        
        if prefs is None:
            self.report({"ERROR"}, "Addon preferences is None. Please reinstall the addon.")
            return {"CANCELLED"}

        if len(prefs.languages) == 0:
            self.report({"WARNING"}, "No languages to remove.")
            return {"CANCELLED"}

        # アクティブな言語を削除
        active_index = prefs.active_language_index
        if active_index >= 0 and active_index < len(prefs.languages):
            prefs.languages.remove(active_index)

            # インデックスを調整
            if prefs.active_language_index >= len(prefs.languages):
                prefs.active_language_index = max(0, len(prefs.languages) - 1)

        return {"FINISHED"}


class LANGSWAP_OT_initialize_languages(bpy.types.Operator):
    """Initialize default languages (English and Japanese)"""
    bl_label = "Initialize Default Languages"
    bl_idname = "langswap.initialize_languages"

    def execute(self, context):
        try:
            prefs = get_addon_preferences(context)
        except KeyError as e:
            self.report({"ERROR"}, f"Failed to get addon preferences: {e}")
            return {"CANCELLED"}
        
        if prefs is None:
            self.report({"ERROR"}, "Addon preferences is None. Please reinstall the addon.")
            return {"CANCELLED"}

        # 既に言語がある場合はクリア
        prefs.languages.clear()

        # デフォルト言語を追加
        lang1 = prefs.languages.add()
        lang1.locale = "en_US"

        lang2 = prefs.languages.add()
        lang2.locale = "ja_JP"

        prefs.active_language_index = 0

        self.report({"INFO"}, "Initialized default languages (en_US, ja_JP)")
        return {"FINISHED"}

