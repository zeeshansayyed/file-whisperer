[![Release](https://img.shields.io/github/v/release/zeeshansayyed/file-whisperer)](https://img.shields.io/github/v/release/zeeshansayyed/file-whisperer)
[![Build status](https://img.shields.io/github/actions/workflow/status/zeeshansayyed/file-whisperer/main.yml?branch=main)](https://github.com/zeeshansayyed/file-whisperer/actions/workflows/main.yml?query=branch%3Amain)
[![codecov](https://codecov.io/gh/zeeshansayyed/file-whisperer/branch/main/graph/badge.svg)](https://codecov.io/gh/zeeshansayyed/file-whisperer)
[![Commit activity](https://img.shields.io/github/commit-activity/m/zeeshansayyed/file-whisperer)](https://img.shields.io/github/commit-activity/m/zeeshansayyed/file-whisperer)
[![License](https://img.shields.io/github/license/zeeshansayyed/file-whisperer)](https://img.shields.io/github/license/zeeshansayyed/file-whisperer)

- **Documentation** <https://zeeshansayyed.github.io/file-whisperer/>

# 🤫 File-Whisperer: Command Your Clouds from the Terminal

**(Because navigating online drives shouldn't feel like shouting into the void)**

---

👋 Hey there! Ever felt like wrangling files across different online drives (Google Drive, OneDrive, you name it) and your local computer is a bit... clunky? Like trying to herd digital cats? We're building **File-Whisperer** to change that!

**The Problem:**

Let's face it: web interfaces for cloud drives are great for a quick peek, but when you're doing serious file management – moving mountains of data, organizing folders like a digital Marie Kondo, or just wanting the pure, unadulterated power of command-line efficiency – they fall short. And switching between drives in different browser tabs? _Ugh._ It's time to bring the terminal to the cloud!

**Our Solution: File-Whisperer to the Rescue!**

Imagine a world where you can command your online drives (and your local files too!) with the familiar power of your terminal. Think `ls`, `cd`, `cp`, `mv`, `mkdir`, `rmdir` – all working seamlessly across your Google Drive, OneDrive, and your local file system. That's **File-Whisperer**!

We're crafting a Python-based terminal application that gives you a unified command interface to manage files, no matter where they live. Think of it as your personal "command center" for all your digital belongings. No more clicking through endless folders in web browsers!

**✨ Key Features (in progress, but aiming for awesome!):**

- **Drive Mounting (Local & Remote):** Think of it like mounting a USB drive, but for your clouds! Effortlessly connect local directories and your online drives (starting with Google Drive and OneDrive, with more to come!). Use drive letters like `L1:`, `G1:` to switch drives as easily as navigating your local system. It's like giving your cloud drives a VIP pass to your terminal.
- **Familiar Terminal Commands:** Use commands you already know and love: `ls`, `cd`, `cp`, `mv`, `mkdir`, `rmdir`. We're making cloud file management feel like home. No need to learn a new language – your existing terminal skills are your superpower!
- **Intelligent Pathing:** Navigate seamlessly between local and remote drives with intuitive pathing. Think `G1:~/Documents` to jump to your Google Drive documents, or `cp L1:/MyLocalFile G2:~/CloudBackup`. We're making "global" file operations a breeze. It's like having a GPS for your files, no matter where they live.
- **Speedy Shortcuts:**
  - **Numbered Aliases in `ls`:** `ls` output gets a smart makeover! Directories and files get numbered, so you can `cd 1` instead of typing out long names. Boom! Efficiency. It's like speed dial for your file system.
  - **Implicit `cd`:** Just type a path (local or cloud), hit Enter, and BAM! You're there. No need to type `cd` every time. It's like teleportation for your terminal.
  - **File Opening:** Type the name (or number alias) of a file and press Enter - we'll try to open it for you! (Maybe even download and open remote files locally). It's like having a personal butler who anticipates your every file-opening need.

**🏗️ Under the Hood (A Peek at the Design):**

We're building File-Whisperer with a modular design in Python, making it robust and extensible:

- **`drives` Module:** This is the engine room! It handles the nitty-gritty of interacting with different types of drives (local, Google Drive, OneDrive, etc.). It uses an abstract `Drive` class with concrete implementations for `LocalDrive` and `RemoteDrive`, giving us a unified interface.
- **`commands` Module:** The command center! It parses user commands (like `ls`, `cd`) and orchestrates actions by talking to the `DriveManager`. It also handles cool shortcuts like aliases.
- **`ui` Module:** The face of File-Whisperer! Built with `prompt_toolkit`, it provides a slick, interactive terminal interface with tab completion, smart prompts, and potentially even some snazzy styling.
- **`config` Module:** The memory bank! Manages configuration settings, like remembering added drives and user preferences (if we get fancy!).
- **`auth` Module:** The gatekeeper! Handles authentication with remote drive services (OAuth and API key magic will live here).

**(See the `docs/uml_diagram.png` – _coming soon!_ - for a UML class diagram visual if you're into blueprints)**

**🛠️ Tech Stack:**

- **Python:** Because it's awesome for scripting, has great libraries, and we love it!
- **`prompt_toolkit`:** For building a beautiful and powerful command-line interface.

**🗺️ Future Roadmap (Just the Beginning!):**

- **More Cloud Services:** Expand to support other cloud providers.
- **File Opening Functionality:** Make "open" command truly open files (download and open locally or stream).
- **More Commands:** `rm`, `du`, `tree`, search, maybe even file editing...? Sky's the limit!
- **Configuration Persistence:** Save added drives and settings across sessions.
- **Robust Error Handling and User Feedback:** Make it user-friendly and error-proof.
- **And ofcourse, a sprinkle of AI**: Think automatic renaming of files, tagging, filing, etc based on the files content.
- **...and your amazing ideas!**

**🌱 Contributing (Future is Bright!)**

We use [uv](https://docs.astral.sh/uv/) for managing Python environments. You have two main options for setting up your development environment: using Docker or installing uv directly.

**Option 1: Docker (Recommended for Isolation)**

1.  **Build the Docker container:**
    ```bash
    make docker
    ```
2.  **Open an interactive terminal inside the container:**
    ```bash
    make docker-shell
    ```
    This gives you a consistent and isolated environment with all dependencies pre-installed.

**Option 2: Local uv Installation (If You Prefer Native Setup)**

1.  **Install uv:**
    For MacOS or Linux, you can install uv as follows:
    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```
2.  **Use Make commands:**
    After installing uv, you can use the `make` commands such as `make install`, `make test`, `make build`, etc., to manage your environment.

---

Repository initiated with [fpgmaas/cookiecutter-uv](https://github.com/fpgmaas/cookiecutter-uv).
