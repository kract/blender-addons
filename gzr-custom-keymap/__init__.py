# GZR Custom Keymap (C)2024 KRACT
# 
# ##### BEGIN GPL LICENSE BLOCK #####
# 
# This program is free software: 
# you can redistribute it and/or modify it under the terms of 
# the GNU General Public License as published by the Free Software Foundation, 
# either version 3 of the License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; 
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
# See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along with this program. 
# If not, see <https://www.gnu.org/licenses/>.
#
# ##### END GPL LICENSE BLOCK #####

bl_info = {
    "name": "GZR Custom Keymap",
    "author": "KRACT",
    "version": (1, 0, 0),
    "blender": (4, 2, 0),
    "description": "Custom key maps",
    "warning": "",
    "category": "UI",
}


import bpy
from bpy.props import *
from bpy.types import AddonPreferences
import rna_keymap_ui

class GZR_KEYMAP_AddonPreferences(AddonPreferences):
    bl_idname = __name__

    tab_addon_menu: EnumProperty(
        name="tab",
        description="",
        items=[
            ('KEYMAP', "Keymap", "", "EVENT_A", 0),
            ('LINK', "Link", "", "URL", 1)
        ],
        default='KEYMAP'
    )

    def draw(self, context):
        layout = self.layout
        
        row = layout.row(align=True)
        row.prop(self, "tab_addon_menu", expand=True)

        if self.tab_addon_menu == "KEYMAP":
            box = layout.box()
            col = box.column()
            col.label(text="Keymap List:")

            wm = bpy.context.window_manager
            kc = wm.keyconfigs.user
            old_km_name = ""
            old_id_l = []

            for km_add, kmi_add in addon_keymaps:
                for km_con in kc.keymaps:
                    if km_add.name == km_con.name:
                        km = km_con
                        break

                for kmi_con in km.keymap_items:
                    if kmi_add.idname == kmi_con.idname:
                        if not kmi_con.id in old_id_l:
                            kmi = kmi_con
                            old_id_l.append(kmi_con.id)
                            break

                try:
                    if not km.name == old_km_name:
                        col.label(text=str(km.name), icon="DOT")
                    col.context_pointer_set("keymap", km)
                    rna_keymap_ui.draw_kmi([], kc, km, kmi, col, 0)
                    col.separator()
                    old_km_name = km.name
                except:
                    pass

        if self.tab_addon_menu == "LINK":
            row = layout.row()
            row.label(text="Link:")
            row.operator("wm.url_open", text="Repository").url = "https://github.com/kract/blender-addons/tree/main/gzr-custom-keymap"

classes = (GZR_KEYMAP_AddonPreferences,)

addon_keymaps = []

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon

    # 3D View
    km = kc.keymaps.new(name="3D View", space_type="VIEW_3D")
    if kc:
        # ビューを回転
        kmi = km.keymap_items.new("view3d.rotate", type='LEFTMOUSE', value="PRESS", alt=True)
        addon_keymaps.append((km, kmi))

        # 視点の移動
        kmi = km.keymap_items.new("view3d.move", type='MIDDLEMOUSE', value="PRESS", alt=True)
        addon_keymaps.append((km, kmi))

        # ビューをズーム
        kmi = km.keymap_items.new("view3d.zoom", type='RIGHTMOUSE', value="PRESS", alt=True)
        addon_keymaps.append((km, kmi))

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

    try:
        bpy.app.translations.unregister(__name__)
    except:
        pass

    for (km, kmi) in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()


if __name__ == '__main__':
    register()

