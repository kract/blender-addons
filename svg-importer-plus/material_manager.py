import bpy
from typing import List

class SVGMaterialManager:
    """Handles SVG material cleanup operations"""
    
    @staticmethod
    def remove_materials_from_objects(objects: List[bpy.types.Object]) -> None:
        """Remove all materials from specified objects"""
        for obj in objects:
            if obj.data and hasattr(obj.data, 'materials'):
                obj.data.materials.clear()
    
    @staticmethod
    def cleanup_unused_svg_materials() -> int:
        """Remove unused SVG materials from Blender's material database"""
        materials_to_remove = []
        for material in bpy.data.materials:
            if material.name.startswith("SVG") and material.users == 0:
                materials_to_remove.append(material)
        
        for material in materials_to_remove:
            bpy.data.materials.remove(material)
        
        return len(materials_to_remove)
    
    @classmethod
    def remove_svg_materials(cls, objects: List[bpy.types.Object]) -> int:
        """Complete SVG material removal process"""
        cls.remove_materials_from_objects(objects)
        return cls.cleanup_unused_svg_materials()

