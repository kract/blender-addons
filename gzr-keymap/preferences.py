import bpy
from bpy.props import EnumProperty, BoolProperty
from bpy.types import AddonPreferences
import rna_keymap_ui

# グローバル変数（keymap.pyから参照される）
addon_keymaps = []

class GZR_KEYMAP_AddonPreferences(AddonPreferences):
    bl_idname = "gzr_keymap"  # アドオン名（ディレクトリ名からハイフンをアンダースコアに変換）

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

