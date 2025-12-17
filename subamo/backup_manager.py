import os
import shutil

def organize_backup_files(current_filepath):
    """現在のファイルパスに基づいてバックアップファイルを整理"""
    if not current_filepath:
        return 0
    
    # 現在のファイルのディレクトリとベース名を取得
    current_dir = os.path.dirname(current_filepath)
    current_filename = os.path.basename(current_filepath)
    base_name = os.path.splitext(current_filename)[0]
    
    # backupフォルダのパスを作成
    backup_dir = os.path.join(current_dir, "backup")
    
    # バックアップファイルの拡張子リスト（Blenderの最大32個に対応）
    backup_extensions = [f'.blend{i}' for i in range(1, 33)]  # .blend1 to .blend32
    
    moved_count = 0
    
    # 各バックアップファイルをチェック
    for ext in backup_extensions:
        backup_filename = base_name + ext
        backup_filepath = os.path.join(current_dir, backup_filename)
        
        # バックアップファイルが存在する場合
        if os.path.exists(backup_filepath):
            # backupフォルダが存在しない場合は作成
            if not os.path.exists(backup_dir):
                os.makedirs(backup_dir)
            
            # バックアップファイルをbackupフォルダに移動
            destination_path = os.path.join(backup_dir, backup_filename)
            
            # 同名ファイルが既に存在する場合は上書き
            if os.path.exists(destination_path):
                os.remove(destination_path)
            
            shutil.move(backup_filepath, destination_path)
            moved_count += 1
    
    return moved_count

