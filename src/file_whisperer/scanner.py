"""Module for scanning directories and extracting file metadata."""

import os
from pathlib import Path


def scan_directory(path: Path) -> list[Path]:
    """Scans a directory and returns a list of all file paths within it."""
    file_paths: list[Path] = []
    for root, _, files in os.walk(path):
        for file in files:
            file_paths.append(Path(root) / file)
    return file_paths
