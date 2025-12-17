import bpy

class SVG_FH_import_plus(bpy.types.FileHandler):
    bl_idname = "SVG_FH_import_plus"
    bl_label = "SVG Importer Plus"
    bl_import_operator = "import_mesh.svg_plus"
    bl_file_extensions = ".svg"

    @classmethod
    def poll_drop(cls, context):
        return (context.area and context.area.type == 'VIEW_3D')

