bl_info = {
    "name": "GZR Keymap",
    "author": "KRACT",
    "version": (1, 0, 0),
    "blender": (4, 2, 0),
    "description": "Custom keymap for viewport navigation",
    "category": "UI",
}

import bpy
from bpy.props import EnumProperty, BoolProperty
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

    # Accordion expand states for each keymap section
    show_3d_view: BoolProperty(
        name="Show 3D View",
        description="Show 3D View keymap items",
        default=True
    )
    show_view2d: BoolProperty(
        name="Show View2D",
        description="Show View2D keymap items",
        default=True
    )
    show_image: BoolProperty(
        name="Show Image",
        description="Show Image Editor keymap items",
        default=True
    )
    show_mesh: BoolProperty(
        name="Show Mesh",
        description="Show Mesh keymap items",
        default=True
    )

    def draw(self, context):
        layout = self.layout

        row = layout.row(align=True)
        row.prop(self, "tab_addon_menu", expand=True)

        if self.tab_addon_menu == "KEYMAP":
            wm = bpy.context.window_manager
            kc = wm.keyconfigs.user

            # Group keymap items by keymap name
            keymap_groups = {}
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
                    km_name = km.name
                    if km_name not in keymap_groups:
                        keymap_groups[km_name] = []
                    keymap_groups[km_name].append((km, kmi))
                except:
                    pass

            # Draw each keymap section in an accordion
            for km_name, km_items in keymap_groups.items():
                # Get the expand property based on keymap name
                if km_name == "3D View":
                    expand_prop = self.show_3d_view
                    prop_name = "show_3d_view"
                elif km_name == "View2D":
                    expand_prop = self.show_view2d
                    prop_name = "show_view2d"
                elif km_name == "Image":
                    expand_prop = self.show_image
                    prop_name = "show_image"
                elif km_name == "Mesh":
                    expand_prop = self.show_mesh
                    prop_name = "show_mesh"
                else:
                    expand_prop = True
                    prop_name = None

                # Create accordion
                if prop_name:
                    # Accordion header with toggle
                    box = layout.box()
                    col = box.column()
                    row_header = col.row()
                    row_header.alignment = 'LEFT'
                    row_header.prop(self, prop_name, text=km_name, icon="TRIA_DOWN" if expand_prop else "TRIA_RIGHT", emboss=False)
                    
                    # Draw keymap items if expanded
                    if expand_prop:
                        col_inner = col.column()
                        for km, kmi in km_items:
                            col_inner.context_pointer_set("keymap", km)
                            rna_keymap_ui.draw_kmi([], kc, km, kmi, col_inner, 0)
                            col_inner.separator()
                else:
                    # Fallback for unknown keymaps
                    box = layout.box()
                    col = box.column()
                    col.label(text=km_name, icon="DOT")
                    for km, kmi in km_items:
                        col.context_pointer_set("keymap", km)
                        rna_keymap_ui.draw_kmi([], kc, km, kmi, col, 0)
                        col.separator()


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
    kmi = km.keymap_items.new("view3d.rotate", type='LEFTMOUSE', value="PRESS", shift=True)
    addon_keymaps.append((km, kmi))

    # 視点の移動
    kmi = km.keymap_items.new("view3d.move", type='MIDDLEMOUSE', value="PRESS", shift=True)
    addon_keymaps.append((km, kmi))

    # ビューをズーム
    kmi = km.keymap_items.new("view3d.zoom", type='RIGHTMOUSE', value="PRESS", shift=True)
    addon_keymaps.append((km, kmi))

    # 2D View
    km = kc.keymaps.new(name="View2D", space_type="EMPTY")
    
    # 視点の移動
    kmi = km.keymap_items.new("view2d.pan", type='LEFTMOUSE', value="PRESS", shift=True)
    addon_keymaps.append((km, kmi))

    # 視点の移動
    kmi = km.keymap_items.new("view2d.pan", type='MIDDLEMOUSE', value="PRESS", shift=True)
    addon_keymaps.append((km, kmi))

    # 2Dビューズーム
    kmi = km.keymap_items.new("view2d.zoom", type='RIGHTMOUSE', value="PRESS", shift=True)
    addon_keymaps.append((km, kmi))

    # Image Editor
    km = kc.keymaps.new(name="Image", space_type="IMAGE_EDITOR")
    
    # 視点の移動
    kmi = km.keymap_items.new("image.view_pan", type='LEFTMOUSE', value="PRESS", shift=True)
    addon_keymaps.append((km, kmi))

    # 視点の移動
    kmi = km.keymap_items.new("image.view_pan", type='MIDDLEMOUSE', value="PRESS", shift=True)
    addon_keymaps.append((km, kmi))

    # 2Dビューズーム
    kmi = km.keymap_items.new("image.view_zoom", type='RIGHTMOUSE', value="PRESS", shift=True)
    addon_keymaps.append((km, kmi))

    # Mesh (Edit Mode)
    km = kc.keymaps.new(name="Mesh", space_type="EMPTY")
    
    # 選択モード切り替え（頂点モード）- Alt + 左ドラッグ（左方向）
    kmi = km.keymap_items.new("mesh.select_mode", type='LEFTMOUSE', value="CLICK_DRAG", alt=True, direction='WEST')
    kmi.properties.type = 'VERT'
    addon_keymaps.append((km, kmi))

    # 選択モード切り替え（辺モード）- Alt + 左ドラッグ（下方向）
    kmi = km.keymap_items.new("mesh.select_mode", type='LEFTMOUSE', value="CLICK_DRAG", alt=True, direction='SOUTH')
    kmi.properties.type = 'EDGE'
    addon_keymaps.append((km, kmi))

    # 選択モード切り替え（面モード）- Alt + 左ドラッグ（右方向）
    kmi = km.keymap_items.new("mesh.select_mode", type='LEFTMOUSE', value="CLICK_DRAG", alt=True, direction='EAST')
    kmi.properties.type = 'FACE'
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

