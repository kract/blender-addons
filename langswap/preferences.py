# -*- coding: utf-8 -*-
import bpy
from bpy.props import BoolProperty
import rna_keymap_ui


# Addon設定パネル
class LANGSWAP_AddonPreferences(bpy.types.AddonPreferences):
    bl_idname = "langswap"

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
    # 報告（非表示、常にFalse）
    trans_reports: BoolProperty(
        default=False,
    )
    # 新規データ（非表示、常にFalse）
    trans_new_dataname: BoolProperty(
        default=False,
    )

    def draw(self, context):
        layout = self.layout

        # 現在の言語表示
        view = context.preferences.view
        current_lang = view.language
        box = layout.box()
        box.label(text=f"Current Language: {current_lang}")

        # 言語情報（固定：ja_JPとen_US）
        box = layout.box()
        box.label(text="Languages: ja_JP, en_US", icon="WORLD")

        # 翻訳設定
        box = layout.box()
        box.label(text="Translation Settings:")
        row = box.row()
        row.alignment = "EXPAND"
        row.prop(self, "trans_tooltips")
        row.prop(self, "trans_interface")

        # キーマップ設定
        box = layout.box()
        box.label(text="Keymap:")
        
        # 現在のキーマップを表示・編集
        from . import keymap
        wm = context.window_manager
        kc = wm.keyconfigs.addon
        
        if kc and keymap.addon_keymaps:
            for km, kmi_addon in keymap.addon_keymaps:
                if km and kmi_addon:
                    # ユーザーキーマップから実際のキーマップアイテムを取得
                    km_user = None
                    kmi_user = None
                    
                    for km_check in kc.keymaps:
                        if km_check.name == km.name:
                            km_user = km_check
                            break
                    
                    if km_user:
                        for kmi_check in km_user.keymap_items:
                            if kmi_check.idname == kmi_addon.idname:
                                kmi_user = kmi_check
                                break
                    
                    if km_user and kmi_user:
                        # rna_keymap_uiを使用してキーマップを表示・編集可能にする
                        col = box.column()
                        col.context_pointer_set("keymap", km_user)
                        rna_keymap_ui.draw_kmi([], kc, km_user, kmi_user, col, 0)
                    else:
                        box.label(text="Keymap not found in user keymap", icon="ERROR")
                    break
        else:
            box.label(text="Keymap not found", icon="ERROR")

