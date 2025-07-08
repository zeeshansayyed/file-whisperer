"""Module for managing application paths using platformdirs."""

from pathlib import Path

from platformdirs import user_config_dir, user_data_dir

APP_NAME = "file-whisperer"
APP_AUTHOR = "zeeshansayyed"


def get_data_dir() -> Path:
    """Returns the appropriate user data directory for the application."""
    return Path(user_data_dir(appname=APP_NAME, appauthor=APP_AUTHOR))


def get_config_dir() -> Path:
    """Returns the appropriate user config directory for the application."""
    return Path(user_config_dir(appname=APP_NAME, appauthor=APP_AUTHOR))
