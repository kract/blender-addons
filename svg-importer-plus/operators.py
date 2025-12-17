import bpy
import bmesh
from bpy_extras.io_utils import ImportHelper
from bpy.props import StringProperty, BoolProperty
from bpy.types import Operator
from bpy.app.translations import pgettext_iface as _
from typing import Set, List
import os
from . import material_manager, post_processor

class IMPORT_OT_svg_plus(Operator, ImportHelper):
    """Import SVG with automatic mesh conversion and origin centering"""
    bl_idname = "import_mesh.svg_plus"
    bl_label = "SVG Importer Plus"
    bl_options = {'REGISTER', 'UNDO'}

    filename_ext = ".svg"
    filter_glob: StringProperty(
        default="*.svg",
        options={'HIDDEN'},
        maxlen=255,
    )

    convert_to_mesh: BoolProperty(
        name="Convert to Mesh",
        description="Automatically convert curves to mesh",
        default=True,
    )

    join_objects: BoolProperty(
        name="Join Objects",
        description="Join all imported objects into one",
        default=False,
    )

    center_origin: BoolProperty(
        name="Center Origin",
        description="Move origin to geometry center",
        default=True,
    )

    is_menu: BoolProperty(
        options={'HIDDEN', 'SKIP_SAVE'},
        default=False,
    )

    def invoke(self, context, event):
        if not self.is_menu and self.filepath and os.path.isfile(self.filepath) and self.filepath.lower().endswith('.svg'):
            return self.execute(context)
        return super().invoke(context, event)

    def execute(self, context):
        if not self._validate_inputs():
            return {'CANCELLED'}
        
        try:
            original_objects = set(context.scene.objects)
            new_objects = self._import_svg_file(original_objects)
            
            if not new_objects:
                self.report({'WARNING'}, _("No objects were imported"))
                return {'CANCELLED'}
            
            self._process_imported_objects(new_objects)
            self._report_results(new_objects)
            
            return {'FINISHED'}
            
        except Exception as e:
            self.report({'ERROR'}, f"Import failed: {str(e)}")
            return {'CANCELLED'}
    
    def _validate_inputs(self) -> bool:
        """Validate input parameters before processing"""
        
        if not self.filepath:
            self.report({'ERROR'}, "No file path specified")
            return False
        
        if not os.path.exists(self.filepath):
            self.report({'ERROR'}, f"File does not exist: {self.filepath}")
            return False
        
        if not self.filepath.lower().endswith('.svg'):
            self.report({'ERROR'}, "Selected file is not an SVG file")
            return False
        
        try:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                content = f.read(1024)
                if '<svg' not in content.lower():
                    self.report({'ERROR'}, "File does not appear to be a valid SVG")
                    return False
        except Exception as e:
            self.report({'ERROR'}, f"Cannot read file: {str(e)}")
            return False
        
        return True
    
    def _import_svg_file(self, original_objects: Set[bpy.types.Object]) -> List[bpy.types.Object]:
        """Import SVG file and return newly created objects"""
        try:
            bpy.ops.import_curve.svg(filepath=self.filepath)
        except Exception as e:
            raise RuntimeError(f"Failed to import SVG: {str(e)}")
        
        return [obj for obj in bpy.context.scene.objects if obj not in original_objects]
    
    def _process_imported_objects(self, new_objects: List[bpy.types.Object]) -> None:
        """Process all imported objects with material cleanup and post-processing"""
        material_manager.SVGMaterialManager.remove_svg_materials(new_objects)

        if self.join_objects and len(new_objects) > 1:
            new_objects = self._join_objects(new_objects)
        
        processor = post_processor.SVGPostProcessor(self.convert_to_mesh, self.center_origin)
        
        for obj in new_objects:
            try:
                processor.process_object(obj)
            except RuntimeError as e:
                self.report({'WARNING'}, str(e))
        
        self.converted_count, self.centered_count = processor.get_statistics()
    
    def _report_results(self, new_objects: List[bpy.types.Object]) -> None:
        """Generate and report import results"""
        total_objects = len(new_objects)
        messages = [f"Imported {total_objects} object(s)"]
        
        if self.convert_to_mesh and self.converted_count > 0:
            messages.append(f"converted {self.converted_count} to mesh")
        
        if self.center_origin and self.centered_count > 0:
            messages.append(f"centered {self.centered_count} origins")
        
        self.report({'INFO'}, _(", ").join(messages))

    def _join_objects(self, objects: List[bpy.types.Object]) -> List[bpy.types.Object]:
        """Join multiple objects into one"""
        if not objects:
            return []
            
        # Deselect all
        bpy.ops.object.select_all(action='DESELECT')
        
        # Select all objects to join
        for obj in objects:
            obj.select_set(True)
            
        # Set active object (last one)
        bpy.context.view_layer.objects.active = objects[-1]
        
        try:
            bpy.ops.object.join()
            return [bpy.context.view_layer.objects.active]
        except Exception as e:
            self.report({'WARNING'}, f"Failed to join objects: {str(e)}")
            return objects

    def draw(self, context):
        layout = self.layout
        
        layout.use_property_split = True
        layout.use_property_decorate = False
        
        layout.separator()
        layout.label(text=_("Post-Processing Options:"))
        
        layout.prop(self, "join_objects")
        layout.prop(self, "convert_to_mesh")
        layout.prop(self, "center_origin")

