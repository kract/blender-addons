# -*- coding: utf-8 -*-
import sys
import bpy
from . import preferences


def get_addon_preferences(context):
    """Get addon preferences by searching for LANGSWAP_AddonPreferences instance"""
    # bl_idnameを取得（動的に設定される可能性があるため）
    bl_idname = getattr(preferences.LANGSWAP_AddonPreferences, 'bl_idname', 'langswap')
    
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
                # 言語リストは固定（ja_JPとen_US）なので、languagesプロパティは不要
                self.trans_tooltips = True
                self.trans_interface = True
                self.trans_reports = False
                self.trans_new_dataname = False
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

        # 固定の言語リスト（ja_JPとen_US）
        languages = ["ja_JP", "en_US"]

        # 現在の言語を取得
        current_lang = view.language

        # 現在の言語がリスト内にあるか確認
        if current_lang in languages:
            # 現在の言語がリスト内にある場合、次の言語に切り替え
            current_index = languages.index(current_lang)
            next_index = (current_index + 1) % len(languages)
            next_lang = languages[next_index]
        else:
            # 現在の言語がリスト内にない場合、最初の言語に切り替え
            next_lang = languages[0]

        # 言語切替
        view.language = next_lang

        # 翻訳範囲設定
        view.use_translate_tooltips = prefs.trans_tooltips
        view.use_translate_interface = prefs.trans_interface
        view.use_translate_reports = prefs.trans_reports
        view.use_translate_new_dataname = prefs.trans_new_dataname

        self.report({"INFO"}, f"Switched to {next_lang}")
        return {"FINISHED"}



