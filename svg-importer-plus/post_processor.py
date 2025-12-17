import bpy

class SVGPostProcessor:
    """Handles post-processing operations for imported SVG objects"""
    
    def __init__(self, convert_to_mesh: bool = True, center_origin: bool = True):
        self.convert_to_mesh = convert_to_mesh
        self.center_origin = center_origin
        self.converted_count = 0
        self.centered_count = 0
    
    def process_object(self, obj: bpy.types.Object) -> None:
        """Process a single object with mesh conversion and origin centering"""
        bpy.context.view_layer.objects.active = obj
        obj.select_set(True)
        
        try:
            if self.convert_to_mesh and obj.type == 'CURVE':
                self._convert_to_mesh(obj)
            
            if self.center_origin:
                self._center_origin(obj)
        
        finally:
            obj.select_set(False)
    
    def _convert_to_mesh(self, obj: bpy.types.Object) -> None:
        """Convert curve object to mesh"""
        try:
            bpy.ops.object.convert(target='MESH')
            self.converted_count += 1
        except Exception as e:
            raise RuntimeError(f"Failed to convert {obj.name} to mesh: {str(e)}")
    
    def _center_origin(self, obj: bpy.types.Object) -> None:
        """Center object origin to geometry bounds"""
        try:
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='BOUNDS')
            self.centered_count += 1
        except Exception as e:
            raise RuntimeError(f"Failed to center origin for {obj.name}: {str(e)}")
    
    def get_statistics(self) -> tuple:
        """Get processing statistics"""
        return self.converted_count, self.centered_count

