import os
import sys
import shutil

def resource_path(relative_path: str) -> str:
    try:
        base_path = sys._MEIPASS  # Extracted temporary path when bundled
    except AttributeError:
        base_path = os.path.abspath(".")  # Normal dev environment

    return os.path.join(base_path, relative_path)


def get_user_data_dir(app_name: str = "LMS") -> str:
    r"""
    Return a writable directory for user-specific data (e.g., database).
    Windows: %LOCALAPPDATA%\LMS
    Linux/Mac: ~/.local/share/LMS
    """
    if os.name == "nt":  # Windows
        base = os.environ.get("LOCALAPPDATA") or os.environ.get("APPDATA")
    else:
        base = os.path.expanduser("~/.local/share")

    folder = os.path.join(base, app_name)
    os.makedirs(folder, exist_ok=True)
    return folder


def ensure_writable_db(default_db_relpath: str = "database/library.db") -> str:
    r"""
    Ensures a writable SQLite DB exists in the user's AppData folder.
    Copies it from bundled resources if not found.
    Returns the full absolute path to the writable DB.
    """
    user_dir = get_user_data_dir()
    db_target = os.path.join(user_dir, "library.db")

    if not os.path.exists(db_target):
        src = resource_path(default_db_relpath)
        shutil.copy(src, db_target)

    return db_target
