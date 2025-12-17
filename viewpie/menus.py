import bpy
from bpy.types import Menu
from . import operators

class VIEWPIE_MT_pie_menu(Menu):
    """Viewpie pie menu for viewport navigation"""
    bl_label = "Viewpie"
    bl_idname = "VIEWPIE_MT_pie_menu"
    
    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        
        # Right (3 o'clock) - Left View  
        op = pie.operator("viewpie.set_view", text=operators.get_translation("Left"), icon='TRIA_LEFT')
        op.view_type = 'LEFT'
        
        # Left (9 o'clock) - Right View
        op = pie.operator("viewpie.set_view", text=operators.get_translation("Right"), icon='TRIA_RIGHT')
        op.view_type = 'RIGHT'
        
        # Bottom (6 o'clock) - Bottom View
        op = pie.operator("viewpie.set_view", text=operators.get_translation("Bottom"), icon='TRIA_DOWN')
        op.view_type = 'BOTTOM'
        
        # Top (12 o'clock) - Top View
        op = pie.operator("viewpie.set_view", text=operators.get_translation("Top"), icon='TRIA_UP')
        op.view_type = 'TOP'
        
        # Top-Left (10:30) - Back View
        op = pie.operator("viewpie.set_view", text=operators.get_translation("Back"), icon='LOOP_BACK')
        op.view_type = 'BACK'
        
        # Top-Right (1:30) - Front View
        op = pie.operator("viewpie.set_view", text=operators.get_translation("Front"), icon='LOOP_FORWARDS')
        op.view_type = 'FRONT'
        
        # Bottom-Left (7:30) - Camera View
        op = pie.operator("viewpie.set_view", text=operators.get_translation("Camera"), icon='CAMERA_DATA')
        op.view_type = 'CAMERA'
        
        # Bottom-Right (4:30) - View Selected
        op = pie.operator("viewpie.set_view", text=operators.get_translation("View Selected"), icon='ZOOM_SELECTED')
        op.view_type = 'SELECTED'

class VIEWPIE_MT_pie_menu_extended(Menu):
    """Extended Viewpie pie menu with additional options"""
    bl_label = "Viewpie Extended"
    bl_idname = "VIEWPIE_MT_pie_menu_extended"
    
    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        
        # Right (3 o'clock) - View Selected
        op = pie.operator("viewpie.set_view", text=operators.get_translation("View Selected"), icon='ZOOM_SELECTED')
        op.view_type = 'SELECTED'
        
        # Left (9 o'clock) - View All
        op = pie.operator("viewpie.set_view", text=operators.get_translation("View All"), icon='VIEWZOOM')
        op.view_type = 'ALL'
        
        # Bottom (6 o'clock) - Center View
        op = pie.operator("viewpie.set_view", text=operators.get_translation("Center Cursor"), icon='PIVOT_CURSOR')
        op.view_type = 'CENTER'
        
        # Top (12 o'clock) - Main Pie Menu
        pie.menu("VIEWPIE_MT_pie_menu", text=operators.get_translation("Basic Views"), icon='VIEW3D')
        
        # Top-Left (10:30) - Perspective
        op = pie.operator("viewpie.set_view", text=operators.get_translation("Perspective"), icon='VIEW_PERSPECTIVE')
        op.view_type = 'PERSPECTIVE'
        
        # Top-Right (1:30) - Orthographic
        op = pie.operator("viewpie.set_view", text=operators.get_translation("Orthographic"), icon='VIEW_ORTHO')
        op.view_type = 'ORTHOGRAPHIC'
        
        # Bottom-Left (7:30) - Camera View
        op = pie.operator("viewpie.set_view", text=operators.get_translation("Camera"), icon='CAMERA_DATA')
        op.view_type = 'CAMERA'
        
        # Bottom-Right (4:30) - Empty for future expansion
        pie.separator()

