import os
import platform
from pathlib import Path


def get_storage_path() -> Path:
    """Get the path to the storage file based on the operating system.

    Returns:
        Path: The path to the storage file.
    Raises:
        RuntimeError: If the storage file cannot be found.
    """
    system = platform.system()

    try:
        if system == "Windows":
            base_path = os.getenv("APPDATA")
        elif system == "Darwin":  # MacOS
            base_path = str(Path.home() / "Library/Application Support")
        else:  # Linux and others
            base_path = str(Path.home() / ".config")

        storage_path = Path(base_path) / "Cursor/User/globalStorage/storage.json"
        return storage_path

    except Exception as e:
        raise RuntimeError(f"Failed to determine storage path: {e}")


def reset_cursor_id():
    try:
        storage_path = get_storage_path()
        print(f"Storage file location: {storage_path}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    reset_cursor_id()
