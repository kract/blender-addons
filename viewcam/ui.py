import bpy
from . import operators

def draw_viewcam_button(self, context):
    """3Dビューポートヘッダーにボタンを描画"""
    layout = self.layout
    
    # カメラが存在する場合のみボタンを表示
    if context.scene.camera:
        layout.operator("viewcam.set_view_to_camera", text="", icon='CAMERA_DATA', emboss=False)

