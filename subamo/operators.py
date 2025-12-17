import bpy
import os
from bpy.props import IntProperty
from bpy.app.translations import pgettext_iface as _

class SUBAMO_OT_delete_backup(bpy.types.Operator):
    """Delete selected backup file"""
    bl_idname = "subamo.delete_backup"
    bl_label = "Delete Backup"
    bl_options = {'REGISTER', 'UNDO'}
    
    backup_index: IntProperty()
    
    def execute(self, context):
        current_filepath = bpy.data.filepath
        if not current_filepath:
            self.report({'WARNING'}, _("No file currently open"))
            return {'CANCELLED'}
        
        current_dir = os.path.dirname(current_filepath)
        current_filename = os.path.basename(current_filepath)
        base_name = os.path.splitext(current_filename)[0]
        backup_dir = os.path.join(current_dir, "backup")
        
        backup_extensions = [f'.blend{i}' for i in range(1, 33)]  # .blend1 to .blend32
        
        if self.backup_index < len(backup_extensions):
            ext = backup_extensions[self.backup_index]
            backup_filename = base_name + ext
            backup_filepath = os.path.join(backup_dir, backup_filename)
            
            if os.path.exists(backup_filepath):
                try:
                    os.remove(backup_filepath)
                    self.report({'INFO'}, _("Deleted {}").format(backup_filename))
                except Exception as e:
                    self.report({'ERROR'}, _("Failed to delete backup: {}").format(str(e)))
                    return {'CANCELLED'}
            else:
                self.report({'WARNING'}, _("Backup file not found"))
                return {'CANCELLED'}
        
        return {'FINISHED'}

class SUBAMO_OT_open_backup(bpy.types.Operator):
    """Open selected backup file"""
    bl_idname = "subamo.open_backup"
    bl_label = "Open Backup"
    bl_options = {'REGISTER'}
    
    backup_index: IntProperty()
    
    def execute(self, context):
        current_filepath = bpy.data.filepath
        if not current_filepath:
            self.report({'WARNING'}, _("No file currently open"))
            return {'CANCELLED'}
        
        current_dir = os.path.dirname(current_filepath)
        current_filename = os.path.basename(current_filepath)
        base_name = os.path.splitext(current_filename)[0]
        backup_dir = os.path.join(current_dir, "backup")
        
        backup_extensions = [f'.blend{i}' for i in range(1, 33)]  # .blend1 to .blend32
        
        if self.backup_index < len(backup_extensions):
            ext = backup_extensions[self.backup_index]
            backup_filename = base_name + ext
            backup_filepath = os.path.join(backup_dir, backup_filename)
            
            if os.path.exists(backup_filepath):
                try:
                    bpy.ops.wm.open_mainfile(filepath=backup_filepath)
                    self.report({'INFO'}, _("Opened {}").format(backup_filename))
                except Exception as e:
                    self.report({'ERROR'}, _("Failed to open backup: {}").format(str(e)))
                    return {'CANCELLED'}
            else:
                self.report({'WARNING'}, _("Backup file not found"))
                return {'CANCELLED'}
        
        return {'FINISHED'}

