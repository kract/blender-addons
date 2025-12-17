import bpy

class VIEWCAM_OT_set_view_to_camera(bpy.types.Operator):
    """Set current viewport view to active camera"""
    bl_idname = "viewcam.set_view_to_camera"
    bl_label = "View to Camera"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        # 3Dビューポートにいるかチェック
        return context.area and context.area.type == 'VIEW_3D'
    
    def execute(self, context):
        # アクティブなカメラを取得
        camera = context.scene.camera
        if not camera:
            self.report({'WARNING'}, "No active camera in scene")
            return {'CANCELLED'}
        
        # 現在の3Dビューの情報を取得
        area = context.area
        region = None
        region_3d = None
        
        for region in area.regions:
            if region.type == 'WINDOW':
                region_3d = region.data
                break
        
        if not region_3d:
            self.report({'ERROR'}, "Could not find 3D viewport region")
            return {'CANCELLED'}
        
        # 現在のビューマトリックスを取得
        view_matrix = region_3d.view_matrix.copy()
        
        # ビューマトリックスをワールド座標のカメラ変換マトリックスに変換
        # view_matrix は world_to_view 変換なので、逆行列を取ってカメラの位置・回転を取得
        camera_matrix = view_matrix.inverted()
        
        # カメラオブジェクトの変換を設定
        camera.matrix_world = camera_matrix
        
        # 変更を更新
        context.view_layer.update()
        
        # カメラビューに切り替え
        bpy.ops.view3d.view_camera()
        
        self.report({'INFO'}, f"Camera '{camera.name}' set to current view")
        return {'FINISHED'}


class VIEWCAM_OT_toggle_camera_to_view(bpy.types.Operator):
    """Toggle 'Camera to View' lock on/off"""
    bl_idname = "viewcam.toggle_camera_to_view"
    bl_label = "Toggle Camera to View"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        # 3Dビューポートかつカメラビューにいるかチェック
        if not (context.area and context.area.type == 'VIEW_3D'):
            return False
        
        # カメラビューかどうか確認
        region_3d = None
        for region in context.area.regions:
            if region.type == 'WINDOW':
                region_3d = region.data
                break
        
        return region_3d and region_3d.view_perspective == 'CAMERA'
    
    def execute(self, context):
        camera = context.scene.camera
        if not camera:
            self.report({'WARNING'}, "No active camera in scene")
            return {'CANCELLED'}
        
        # カメラビューにいることを再確認
        region_3d = None
        for region in context.area.regions:
            if region.type == 'WINDOW':
                region_3d = region.data
                break
        
        if not region_3d or region_3d.view_perspective != 'CAMERA':
            self.report({'WARNING'}, "Must be in camera view to toggle Lock Camera to View")
            return {'CANCELLED'}
        
        # Lock Camera to Viewの状態を切り替え
        space_data = context.space_data
        space_data.lock_camera = not space_data.lock_camera
        
        status = "enabled" if space_data.lock_camera else "disabled"
        self.report({'INFO'}, f"Lock Camera to View: {status}")
        return {'FINISHED'}

