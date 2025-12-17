import bpy

class SVGTranslations:
    """Centralized translation management for SVG Importer Plus"""
    
    TRANSLATIONS = {
        "en_US": {},
        "ja_JP": {
            # Operator descriptions
            ("*", "Import SVG with automatic mesh conversion and origin centering"): 
                "自動メッシュ変換と原点中央配置でSVGをインポート",
            ("*", "SVG Importer Plus"): "SVG Importer Plus",
            
            # Property labels and descriptions  
            ("*", "Convert to Mesh"): "メッシュに変換",
            ("*", "Automatically convert curves to mesh"): "カーブを自動的にメッシュに変換",
            ("*", "Center Origin"): "原点を中央に",
            ("*", "Move origin to geometry center"): "原点をジオメトリの中心に移動",
            
            ("*", "Join Objects"): "オブジェクトを結合",
            ("*", "Join all imported objects into one"): "インポートしたすべてのオブジェクトをひとつに結合",
            
            # UI labels
            ("*", "Post-Processing Options:"): "後処理オプション:",
            ("*", "SVG Importer Plus (.svg)"): "SVG Importer Plus (.svg)",
            
            # Status messages
            ("*", "No objects were imported"): "オブジェクトがインポートされませんでした",
            
            # Formatting
            ("*", ", "): "、",
        }
    }
    
    @classmethod
    def get_translations(cls):
        """Get the translation dictionary"""
        return cls.TRANSLATIONS
    
    @classmethod
    def register_translations(cls, module_name: str):
        """Register translations with Blender"""
        try:
            bpy.app.translations.register(module_name, cls.TRANSLATIONS)
        except ValueError:
            pass
    
    @classmethod
    def unregister_translations(cls, module_name: str):
        """Unregister translations from Blender"""
        try:
            bpy.app.translations.unregister(module_name)
        except ValueError:
            pass

