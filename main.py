import os
import datetime
import sys

def get_folder_size(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            try:
                total_size += os.path.getsize(fp)
            except OSError:
                pass
    return total_size

def format_size(size_bytes):
    units = [' B', 'KB', 'MB', 'GB']
    unit_index = 0
    while size_bytes >= 1024 and unit_index < 3:
        size_bytes /= 1024
        unit_index += 1
    return f"{size_bytes:.2f} {units[unit_index]}"

def ls(path):
    full_path = os.path.abspath(path)
    print(f"\n\nDirectory: {full_path}\n\n")

    items = []
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
            items.append((last_write_time, type, size, item))
        except Exception as e:
            print(f"Error accessing {item}: {e}")

    # Calculate maximum lengths for each column
    max_last_write_time = max(len(item[0]) for item in items) if items else len("LastWriteTime")
    max_type_length = max(len(item[1]) for item in items) if items else len("Type")
    max_size_length = max(len(format_size(item[2])) for item in items) if items else len("Size")
    max_name_length = max(len(item[3]) for item in items) if items else len("Name")

    # Ensure header length is considered
    max_last_write_time = max(max_last_write_time, len("LastWriteTime"))
    max_type_length = max(max_type_length, len("Type"))
    max_size_length = max(max_size_length, len("Size"))
    max_name_length = max(max_name_length, len("Name"))

    print(f"{'LastWriteTime':<{max_last_write_time}}  {'Type':<{max_type_length}}  {'Size':>{max_size_length}}  {'Name'}")
    print(f"{'-------------':<{max_last_write_time}}  {'----':<{max_type_length}}  {'----':>{max_size_length}}  {'----'}")

    for last_write_time, type, size, item in items:
        print(f"{last_write_time:<{max_last_write_time}}  {type:<{max_type_length}}  {format_size(size):>{max_size_length}}  {item}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        folder_path = sys.argv[1]
    else:
        folder_path = "."
    ls(folder_path)
