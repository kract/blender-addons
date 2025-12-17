import bpy
import os
import datetime
from bpy.app.translations import pgettext_iface as _

class SUBAMO_PT_panel(bpy.types.Panel):
    """Subamo パネル"""
    bl_label = "Subamo"
    bl_idname = "SUBAMO_PT_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Tool"
    
    def draw(self, context):
        layout = self.layout
        
        # 現在のファイル情報を表示
        current_filepath = bpy.data.filepath
        if current_filepath:
            current_dir = os.path.dirname(current_filepath)
            current_filename = os.path.basename(current_filepath)
            base_name = os.path.splitext(current_filename)[0]
            backup_dir = os.path.join(current_dir, "backup")
            
            layout.label(text=_("Backup Files:"))
            
            if os.path.exists(backup_dir):
                # 同じプロジェクトのバックアップファイル一覧を取得
                backup_extensions = [f'.blend{i}' for i in range(1, 33)]  # .blend1 to .blend32
                backup_files = []
                
                for i, ext in enumerate(backup_extensions):
                    backup_filename = base_name + ext
                    backup_filepath = os.path.join(backup_dir, backup_filename)
                    
                    if os.path.exists(backup_filepath):
                        # ファイル情報を取得
                        stat = os.stat(backup_filepath)
                        modified_time = datetime.datetime.fromtimestamp(stat.st_mtime)
                        backup_files.append({
                            'index': i,
                            'number': ext[6:],  # .blend1 -> 1
                            'filename': backup_filename,
                            'datetime': modified_time.strftime("%m/%d %H:%M"),
                            'size': round(stat.st_size / 1024 / 1024, 1)  # MB
                        })
                
                # バックアップファイルを新しい順にソート（番号が大きい = 新しい）
                backup_files.sort(key=lambda x: int(x['number']), reverse=True)
                
                if backup_files:
                    # Versave風のリスト表示
                    box = layout.box()
                    
                    col = box.column(align=False)
                    max_visible_rows = 10  # 最大表示数（32個まで対応するため少し増加）
                    
                    for i, backup in enumerate(backup_files[:max_visible_rows]):
                        # アイテム間の間隔
                        if i > 0:
                            col.separator(factor=0.3)
                        
                        row = col.row(align=True)
                        
                        # バックアップアイコン
                        row.label(text="", icon='FILE_BACKUP')
                        
                        # バックアップ番号（固定幅・番号大きい=新しい）
                        number_col = row.column()
                        number_col.ui_units_x = 2.0  # 2桁対応のため幅を拡張
                        number_col.label(text=f"#{backup['number']}")
                        
                        # 日時（固定幅）
                        date_col = row.column()
                        date_col.ui_units_x = 4.0
                        date_col.label(text=backup['datetime'])
                        
                        # ファイルサイズ（固定幅・右寄せ）
                        size_col = row.column()
                        size_col.ui_units_x = 3.5
                        size_col.alignment = 'RIGHT'
                        size_col.label(text=f"{backup['size']}MB")
                        
                        # スペーサー
                        row.separator()
                        
                        # 開くボタン
                        open_op = row.operator("subamo.open_backup", text="", icon='FILE_FOLDER')
                        open_op.backup_index = backup['index']

                        layout.separator()
                        
                        # 削除ボタン
                        delete_op = row.operator("subamo.delete_backup", text="", icon='TRASH')
                        delete_op.backup_index = backup['index']
                    
                    # 表示されていないファイルがある場合の表示
                    if len(backup_files) > max_visible_rows:
                        col.separator(factor=0.3)
                        col.label(text=f"... {_('... and {} more files').format(len(backup_files) - max_visible_rows)}")
                    
                    # 統計情報
                    layout.separator(factor=0.5)
                    stats_row = layout.row()
                    stats_row.scale_y = 0.8
                    total_size = sum(backup['size'] for backup in backup_files)
                    stats_row.label(text=_("Total: {} files, {:.1f}MB").format(len(backup_files), total_size))
                    
                else:
                    layout.label(text="No backup files found")
            else:
                layout.label(text="No backup folder")
        else:
            layout.label(text="No file open")

