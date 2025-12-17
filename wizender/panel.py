import bpy

class WIZENDER_PT_output_panel(bpy.types.Panel):
    bl_label = "Wizender"
    bl_idname = "WIZENDER_PT_output_panel"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "output"
    bl_parent_id = "RENDER_PT_output"

    def draw(self, context):
        layout = self.layout
        
        # 現在の設定表示
        addon_prefs = context.preferences.addons["wizender"].preferences
        
        box = layout.box()
        box.label(text="Current Global Settings", icon='INFO')
        
        row = box.row()
        row.label(text="Output Path:")
        row.label(text=addon_prefs.output_path)
        
        row = box.row()
        row.label(text="Format:")
        row.label(text=addon_prefs.file_format)
        
        row = box.row()
        row.label(text="Color Mode:")
        row.label(text=addon_prefs.color_mode)
        
        row = box.row()
        row.label(text="Color Depth:")
        row.label(text=addon_prefs.color_depth)
        
        layout.separator()
        
        # 実行ボタン
        layout.operator("wizender.set_settings", icon='RENDER_ANIMATION', text="Apply Wizender Settings")
        
        layout.separator()
        
        # 設定変更案内
        box = layout.box()
        box.label(text="To change settings:", icon='SETTINGS')
        box.label(text="Edit > Preferences > Add-ons > Wizender")

