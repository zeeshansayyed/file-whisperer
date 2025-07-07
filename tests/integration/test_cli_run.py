import subprocess


def test_main_function_execution() -> None:
    """Test that running cli.py directly executes the app and shows help."""
    result = subprocess.run(
        ["python", "src/file_whisperer/cli.py"],
        capture_output=True,
        text=True,
        cwd="/home/shahensha/Development/file-whisperer",
    )
    assert result.returncode == 0
    assert "Usage: cli.py [OPTIONS] COMMAND [ARGS]..." in result.stdout
    assert "🤫 File-Whisperer: Your AI-powered file organization assistant." in result.stdout
