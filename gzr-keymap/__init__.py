bl_info = {
    "name": "GZR Keymap",
    "author": "KRACT",
    "version": (1, 0, 0),
    "blender": (4, 2, 0),
    "description": "Custom keymap for viewport navigation",
    "category": "UI",
}

import bpy
from bpy.props import EnumProperty
from bpy.types import AddonPreferences
import rna_keymap_ui

addon_keymaps = []


class GZR_KEYMAP_AddonPreferences(AddonPreferences):
    bl_idname = __name__

    tab_addon_menu: EnumProperty(
        name="tab",
        description="",
        items=[
            ('KEYMAP', "Keymap", "", "EVENT_A", 0),
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


classes = (GZR_KEYMAP_AddonPreferences,)


def register():
    """Register addon"""
    for cls in classes:
        bpy.utils.register_class(cls)

    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon

    if not kc:
        return

    # 3D View
    km = kc.keymaps.new(name="3D View", space_type="VIEW_3D")
    
    # ビューを回転
    kmi = km.keymap_items.new("view3d.rotate", type='LEFTMOUSE', value="PRESS", alt=True)
    addon_keymaps.append((km, kmi))

    # 視点の移動
    kmi = km.keymap_items.new("view3d.move", type='MIDDLEMOUSE', value="PRESS", alt=True)
    addon_keymaps.append((km, kmi))

    # ビューをズーム
    kmi = km.keymap_items.new("view3d.zoom", type='RIGHTMOUSE', value="PRESS", alt=True)
    addon_keymaps.append((km, kmi))

    # 2D View
    km = kc.keymaps.new(name="View2D", space_type="EMPTY")
    
    # 視点の移動
    kmi = km.keymap_items.new("view2d.pan", type='LEFTMOUSE', value="PRESS", alt=True)
    addon_keymaps.append((km, kmi))

    # 視点の移動
    kmi = km.keymap_items.new("view2d.pan", type='MIDDLEMOUSE', value="PRESS", alt=True)
    addon_keymaps.append((km, kmi))

    # 2Dビューズーム
    kmi = km.keymap_items.new("view2d.zoom", type='RIGHTMOUSE', value="PRESS", alt=True)
    addon_keymaps.append((km, kmi))

    # Image Editor
    km = kc.keymaps.new(name="Image", space_type="IMAGE_EDITOR")
    
    # 視点の移動
    kmi = km.keymap_items.new("image.view_pan", type='LEFTMOUSE', value="PRESS", alt=True)
    addon_keymaps.append((km, kmi))

    # 視点の移動
    kmi = km.keymap_items.new("image.view_pan", type='MIDDLEMOUSE', value="PRESS", alt=True)
    addon_keymaps.append((km, kmi))

    # 2Dビューズーム
    kmi = km.keymap_items.new("image.view_zoom", type='RIGHTMOUSE', value="PRESS", alt=True)
    addon_keymaps.append((km, kmi))


def unregister():
    """Unregister addon"""
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

    for (km, kmi) in addon_keymaps:
        try:
            km.keymap_items.remove(kmi)
        except (KeyError, ReferenceError):
            pass  # Keymap item already removed
    addon_keymaps.clear()


if __name__ == '__main__':
    register()

