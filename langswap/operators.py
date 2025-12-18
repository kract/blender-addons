# -*- coding: utf-8 -*-
import bpy
from bpy.props import StringProperty


class LANGSWAP_OT_switch_language(bpy.types.Operator):
    """Switch to next language in the list"""
    bl_label = "Switch Language"
    bl_idname = "langswap.switch_language"

    def execute(self, context):
        prefs = context.preferences.addons[__name__.split(".")[0]].preferences
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
        prefs = context.preferences.addons[__name__.split(".")[0]].preferences

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
        prefs = context.preferences.addons[__name__.split(".")[0]].preferences

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
        prefs = context.preferences.addons[__name__.split(".")[0]].preferences

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

