import bpy


# アドオンIDと表示名のマッピング
_ADDON_LABELS = {
    "langswap": "LangSwap",
    "viewpie": "Viewpie",
    "versave": "Versave",
    "viewcam": "Viewcam",
    "nukeshima": "Nukeshima",
}

# 各アドオンのショートカット定義
# (context, key_label, action_label)
_CHEATSHEET = {
    "minamo": [
        ("3D View", "Ctrl + LMB",          "ビュー回転"),
        ("3D View", "Ctrl + MMB",          "パン"),
        ("3D View", "Ctrl + RMB",          "ズーム"),
        ("2D View / Image", "Ctrl + LMB",  "パン"),
        ("2D View / Image", "Ctrl + MMB",  "パン"),
        ("2D View / Image", "Ctrl + RMB",  "ズーム"),
        ("Edit Mode", "Alt + ドラッグ ←",  "頂点モード"),
        ("Edit Mode", "Alt + ドラッグ ↓",  "辺モード"),
        ("Edit Mode", "Alt + ドラッグ →",  "面モード"),
    ],
    "langswap": [
        ("Window", "End",                  "言語切り替え"),
    ],
    "viewpie": [
        ("3D View", "Q",                   "ビューパイメニュー"),
        ("3D View", "Shift + Q",           "拡張ビューパイメニュー"),
    ],
    "versave": [
        ("Window", "Cmd + S",              "保存（初回バージョン付き）"),
        ("Window", "Cmd + Alt + S",        "増分保存"),
        ("Window", "Cmd + Shift + E",      "バージョンマネージャー"),
    ],
    "viewcam": [
        ("3D View", "Cmd + Shift + C",     "ビューをカメラに設定"),
        ("3D View", "Cmd + Shift + Alt + C", "カメラ to ビュー トグル"),
    ],
    "nukeshima": [
        ("Object / Edit", "X",             "スマート削除"),
        ("Object / Edit", "Shift + X",     "削除メニュー"),
    ],
}


def _is_addon_installed(context, addon_id):
    return any(addon_id in name for name in context.preferences.addons.keys())


def _draw_section(layout, title, entries):
    box = layout.box()
    box.label(text=title, icon="KEYINGSET")
    col = box.column(align=True)
    for ctx, key, action in entries:
        row = col.row(align=True)
        row.label(text=ctx)
        row.label(text=key)
        row.label(text=action)


class MINAMO_KEYMAP_PT_cheatsheet(bpy.types.Panel):
    bl_label = "Cheatsheet"
    bl_idname = "MINAMO_KEYMAP_PT_cheatsheet"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Minamo"

    def draw(self, context):
        layout = self.layout

        _draw_section(layout, "Minamo Keymap", _CHEATSHEET["minamo"])

        for addon_id, label in _ADDON_LABELS.items():
            if _is_addon_installed(context, addon_id):
                _draw_section(layout, label, _CHEATSHEET[addon_id])
