import os
import datetime

def get_folder_size(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            try:
                total_size += os.path.getsize(fp)
            except OSError:
                pass  # Handle cases where the file is inaccessible
    return total_size

def format_size(size_bytes):
    units = ['B', 'KB', 'MB', 'GB']
    unit_index = 0
    while size_bytes >= 1024 and unit_index < 3:
        size_bytes /= 1024
        unit_index += 1
    return f"{size_bytes:.2f} {units[unit_index]}"

def ls(path):
    print(f"\n\n    Directory: {path}\n\n")
    print(f"{'LastWriteTime':<20} {'Type':<15} {'Size':<10} {'Name'}")
    print(f"{'-------------':<20} {'----':<15} {'----':<10} {'----'}")

    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        try:
            stat_info = os.stat(full_path)
            if os.path.isdir(full_path):
                type = "folder"
            else:
                name, ext = os.path.splitext(item)
                type = ext if ext else "file"
            last_write_time = datetime.datetime.fromtimestamp(stat_info.st_mtime).strftime('%m/%d/%Y %I:%M %p')
            size = stat_info.st_size
            if os.path.isdir(full_path):
                size = get_folder_size(full_path)
            print(f"{last_write_time:<20} {type:<15} {format_size(size):<10} {item}")
        except Exception as e:
            print(f"Error accessing {item}: {e}")

if __name__ == "__main__":
    TEST_FOLDER_PATH = r"C:\\Users\\otash\\Documents"
    ls(TEST_FOLDER_PATH)
