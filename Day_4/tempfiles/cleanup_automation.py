import os

folder_path = r"C:\Users\akshi\OneDrive\Desktop\PRIMARY TRACK\Day_4\tempfiles"
file_extensions_to_remove = (".tmp", ".log", ".bak")  # temp files

deleted_files = []

for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)
    
    if os.path.isfile(file_path) and file_name.endswith(file_extensions_to_remove):
        os.remove(file_path)
        deleted_files.append(file_name)
        print(f"Deleted: {file_name}")

print(f"Cleanup completed. {len(deleted_files)} files removed.")
