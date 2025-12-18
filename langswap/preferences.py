# -*- coding: utf-8 -*-
import bpy
import re
from bpy.props import (
    BoolProperty,
    EnumProperty,
    CollectionProperty,
    StringProperty,
    IntProperty,
)
from bpy.types import PropertyGroup


# 対応言語をリストアップ
def get_languages(self, context):
    """Get available languages from Blender"""
    try:
        if not hasattr(bpy.app, 'translations') or not hasattr(bpy.app.translations, 'locales'):
            # フォールバック: デフォルトの言語リスト
            return [
                ("en_US", "English (en_US)", ""),
                ("ja_JP", "日本語 (ja_JP)", ""),
            ]
        
        if bpy.app.version >= (4, 5, 0) and bpy.app.version <= (4, 5, 1):
            languages = []
            for entry in bpy.app.translations.locales:
                label = entry
                match = re.search(r"Locale code:\s*([\w@]+)", label)
                if match:
                    locale_code = match.group(1)
                    languages.append((locale_code, locale_code, ""))
            return languages if languages else [("en_US", "English (en_US)", "")]
        else:
            locales = bpy.app.translations.locales
            if locales:
                return [(locale, locale, "") for locale in locales]
            else:
                return [("en_US", "English (en_US)", "")]
    except (AttributeError, TypeError):
        # エラーが発生した場合はデフォルトの言語リストを返す
        return [
            ("en_US", "English (en_US)", ""),
            ("ja_JP", "日本語 (ja_JP)", ""),
        ]


# 言語プロパティグループ
class LANGSWAP_LanguageItem(PropertyGroup):
    """Language item for collection"""
    locale: StringProperty(
        name="Language",
        description="Select language locale",
        default="en_US",
    )


# Addon設定パネル
class LANGSWAP_AddonPreferences(bpy.types.AddonPreferences):
    bl_idname = "langswap"

    # 言語リスト（動的）
    languages: CollectionProperty(
        type=LANGSWAP_LanguageItem,
        name="Languages",
        description="List of languages to switch between",
    )

    # アクティブな言語インデックス
    active_language_index: IntProperty(
        name="Active Language Index",
        description="Index of currently active language",
        default=0,
        min=0,
    )

    # ツールチップ
    trans_tooltips: BoolProperty(
        default=True,
        name="Tooltips",
        description="Translate tooltips",
    )
    # インターフェイス
    trans_interface: BoolProperty(
        default=True,
        name="Interface",
        description="Translate interface",
    )
    # 報告
    trans_reports: BoolProperty(
        default=True,
        name="Reports",
        description="Translate reports",
    )
    # 新規データ
    trans_new_dataname: BoolProperty(
        default=True,
        name="New Data",
        description="Translate new data names",
    )

    def draw(self, context):
        layout = self.layout

        # 現在の言語表示
        view = context.preferences.view
        current_lang = view.language
        box = layout.box()
        box.label(text=f"Current Language: {current_lang}")

        # 言語リスト
        box = layout.box()
        box.label(text="Languages:")
        row = box.row()
        col = row.column()
        col.template_list(
            "LANGSWAP_UL_language_list",
            "",
            self,
            "languages",
            self,
            "active_language_index",
            rows=3,
        )

        # 追加/削除ボタン
        col = row.column()
        col.operator("langswap.add_language", icon="ADD", text="")
        col.operator("langswap.remove_language", icon="REMOVE", text="")

        # 初期化チェック（言語リストが空の場合）
        if len(self.languages) == 0:
            box = layout.box()
            box.label(text="No languages configured.", icon="INFO")
            box.operator("langswap.initialize_languages", text="Initialize Default Languages")

        # 翻訳設定
        box = layout.box()
        box.label(text="Translation Settings:")
        row = box.row()
        row.alignment = "EXPAND"
        row.prop(self, "trans_tooltips")
        row.prop(self, "trans_interface")
        row.prop(self, "trans_reports")
        row.prop(self, "trans_new_dataname")

        layout.label(
            text="Important: `Keymap > Window > Switch Language` to change keymap."
        )


# UIリスト用のクラス
class LANGSWAP_UL_language_list(bpy.types.UIList):
    """UI list for language items"""
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname):
        # 利用可能な言語リストを取得
        languages = get_languages(None, context)
        
        # 現在の値を表示
        current_value = item.locale
        # 言語リストから現在の値に対応する表示名を取得
        display_name = current_value
        for lang_code, lang_name, _ in languages:
            if lang_code == current_value:
                display_name = lang_name
                break
        
        if self.layout_type in {"DEFAULT", "COMPACT"}:
            # 言語を直接テキスト入力で設定
            row = layout.row(align=True)
            row.prop(item, "locale", text="", icon="WORLD")
        elif self.layout_type in {"GRID"}:
            layout.alignment = "CENTER"
            layout.label(text=display_name, icon="WORLD")

