import re
import tempfile
from pathlib import Path

from typer.testing import CliRunner

from file_whisperer.cli import app
from file_whisperer.paths import get_config_dir, get_data_dir

runner = CliRunner(mix_stderr=False)


def strip_ansi(text: str) -> str:
    """Strips ANSI escape codes from a string."""
    ansi_escape = re.compile(r"\x1b\[[0-9;]*m")
    return ansi_escape.sub("", text)


def test_app_help() -> None:
    """Test that running the app with no arguments shows help."""
    result = runner.invoke(app, [])
    assert result.exit_code == 0
    assert "Usage: file-whisperer [OPTIONS] COMMAND [ARGS]..." in strip_ansi(result.stdout)
    assert "🤫 File-Whisperer: Your AI-powered file organization assistant." in strip_ansi(result.stdout)


def test_app_explicit_help() -> None:
    """Test that running the app with --help shows help."""
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "Usage: file-whisperer [OPTIONS] COMMAND [ARGS]..." in strip_ansi(result.stdout)
    assert "🤫 File-Whisperer: Your AI-powered file organization assistant." in strip_ansi(result.stdout)


def test_scan_command() -> None:
    """Test the scan command."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a dummy file to ensure the loop is entered
        dummy_file = Path(tmpdir) / "dummy.txt"
        dummy_file.touch()

        result = runner.invoke(app, ["scan", tmpdir])
        assert result.exit_code == 0
        assert f"Scanning directory: {tmpdir}" in strip_ansi(result.stdout)
        assert f"- {dummy_file}" in strip_ansi(result.stdout)


def test_organize_command() -> None:
    """Test the organize command."""
    result = runner.invoke(app, ["organize"])
    assert result.exit_code == 0
    assert "Generating organization recommendations..." in strip_ansi(result.stdout)


def test_review_command() -> None:
    """Test the review command."""
    result = runner.invoke(app, ["review"])
    assert result.exit_code == 0
    assert "Reviewing organization recommendations..." in strip_ansi(result.stdout)


def test_apply_command() -> None:
    """Test the apply command."""
    result = runner.invoke(app, ["apply"])
    assert result.exit_code == 0
    assert "Applying organization recommendations..." in strip_ansi(result.stdout)


def test_learn_command() -> None:
    """Test the learn command."""
    result = runner.invoke(app, ["learn"])
    assert result.exit_code == 0
    assert "Updating AI understanding..." in strip_ansi(result.stdout)


def test_config_command() -> None:
    """Test the config command."""
    result = runner.invoke(app, ["config"])
    assert result.exit_code == 0
    assert "Managing settings and preferences..." in strip_ansi(result.stdout)
    assert f"Config directory: {get_config_dir()}" in strip_ansi(result.stdout)
    assert f"Data directory: {get_data_dir()}" in strip_ansi(result.stdout)
