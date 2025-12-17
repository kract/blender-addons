import bpy
import bmesh

# Translation dictionary
translations = {
    "en_US": {
        "Delete Vertices": "Delete Vertices",
        "Delete Edges": "Delete Edges", 
        "Delete Faces": "Delete Faces",
        "Delete Objects": "Delete Objects",
        "Dissolve Vertices": "Dissolve Vertices",
        "Dissolve Edges": "Dissolve Edges",
        "Dissolve Faces": "Dissolve Faces",
        "Limited Dissolve": "Limited Dissolve",
        "Edge Collapse": "Edge Collapse",
        "Edge Loops": "Edge Loops",
        "Only Edges & Faces": "Only Edges & Faces",
        "Only Faces": "Only Faces"
    },
    "ja_JP": {
        "Delete Vertices": "頂点を削除",
        "Delete Edges": "辺を削除",
        "Delete Faces": "面を削除", 
        "Delete Objects": "オブジェクトを削除",
        "Dissolve Vertices": "頂点を融解",
        "Dissolve Edges": "辺を融解",
        "Dissolve Faces": "面を融解",
        "Limited Dissolve": "制限融解",
        "Edge Collapse": "辺を潰す",
        "Edge Loops": "辺ループ",
        "Only Edges & Faces": "辺と面のみ",
        "Only Faces": "面のみ"
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

class NUKESHIMA_OT_silent_delete(bpy.types.Operator):
    """Silent delete without confirmation dialogs"""
    bl_idname = "nukeshima.silent_delete"
    bl_label = "Silent Delete"
    bl_options = {'REGISTER', 'UNDO'}
    
    delete_type: bpy.props.StringProperty(name="Delete Type")
    
    @classmethod
    def poll(cls, context):
        return context.area and context.area.type == 'VIEW_3D'
    
    def execute(self, context):
        # Object mode - delete selected objects
        if context.mode == 'OBJECT':
            if context.selected_objects:
                bpy.ops.object.delete(use_global=False, confirm=False)
            return {'FINISHED'}
        
        # Edit mode - delete based on selection mode and type
        if context.mode == 'EDIT_MESH':
            mesh = context.edit_object.data
            
            # Check what's selected
            bm = bmesh.from_edit_mesh(mesh)
            
            selected_verts = [v for v in bm.verts if v.select]
            selected_edges = [e for e in bm.edges if e.select]
            selected_faces = [f for f in bm.faces if f.select]
            
            if not (selected_verts or selected_edges or selected_faces):
                return {'CANCELLED'}
            
            # Execute the appropriate delete operation
            if self.delete_type == 'VERT':
                bpy.ops.mesh.delete(type='VERT')
            elif self.delete_type == 'EDGE':
                bpy.ops.mesh.delete(type='EDGE')
            elif self.delete_type == 'FACE':
                bpy.ops.mesh.delete(type='FACE')
            elif self.delete_type == 'EDGE_FACE':
                bpy.ops.mesh.delete(type='EDGE_FACE')
            elif self.delete_type == 'ONLY_FACE':
                bpy.ops.mesh.delete(type='ONLY_FACE')
            elif self.delete_type == 'DISSOLVE_VERTS':
                bpy.ops.mesh.dissolve_verts()
            elif self.delete_type == 'DISSOLVE_EDGES':
                bpy.ops.mesh.dissolve_edges()
            elif self.delete_type == 'DISSOLVE_FACES':
                bpy.ops.mesh.dissolve_faces()
            elif self.delete_type == 'DISSOLVE_LIMITED':
                bpy.ops.mesh.dissolve_limited()
            elif self.delete_type == 'EDGE_COLLAPSE':
                bpy.ops.mesh.edge_collapse()
            elif self.delete_type == 'EDGE_LOOPS':
                bpy.ops.mesh.delete(type='EDGE_LOOP')
            else:
                # Smart delete based on selection
                if selected_faces:
                    bpy.ops.mesh.delete(type='FACE')
                elif selected_edges:
                    bpy.ops.mesh.delete(type='EDGE')
                elif selected_verts:
                    bpy.ops.mesh.delete(type='VERT')
            
            return {'FINISHED'}
        
        return {'CANCELLED'}

class NUKESHIMA_OT_smart_delete(bpy.types.Operator):
    """Smart delete - automatically chooses best delete method"""
    bl_idname = "nukeshima.smart_delete"
    bl_label = "Smart Delete"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        return context.area and context.area.type == 'VIEW_3D'
    
    def execute(self, context):
        # Object mode - delete selected objects
        if context.mode == 'OBJECT':
            if context.selected_objects:
                bpy.ops.object.delete(use_global=False, confirm=False)
            return {'FINISHED'}
        
        # Edit mode - smart selection-based delete
        if context.mode == 'EDIT_MESH':
            mesh = context.edit_object.data
            
            bm = bmesh.from_edit_mesh(mesh)
            
            selected_verts = [v for v in bm.verts if v.select]
            selected_edges = [e for e in bm.edges if e.select]
            selected_faces = [f for f in bm.faces if f.select]
            
            if not (selected_verts or selected_edges or selected_faces):
                return {'CANCELLED'}
            
            # Smart delete logic: prioritize faces > edges > vertices
            if selected_faces:
                bpy.ops.mesh.delete(type='FACE')
            elif selected_edges:
                bpy.ops.mesh.delete(type='EDGE')
            elif selected_verts:
                bpy.ops.mesh.delete(type='VERT')
            
            return {'FINISHED'}
        
        return {'CANCELLED'}

