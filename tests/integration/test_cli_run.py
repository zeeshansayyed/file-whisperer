import re
import subprocess


def strip_ansi(text: str) -> str:
    """Strips ANSI escape codes from a string."""
    ansi_escape = re.compile(r"\x1b\[[0-9;]*m")
    return ansi_escape.sub("", text)


def test_main_function_execution() -> None:
    """Test that running cli.py directly executes the app and shows help."""
    result = subprocess.run(
        ["python", "src/file_whisperer/cli.py"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "Usage: cli.py [OPTIONS] COMMAND [ARGS]..." in strip_ansi(result.stdout)
    assert "🤫 File-Whisperer: Your AI-powered file organization assistant." in strip_ansi(result.stdout)
