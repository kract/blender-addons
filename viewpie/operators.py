import bpy

# Translation dictionary
translations = {
    "en_US": {
        "Right": "Right",
        "Left": "Left", 
        "Bottom": "Bottom",
        "Top": "Top",
        "Back": "Back",
        "Front": "Front",
        "Camera": "Camera",
        "Perspective/Ortho": "Perspective/Ortho",
        "View Selected": "View Selected",
        "View All": "View All",
        "Center Cursor": "Center Cursor",
        "Basic Views": "Basic Views",
        "Perspective": "Perspective",
        "Orthographic": "Orthographic"
    },
    "ja_JP": {
        "Right": "右面",
        "Left": "左面",
        "Bottom": "底面", 
        "Top": "上面",
        "Back": "背面",
        "Front": "前面",
        "Camera": "カメラ",
        "Perspective/Ortho": "透視/平行",
        "View Selected": "選択オブジェクト表示",
        "View All": "全体表示",
        "Center Cursor": "カーソル中心",
        "Basic Views": "基本ビュー",
        "Perspective": "透視",
        "Orthographic": "平行"
    }
}

def get_translation(text):
    """Get translated text based on current language and UI translation setting"""
    prefs = bpy.context.preferences.view
    
    # Check if translation is enabled in UI
    if not prefs.use_translate_interface:
        # If translation is disabled, always use English
        return translations.get('en_US', {}).get(text, text)
    
    # If translation is enabled, check the system language
    lang = prefs.language
    
    # Map Blender language codes to our translation keys
    lang_map = {
        'ja_JP': 'ja_JP',
        'DEFAULT': 'en_US'
    }
    
    # Get the appropriate language key
    lang_key = lang_map.get(lang, 'en_US')
    
    # Return translated text or original if not found
    return translations.get(lang_key, {}).get(text, text)

class VIEWPIE_OT_set_view(bpy.types.Operator):
    """Set 3D viewport to specific view"""
    bl_idname = "viewpie.set_view"
    bl_label = "Set View"
    
    view_type: bpy.props.StringProperty(name="View Type")
    
    @classmethod
    def poll(cls, context):
        return context.area and context.area.type == 'VIEW_3D'
    
    def execute(self, context):
        view_3d = context.space_data
        region_3d = context.region_data
        
        view_mapping = {
            'FRONT': 'FRONT',
            'BACK': 'BACK',
            'LEFT': 'LEFT',
            'RIGHT': 'RIGHT',
            'TOP': 'TOP',
            'BOTTOM': 'BOTTOM',
            'CAMERA': 'CAMERA'
        }
        
        if self.view_type in view_mapping:
            if self.view_type == 'CAMERA':
                bpy.ops.view3d.view_camera()
            else:
                bpy.ops.view3d.view_axis(type=view_mapping[self.view_type])
        elif self.view_type == 'PERSPECTIVE':
            region_3d.view_perspective = 'PERSP'
        elif self.view_type == 'ORTHOGRAPHIC':
            region_3d.view_perspective = 'ORTHO'
        elif self.view_type == 'SELECTED':
            bpy.ops.view3d.view_selected()
        elif self.view_type == 'ALL':
            bpy.ops.view3d.view_all()
        elif self.view_type == 'CENTER':
            bpy.ops.view3d.view_center_cursor()
        
        return {'FINISHED'}

class VIEWPIE_OT_toggle_projection(bpy.types.Operator):
    """Toggle between perspective and orthographic projection"""
    bl_idname = "viewpie.toggle_projection"
    bl_label = "Toggle Projection"
    
    @classmethod
    def poll(cls, context):
        return context.area and context.area.type == 'VIEW_3D'
    
    def execute(self, context):
        region_3d = context.region_data
        if region_3d.view_perspective == 'PERSP':
            region_3d.view_perspective = 'ORTHO'
            self.report({'INFO'}, "Switched to Orthographic")
        else:
            region_3d.view_perspective = 'PERSP'
            self.report({'INFO'}, "Switched to Perspective")
        
        return {'FINISHED'}

class VIEWPIE_OT_call_pie_menu(bpy.types.Operator):
    """Call Viewpie pie menu"""
    bl_idname = "viewpie.call_pie_menu"
    bl_label = "Viewpie Pie Menu"
    
    extended: bpy.props.BoolProperty(
        name="Extended Menu",
        description="Show extended pie menu with additional options",
        default=False
    )
    
    @classmethod
    def poll(cls, context):
        return context.area and context.area.type == 'VIEW_3D'
    
    def execute(self, context):
        if self.extended:
            bpy.ops.wm.call_menu_pie(name="VIEWPIE_MT_pie_menu_extended")
        else:
            bpy.ops.wm.call_menu_pie(name="VIEWPIE_MT_pie_menu")
        return {'FINISHED'}

