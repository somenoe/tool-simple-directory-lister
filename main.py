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

def ls(path):
    print(f"\n\n    Directory: {path}\n\n")
    print(f"{'Mode':<10} {'LastWriteTime':<20} {'Length':<10} {'Name'}")
    print(f"{'----':<10} {'-------------':<20} {'------':<10} {'----'}")

    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        try:
            stat_info = os.stat(full_path)
            mode = "d-----" if os.path.isdir(full_path) else "-a----"
            last_write_time = datetime.datetime.fromtimestamp(stat_info.st_mtime).strftime('%m/%d/%Y %I:%M %p')
            length = stat_info.st_size
            if os.path.isdir(full_path):
                length = get_folder_size(full_path)
            print(f"{mode:<10} {last_write_time:<20} {length:<10} {item}")
        except Exception as e:
            print(f"Error accessing {item}: {e}")

if __name__ == "__main__":
    TEST_FOLDER_PATH = r"C:\\Users\\otash\\Documents"
    ls(TEST_FOLDER_PATH)
