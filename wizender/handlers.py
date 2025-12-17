import bpy
from bpy.app.handlers import persistent
from . import render_settings

# 保存時ハンドラー
@persistent
def auto_render_on_save(dummy):
    print("[Wizender] Save detected. Applying settings...")
    render_settings.set_render_settings()

