import bpy
from bpy.props import BoolProperty
from bpy.types import AddonPreferences


class VERSAVE_AddonPreferences(AddonPreferences):
    bl_idname = __package__

    create_project_dir: BoolProperty(
        name="プロジェクトディレクトリを作成",
        description="初回保存時にプロジェクト名のディレクトリを作成してその中に保存する",
        default=True,
    )

    def draw(self, context):
        self.layout.prop(self, "create_project_dir")
