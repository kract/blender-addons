import bpy
import os

class WIZENDER_OT_set_settings(bpy.types.Operator):
    bl_idname = "wizender.set_settings"
    bl_label = "Apply Wizender Settings"
    bl_description = "Set render global settings based on project filename"

    def execute(self, context):
        from . import render_settings
        render_settings.set_render_settings()
        return {'FINISHED'}

