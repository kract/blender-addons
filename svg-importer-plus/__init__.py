bl_info = {
    "name": "SVG Importer Plus",
    "author": "KRACT Studio", 
    "version": (1, 0, 3),
    "blender": (4, 2, 0),
    "description": "Enhanced SVG import with automatic mesh conversion and origin centering",
    "location": "File > Import > SVG Importer Plus (.svg)",
    "category": "Import-Export"
}

if "bpy" in locals():
    import importlib
    importlib.reload(material_manager)
    importlib.reload(post_processor)
    importlib.reload(operators)
    importlib.reload(file_handler)
    importlib.reload(translations)
else:
    from . import material_manager
    from . import post_processor
    from . import operators
    from . import file_handler
    from . import translations

import bpy
from bpy.app.translations import pgettext_iface as _

def menu_func_import(self, context):
    op = self.layout.operator(operators.IMPORT_OT_svg_plus.bl_idname, text=_("SVG Importer Plus (.svg)"))
    op.is_menu = True

classes = (
    operators.IMPORT_OT_svg_plus,
    file_handler.SVG_FH_import_plus,
)

def register():
    """アドオン登録"""
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.TOPBAR_MT_file_import.append(menu_func_import)
    translations.SVGTranslations.register_translations(__name__)

def unregister():
    """アドオン登録解除"""
    translations.SVGTranslations.unregister_translations(__name__)
    
    # Safely remove menu function
    try:
        bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)
    except (ValueError, AttributeError):
        pass  # Already removed or doesn't exist
    
    # Safely unregister classes
    for cls in reversed(classes):
        try:
            bpy.utils.unregister_class(cls)
        except RuntimeError:
            pass  # Already unregistered

if __name__ == "__main__":
    register()
