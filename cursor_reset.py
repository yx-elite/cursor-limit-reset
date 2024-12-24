import os
import platform
import shutil
import json
import uuid
import hashlib
from datetime import datetime
from pathlib import Path


def get_storage_path() -> Path:
    """Get the path to the storage file based on the operating system.

    Returns:
        Path: The path to the storage file.
    Raises:
        RuntimeError: If the storage file cannot be found.
    """
    system = platform.system()
    print(f"Operating System: {system}")
    print("Searching for storage file ......")

    try:
        if system == "Windows":
            base_path = os.getenv("APPDATA")
        elif system == "Darwin":  # MacOS
            base_path = str(Path.home() / "Library/Application Support")
        else:  # Linux and others
            base_path = str(Path.home() / ".config")

        storage_path = Path(base_path) / "Cursor/User/globalStorage/storage.json"
        print(f"Storage file location: {storage_path}")
        return storage_path

    except Exception as e:
        raise RuntimeError(f"Failed to determine storage path: {e}")


def create_timestamp_backup(storage_path: Path) -> None:
    """Create a timestamped backup of the storage file."""
    try:
        backup_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = storage_path.parent / f"storage.json.backup_{backup_timestamp}"
        print(f"Creating backup ......")
        shutil.copy2(storage_path, backup_path)
        print(f"Backup file location: {backup_path}")

    except Exception as e:
        raise RuntimeError(f"Failed to create backup: {e}")


def generate_new_ids() -> dict[str, str]:
    """Generate new unique identifiers for Cursor.

    Returns:
        dict: Dictionary containing the new IDs
    """
    return {
        "telemetry.machineId": hashlib.sha256(str(uuid.uuid4()).encode()).hexdigest(),
        "telemetry.macMachineId": hashlib.sha256(
            str(uuid.uuid4()).encode()
        ).hexdigest(),
        "telemetry.devDeviceId": str(uuid.uuid4()),
        "telemetry.sqmId": f"{{{uuid.uuid4()}}}",
    }


def print_ids(prefix: str, ids: dict[str, str]) -> None:
    """Print the IDs in a formatted way.

    Args:
        prefix: String to prefix the output (e.g., "Current" or "New")
        ids: Dictionary containing the IDs to print
    """
    print(f"\n{prefix} IDs:")
    print("-" * 50)
    for key, value in ids.items():
        id_name = key.split(".")[-1].replace("Id", " ID").title()
        print(f"{id_name:<15} : {value}")
    print("-" * 50)


def reset_cursor_ids(storage_path: Path) -> None:
    """Reset Cursor telemetry IDs with new random values.

    Args:
        storage_path: Path to the storage.json file

    Raises:
        RuntimeError: If there's an error reading or writing the storage file
        json.JSONDecodeError: If the storage file contains invalid JSON
    """
    try:
        # Read current data
        with open(storage_path, "r") as file:
            data = json.load(file)

        # Get current IDs
        current_ids = {
            key: data[key] for key in [
                "telemetry.machineId",
                "telemetry.macMachineId",
                "telemetry.devDeviceId",
                "telemetry.sqmId",
            ]
        }

        print("\nFetching cursor IDs......")
        print_ids("Current", current_ids)

        # Generate and set new IDs
        print("\nResetting cursor IDs......")
        new_ids = generate_new_ids()
        data.update(new_ids)

        # Write updated data
        with open(storage_path, "w") as file:
            json.dump(data, file, indent=2)

        print_ids("New", new_ids)
        print("\nCursor IDs have been reset successfully.")

    except json.JSONDecodeError as e:
        raise RuntimeError(f"Invalid JSON in storage file: {e}")
    except IOError as e:
        raise RuntimeError(f"Error accessing storage file: {e}")
    except KeyError as e:
        raise RuntimeError(f"Missing required key in storage file: {e}")


def main():
    try:
        storage_path = get_storage_path()
        create_timestamp_backup(storage_path)
        reset_cursor_ids(storage_path)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
