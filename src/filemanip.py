import os
import shutil

def delete_directory(victim_path):
    if os.path.exists(victim_path):
        shutil.rmtree(victim_path)
        print(f"Deleted directory path '{victim_path}'")
    else:
        print(f"Error: No directory path '{victim_path}'")

def copy_dir_contents(source_path, dest_path):
    if not os.path.exists(source_path):
        print(f"Error: Source path '{source_path}' does not exist")
        return
    copy_dir_content_recursive(source_path, dest_path)
    
def copy_dir_content_recursive(source_path, dest_path):
    if not os.path.exists(dest_path):
        os.mkdir(dest_path)
    content_list = os.listdir(source_path)
    for file in content_list:
        file_source_path = os.path.join(source_path, file)
        file_dest_path = os.path.join(dest_path, file)
        print(f"{file_source_path} -> {file_dest_path}")
        if os.path.isfile(file_source_path):
            shutil.copy(file_source_path, file_dest_path)
        else:
            copy_dir_content_recursive(file_source_path, file_dest_path)
            
