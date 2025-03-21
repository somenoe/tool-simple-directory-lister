import os
import datetime
import sys
import argparse

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

def process_item(path, item):
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
        return (last_write_time, type, size, item)
    except Exception as e:
        print(f"Error accessing {item}: {e}")
        return None

def sort_items(items, sort_by):
    if sort_by == 'Date':
        items.sort(key=lambda x: x[0])
    elif sort_by == 'Type':
        items.sort(key=lambda x: x[1])
    elif sort_by == 'Size':
        items.sort(key=lambda x: x[2])
    elif sort_by == 'Name':
        items.sort(key=lambda x: x[3])

def ls(path, sort_by=None):
    try:
        full_path = os.path.abspath(path)
        print(f"\n\nDirectory: {full_path}\n\n")

        items = []
        for item in os.listdir(path):
            processed_item = process_item(path, item)
            if processed_item:
                items.append(processed_item)

        sort_items(items, sort_by)

        max_last_write_time = max(len(item[0]) for item in items) if items else len("Date Modified")
        max_type_length = max(len(item[1]) for item in items) if items else len("Type")
        max_size_length = max(len(format_size(item[2])) for item in items) if items else len("Size")
        max_name_length = max(len(item[3]) for item in items) if items else len("Name")

        max_last_write_time = max(max_last_write_time, len("Date Modified"))
        max_type_length = max(max_type_length, len("Type"))
        max_size_length = max(max_size_length, len("Size"))
        max_name_length = max(max_name_length, len("Name"))

        print(f"{'Date Modified':<{max_last_write_time}}  {'Type':<{max_type_length}}  {'Size':>{max_size_length}}  {'Name'}")
        print(f"{'-------------':<{max_last_write_time}}  {'----':<{max_type_length}}  {'----':>{max_size_length}}  {'----'}")

        for last_write_time, type, size, item in items:
            print(f"{last_write_time:<{max_last_write_time}}  {type:<{max_type_length}}  {format_size(size):>{max_size_length}}  {item}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except OSError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="List directory contents with sorting options.")
    parser.add_argument("path", nargs="?", default=".", help="Path to the directory (default: current directory)")
    parser.add_argument("-s", "--sort", choices=['Date', 'Type', 'Size', 'Name'], help="Sort by column")

    args = parser.parse_args()

    if not os.path.exists(args.path):
        print(f"Error: Directory not found: {args.path}")
        sys.exit(1)

    if args.sort is not None and args.sort not in ['Date', 'Type', 'Size', 'Name']:
        print(f"Error: Invalid sort option: {args.sort}")
        sys.exit(1)

    ls(args.path, args.sort)
