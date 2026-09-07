import shutil
import json
import subprocess
from pathlib import Path

CONFIG_FILE = Path(__file__).parent / "config.json"

def load_config(config_path):
    """Loads extension-to-path mappings from the JSON file."""
    if not config_path.exists():
        return {}
    with open(config_path, "r") as f:
        return json.load(f)

def send_notification(message):
    title = "File Organizer"
    script = f'display notification "{message}" with title "{title}"'
    subprocess.run(["osascript", "-e", script])
    
config = load_config(CONFIG_FILE)
send_notification(config.get("NOTIFICATION_MESSAGES")[0])

def organize_files():


    downloads_path = config.get("PATH_TO_DOWNLOADS")
    if not config:
        send_notification(config.get("NOTIFICATION_MESSAGES")[1])
        return "0"

    # Normalize extensions to lowercase with a leading dot
    mapping = {
        ext.lower() if ext.startswith('.') else f".{ext.lower()}": Path(dest)
        for ext, dest in config.items()
        if ext not in {"PATH_TO_DOWNLOADS", "NOTIFICATION_MESSAGES"}
    }

    for item in Path(downloads_path).iterdir():
        # Skip directories and hidden files
        if item.is_dir() or item.name.startswith('.'):
            continue

        ext = item.suffix.lower()
        if ext in mapping:
            target_dir = mapping[ext]
            
            # Create target folder if it doesn't exist
            target_dir.mkdir(parents=True, exist_ok=True)
            
            target_path = target_dir / item.name

            # Prevent overwriting existing files by appending a counter
            if target_path.exists():
                stem = item.stem
                counter = 1
                while target_path.exists():
                    target_path = target_dir / f"{stem}_{counter}{ext}"
                    counter += 1

            shutil.move(str(item), str(target_path))
            send_notification(f"Moved: {item.name} -> {target_path}")

if __name__ == "__main__":
    while True:
        if organize_files() == "0":
            break