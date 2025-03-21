# Simple Directory Lister

This program lists the files and folders in a directory. You can also sort the list.

## How to Use

1. **Run the program:**

    ```bash
    python main.py [directory] [options]
    ```

    **`directory` (optional):**  The folder you want to list. If you don't write anything, it uses the current folder.

    **`options` (optional):**

    - `-s` or `--sort`: Sort the list. You can sort by:
        - `Name`:  Sort by file/folder name.
        - `Size`:  Sort by file/folder size.
        - `Type`:  Sort by file type (e.g., ".mp4", ".pdf", ".txt", "folder").
        - `Date`:  Sort by the date the file/folder was last changed.

    **Example:**

    - List the files in the current folder:

        ```bash
        python main.py
        ```

    - List the files in the "MyFolder" folder, sorted by name:

        ```bash
        python main.py MyFolder -s Name
        ```

2. **Build the program:**

    ```bash
    build.bat
    ```

## What it Does

The program shows:

- Date Modified: When the file/folder was last changed.
- Type:  "file", "folder", or the file extension (like ".txt").
- Size:  The size of the file/folder (in bytes, KB, MB, or GB).
- Name:  The name of the file or folder.
