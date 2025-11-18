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
        default=False
    )
    show_view2d: BoolProperty(
        name="Show View2D",
        description="Show View2D keymap items",
        default=False
    )
    show_image: BoolProperty(
        name="Show Image",
        description="Show Image Editor keymap items",
        default=False
    )
    show_mesh: BoolProperty(
        name="Show Mesh",
        description="Show Mesh keymap items",
        default=False
    )
    show_object_mode: BoolProperty(
        name="Show Object Mode",
        description="Show Object Mode keymap items",
        default=False
    )
    show_armature: BoolProperty(
        name="Show Armature",
        description="Show Armature keymap items",
        default=False
    )
    show_pose: BoolProperty(
        name="Show Pose",
        description="Show Pose keymap items",
        default=False
    )
    show_animation: BoolProperty(
        name="Show Animation",
        description="Show Animation keymap items",
        default=False
    )
    show_graph_editor: BoolProperty(
        name="Show Graph Editor",
        description="Show Graph Editor keymap items",
        default=False
    )
    show_uv_editor: BoolProperty(
        name="Show UV Editor",
        description="Show UV Editor keymap items",
        default=False
    )
    show_node_editor: BoolProperty(
        name="Show Node Editor",
        description="Show Node Editor keymap items",
        default=False
    )
    show_sequencer: BoolProperty(
        name="Show Sequencer",
        description="Show Sequencer keymap items",
        default=False
    )
    show_timeline: BoolProperty(
        name="Show Timeline",
        description="Show Timeline keymap items",
        default=False
    )
    show_grease_pencil: BoolProperty(
        name="Show Grease Pencil",
        description="Show Grease Pencil keymap items",
        default=False
    )
    show_sculpt: BoolProperty(
        name="Show Sculpt",
        description="Show Sculpt keymap items",
        default=False
    )
    show_weight_paint: BoolProperty(
        name="Show Weight Paint",
        description="Show Weight Paint keymap items",
        default=False
    )
    show_outliner: BoolProperty(
        name="Show Outliner",
        description="Show Outliner keymap items",
        default=False
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
                elif km_name == "Object Mode":
                    expand_prop = self.show_object_mode
                    prop_name = "show_object_mode"
                elif km_name == "Armature":
                    expand_prop = self.show_armature
                    prop_name = "show_armature"
                elif km_name == "Pose":
                    expand_prop = self.show_pose
                    prop_name = "show_pose"
                elif km_name == "Animation":
                    expand_prop = self.show_animation
                    prop_name = "show_animation"
                elif km_name == "Graph Editor":
                    expand_prop = self.show_graph_editor
                    prop_name = "show_graph_editor"
                elif km_name == "UV Editor":
                    expand_prop = self.show_uv_editor
                    prop_name = "show_uv_editor"
                elif km_name == "Node Editor":
                    expand_prop = self.show_node_editor
                    prop_name = "show_node_editor"
                elif km_name == "Sequencer":
                    expand_prop = self.show_sequencer
                    prop_name = "show_sequencer"
                elif km_name == "Timeline":
                    expand_prop = self.show_timeline
                    prop_name = "show_timeline"
                elif km_name == "Grease Pencil":
                    expand_prop = self.show_grease_pencil
                    prop_name = "show_grease_pencil"
                elif km_name == "Sculpt":
                    expand_prop = self.show_sculpt
                    prop_name = "show_sculpt"
                elif km_name == "Weight Paint":
                    expand_prop = self.show_weight_paint
                    prop_name = "show_weight_paint"
                elif km_name == "Outliner":
                    expand_prop = self.show_outliner
                    prop_name = "show_outliner"
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

    # Zキーエントリ（SAMPLE_KEYMAP.pyから移植）
    # Shading pie menu
    kmi = km.keymap_items.new("wm.call_menu_pie", type='Z', value="PRESS")
    kmi.properties.name = 'VIEW3D_MT_shading_pie'
    addon_keymaps.append((km, kmi))

    # Toggle shading (Wireframe)
    kmi = km.keymap_items.new("view3d.toggle_shading", type='Z', value="PRESS", shift=True)
    kmi.properties.type = 'WIREFRAME'
    addon_keymaps.append((km, kmi))

    # Toggle X-ray
    kmi = km.keymap_items.new("view3d.toggle_xray", type='Z', value="PRESS", alt=True)
    addon_keymaps.append((km, kmi))

    # Toggle overlays
    kmi = km.keymap_items.new("wm.context_toggle", type='Z', value="PRESS", shift=True, alt=True)
    kmi.properties.data_path = 'space_data.overlay.show_overlays'
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

    # Object Mode
    km = kc.keymaps.new(name="Object Mode", space_type="EMPTY")
    
    # Transform translate
    kmi = km.keymap_items.new("transform.translate", type='Z', value="PRESS")
    addon_keymaps.append((km, kmi))

    # Location clear
    kmi = km.keymap_items.new("object.location_clear", type='Z', value="PRESS", ctrl=True, alt=True)
    kmi.properties.clear_delta = False
    addon_keymaps.append((km, kmi))

    # Armature
    km = kc.keymaps.new(name="Armature", space_type="EMPTY")
    
    # Transform translate
    kmi = km.keymap_items.new("transform.translate", type='Z', value="PRESS")
    addon_keymaps.append((km, kmi))

    # Pose
    km = kc.keymaps.new(name="Pose", space_type="EMPTY")
    
    # Location clear
    kmi = km.keymap_items.new("pose.loc_clear", type='Z', value="PRESS", ctrl=True, alt=True)
    addon_keymaps.append((km, kmi))

    # Animation
    km = kc.keymaps.new(name="Animation", space_type="EMPTY")
    
    # Transform transform (TIME_TRANSLATE)
    kmi = km.keymap_items.new("transform.transform", type='Z', value="PRESS")
    kmi.properties.mode = 'TIME_TRANSLATE'
    addon_keymaps.append((km, kmi))

    # Graph Editor
    km = kc.keymaps.new(name="Graph Editor", space_type="GRAPH_EDITOR")
    
    # Transform translate
    kmi = km.keymap_items.new("transform.translate", type='Z', value="PRESS")
    addon_keymaps.append((km, kmi))

    # UV Editor
    km = kc.keymaps.new(name="UV Editor", space_type="EMPTY")
    
    # Transform translate
    kmi = km.keymap_items.new("transform.translate", type='Z', value="PRESS")
    addon_keymaps.append((km, kmi))

    # Node Editor
    km = kc.keymaps.new(name="Node Editor", space_type="NODE_EDITOR")
    
    # Render changed
    kmi = km.keymap_items.new("node.render_changed", type='Z', value="PRESS")
    addon_keymaps.append((km, kmi))

    # Translate attach
    kmi = km.keymap_items.new("node.translate_attach", type='Z', value="PRESS")
    addon_keymaps.append((km, kmi))

    # Transform translate
    kmi = km.keymap_items.new("transform.translate", type='Z', value="PRESS")
    kmi.properties.view2d_edge_pan = True
    addon_keymaps.append((km, kmi))

    # Toggle overlays
    kmi = km.keymap_items.new("wm.context_toggle", type='Z', value="PRESS", shift=True, alt=True)
    kmi.properties.data_path = 'space_data.overlay.show_overlays'
    addon_keymaps.append((km, kmi))

    # Sequencer
    km = kc.keymaps.new(name="Sequencer", space_type="SEQUENCE_EDITOR")
    
    # Transform seq slide
    kmi = km.keymap_items.new("transform.seq_slide", type='Z', value="PRESS")
    kmi.properties.view2d_edge_pan = True
    addon_keymaps.append((km, kmi))

    # Toggle overlays
    kmi = km.keymap_items.new("wm.context_toggle", type='Z', value="PRESS", shift=True, alt=True)
    kmi.properties.data_path = 'space_data.show_overlays'
    addon_keymaps.append((km, kmi))

    # Replace source preserve timing
    kmi = km.keymap_items.new("sequencer.replace_source_preserve_timing", type='Z', value="PRESS", shift=True, ctrl=True, alt=True)
    addon_keymaps.append((km, kmi))

    # Timeline
    km = kc.keymaps.new(name="Timeline", space_type="DOPESHEET_EDITOR")
    
    # Marker move
    kmi = km.keymap_items.new("marker.move", type='Z', value="PRESS")
    addon_keymaps.append((km, kmi))

    # Grease Pencil
    # Note: brush.asset_activateエントリは削除（アセットが存在しない場合にエラーが発生するため）
    # km = kc.keymaps.new(name="Grease Pencil", space_type="EMPTY")
    # kmi = km.keymap_items.new("brush.asset_activate", type='Z', value="PRESS", repeat=True)
    # kmi.properties.asset_library_type = 'CUSTOM'
    # kmi.properties.asset_library_identifier = 'User Library'
    # addon_keymaps.append((km, kmi))

    # Sculpt
    # Note: brush.asset_activateエントリは削除（アセットが存在しない場合にエラーが発生するため）
    # km = kc.keymaps.new(name="Sculpt", space_type="EMPTY")
    # kmi = km.keymap_items.new("brush.asset_activate", type='Z', value="PRESS", repeat=True)
    # kmi.properties.asset_library_type = 'ESSENTIALS'
    # kmi.properties.asset_library_identifier = ''
    # addon_keymaps.append((km, kmi))

    # Weight Paint
    km = kc.keymaps.new(name="Weight Paint", space_type="EMPTY")
    
    # Toggle overlays
    kmi = km.keymap_items.new("wm.context_toggle", type='Z', value="PRESS", shift=True, alt=True)
    kmi.properties.data_path = 'space_data.overlay.show_overlays'
    addon_keymaps.append((km, kmi))

    # Outliner
    km = kc.keymaps.new(name="Outliner", space_type="OUTLINER")
    
    # Item drag drop
    kmi = km.keymap_items.new("outliner.item_drag_drop", type='Z', value="CLICK")
    addon_keymaps.append((km, kmi))

    # Transform Modal Map
    # Note: AXIS_*エントリは削除（動作しないため）
    # PLANE_ZとTRANSLATEも削除（Transform Modal Mapは通常のキーマップアイテムとして登録できない可能性があるため）


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

