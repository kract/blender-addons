import bpy
from . import operators

class NUKESHIMA_MT_delete_menu(bpy.types.Menu):
    """Nukeshima delete menu"""
    bl_label = "Nukeshima Delete"
    bl_idname = "NUKESHIMA_MT_delete_menu"
    
    def draw(self, context):
        layout = self.layout
        
        if context.mode == 'OBJECT':
            # Object mode - simple delete
            op = layout.operator("nukeshima.silent_delete", text=operators.get_translation("Delete Objects"), icon='X')
            op.delete_type = 'OBJECT'
        
        elif context.mode == 'EDIT_MESH':
            # Edit mode - full delete menu
            
            # Standard delete operations
            layout.label(text="Delete:", icon='X')
            
            op = layout.operator("nukeshima.silent_delete", text=operators.get_translation("Delete Vertices"), icon='VERTEXSEL')
            op.delete_type = 'VERT'
            
            op = layout.operator("nukeshima.silent_delete", text=operators.get_translation("Delete Edges"), icon='EDGESEL')
            op.delete_type = 'EDGE'
            
            op = layout.operator("nukeshima.silent_delete", text=operators.get_translation("Delete Faces"), icon='FACESEL')
            op.delete_type = 'FACE'
            
            layout.separator()
            
            op = layout.operator("nukeshima.silent_delete", text=operators.get_translation("Only Edges & Faces"), icon='MESH_DATA')
            op.delete_type = 'EDGE_FACE'
            
            op = layout.operator("nukeshima.silent_delete", text=operators.get_translation("Only Faces"), icon='MESH_DATA')
            op.delete_type = 'ONLY_FACE'
            
            layout.separator()
            
            # Dissolve operations
            layout.label(text="Dissolve:", icon='MOD_DECIM')
            
            op = layout.operator("nukeshima.silent_delete", text=operators.get_translation("Dissolve Vertices"), icon='VERTEXSEL')
            op.delete_type = 'DISSOLVE_VERTS'
            
            op = layout.operator("nukeshima.silent_delete", text=operators.get_translation("Dissolve Edges"), icon='EDGESEL')
            op.delete_type = 'DISSOLVE_EDGES'
            
            op = layout.operator("nukeshima.silent_delete", text=operators.get_translation("Dissolve Faces"), icon='FACESEL')
            op.delete_type = 'DISSOLVE_FACES'
            
            op = layout.operator("nukeshima.silent_delete", text=operators.get_translation("Limited Dissolve"), icon='MOD_DECIM')
            op.delete_type = 'DISSOLVE_LIMITED'
            
            layout.separator()
            
            # Additional operations
            op = layout.operator("nukeshima.silent_delete", text=operators.get_translation("Edge Collapse"), icon='EDGESEL')
            op.delete_type = 'EDGE_COLLAPSE'
            
            op = layout.operator("nukeshima.silent_delete", text=operators.get_translation("Edge Loops"), icon='EDGESEL')
            op.delete_type = 'EDGE_LOOPS'

