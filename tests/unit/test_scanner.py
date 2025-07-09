import tempfile
from pathlib import Path

from file_whisperer.scanner import scan_directory


def test_scan_directory_empty() -> None:
    """Test scanning an empty directory."""
    with tempfile.TemporaryDirectory() as tmpdir:
        path = Path(tmpdir)
        files = scan_directory(path)
        assert len(files) == 0


def test_scan_directory_single_file() -> None:
    """Test scanning a directory with a single file."""
    with tempfile.TemporaryDirectory() as tmpdir:
        path = Path(tmpdir)
        (path / "test.txt").touch()
        files = scan_directory(path)
        assert len(files) == 1
        assert files[0].name == "test.txt"


def test_scan_directory_multiple_files() -> None:
    """Test scanning a directory with multiple files."""
    with tempfile.TemporaryDirectory() as tmpdir:
        path = Path(tmpdir)
        (path / "test1.txt").touch()
        (path / "test2.txt").touch()
        files = scan_directory(path)
        assert len(files) == 2
        assert {f.name for f in files} == {"test1.txt", "test2.txt"}


def test_scan_directory_nested_files() -> None:
    """Test scanning a directory with nested files."""
    with tempfile.TemporaryDirectory() as tmpdir:
        path = Path(tmpdir)
        (path / "dir1").mkdir()
        (path / "dir1" / "test1.txt").touch()
        (path / "dir2").mkdir()
        (path / "dir2" / "test2.txt").touch()
        files = scan_directory(path)
        assert len(files) == 2
        assert {f.name for f in files} == {"test1.txt", "test2.txt"}


def test_scan_directory_mixed_content() -> None:
    """Test scanning a directory with mixed files and subdirectories."""
    with tempfile.TemporaryDirectory() as tmpdir:
        path = Path(tmpdir)
        (path / "file1.txt").touch()
        (path / "subdir1").mkdir()
        (path / "subdir1" / "file2.txt").touch()
        (path / "subdir2").mkdir()
        (path / "subdir2" / "file3.txt").touch()
        (path / "subdir2" / "nested_dir").mkdir()
        (path / "subdir2" / "nested_dir" / "file4.txt").touch()
        files = scan_directory(path)
        assert len(files) == 4
        assert {f.name for f in files} == {"file1.txt", "file2.txt", "file3.txt", "file4.txt"}
