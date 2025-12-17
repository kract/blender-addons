import bpy
from bpy.props import StringProperty, EnumProperty
from bpy.types import AddonPreferences

# アドオンPreferences設定クラス
class WIZENDER_AddonPreferences(AddonPreferences):
    bl_idname = "wizender"
    # 出力パス設定
    output_path: StringProperty(
        name="Output Path",
        description="Render output path (Default: //render/{project_name}/{project_name}_####)",
        default="//render/{project_name}/{project_name}_####",
        subtype='DIR_PATH'
    )
    
    # ファイルフォーマット設定
    file_format: EnumProperty(
        name="File Format",
        description="Output file format",
        items=[
            ('OPEN_EXR', 'OpenEXR', 'OpenEXR format (Default)'),
            ('PNG', 'PNG', 'PNG format'),
            ('JPEG', 'JPEG', 'JPEG format'),
            ('TIFF', 'TIFF', 'TIFF format'),
        ],
        default='OPEN_EXR'
    )
    
    # カラーモード設定
    color_mode: EnumProperty(
        name="Color Mode",
        description="Color mode setting",
        items=[
            ('RGBA', 'RGBA', 'RGBA (with alpha channel)'),
            ('RGB', 'RGB', 'RGB (color only)'),
            ('BW', 'BW', 'Grayscale'),
        ],
        default='RGBA'
    )
    
    # カラー深度設定
    color_depth: EnumProperty(
        name="Color Depth",
        description="Color depth setting",
        items=[
            ('32', '32-bit Float', '32-bit floating point (Full)'),
            ('16', '16-bit Half Float', '16-bit half precision floating point'),
            ('8', '8-bit', '8-bit integer'),
        ],
        default='32'
    )
    
    def draw(self, context):
        layout = self.layout
        
        # 設定セクション
        box = layout.box()
        box.label(text="Render Global Settings", icon='RENDER_ANIMATION')
        
        # 出力パス設定
        box.prop(self, "output_path")
        box.label(text="* {project_name} will be replaced with project name", icon='INFO')
        
        # ファイルフォーマット設定
        box.prop(self, "file_format")
        box.prop(self, "color_mode")
        box.prop(self, "color_depth")
        
        # 使用方法の説明
        layout.separator()
        box = layout.box()
        box.label(text="Usage", icon='QUESTION')
        box.label(text="• Settings are applied automatically when saving projects")
        box.label(text="• Manual execution available from Properties > Output Properties > Wizender")

