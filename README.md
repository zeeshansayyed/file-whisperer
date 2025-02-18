# file-whisperer

This application will help you organize and your local computer.

<summary>Badges</summary>

[![Release](https://img.shields.io/github/v/release/zeeshansayyed/file-whisperer)](https://img.shields.io/github/v/release/zeeshansayyed/file-whisperer)
[![Build status](https://img.shields.io/github/actions/workflow/status/zeeshansayyed/file-whisperer/main.yml?branch=main)](https://github.com/zeeshansayyed/file-whisperer/actions/workflows/main.yml?query=branch%3Amain)
[![codecov](https://codecov.io/gh/zeeshansayyed/file-whisperer/branch/main/graph/badge.svg)](https://codecov.io/gh/zeeshansayyed/file-whisperer)
[![Commit activity](https://img.shields.io/github/commit-activity/m/zeeshansayyed/file-whisperer)](https://img.shields.io/github/commit-activity/m/zeeshansayyed/file-whisperer)
[![License](https://img.shields.io/github/license/zeeshansayyed/file-whisperer)](https://img.shields.io/github/license/zeeshansayyed/file-whisperer)

- **Github repository**: <https://github.com/zeeshansayyed/file-whisperer/>
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

- **Drive Mounting (Local & Remote):** Effortlessly "mount" local directories and connect to your online drives (starting with Google Drive and OneDrive, with more to come!). We're talking drive letters like `L1:`, `G1:` to switch drives as easily as navigating your local system.
- **Familiar Terminal Commands:** Use commands you already know and love: `ls`, `cd`, `cp`, `mv`, `mkdir`, `rmdir`. We're making cloud file management feel like home.
- **Intelligent Pathing:** Navigate seamlessly between local and remote drives with intuitive pathing. Think `G1:~/Documents` to jump to your Google Drive documents, or `cp L1:/MyLocalFile G2:~/CloudBackup`. We're making "global" file operations a breeze.
- **Speedy Shortcuts:**
  - **Numbered Aliases in `ls`:** `ls` output gets a smart makeover! Directories and files get numbered, so you can `cd 1` instead of typing out long names. Boom! Efficiency.
  - **Implicit `cd`:** Just type a path (local or cloud), hit Enter, and BAM! You're there. No need to type `cd` every time.
  - **File Opening:** Type the name (or number alias) of a file and press Enter - we'll try to open it for you! (Maybe even download and open remote files locally).
- **Tab Completion on Steroids:** Smart tab completion that understands local paths, drive-level paths, and even global paths spanning different drives. We're minimizing typing and maximizing speed.

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

(We'll flesh this out as the project matures) - But ideas, feedback, and contributions will be very welcome as we move forward!

---

<details>
<summary>Setup Instructions from CC</summary>

## Getting started with your project

### 1. Create a New Repository

First, create a repository on GitHub with the same name as this project, and then run the following commands:

```bash
git init -b main
git add .
git commit -m "init commit"
git remote add origin git@github.com:zeeshansayyed/file-whisperer.git
git push -u origin main
```

### 2. Set Up Your Development Environment

Then, install the environment and the pre-commit hooks with

```bash
make install
```

This will also generate your `uv.lock` file

### 3. Run the pre-commit hooks

Initially, the CI/CD pipeline might be failing due to formatting issues. To resolve those run:

```bash
uv run pre-commit run -a
```

### 4. Commit the changes

Lastly, commit the changes made by the two steps above to your repository.

```bash
git add .
git commit -m 'Fix formatting issues'
git push origin main
```

You are now ready to start development on your project!
The CI/CD pipeline will be triggered when you open a pull request, merge to main, or when you create a new release.

To finalize the set-up for publishing to PyPI, see [here](https://fpgmaas.github.io/cookiecutter-uv/features/publishing/#set-up-for-pypi).
For activating the automatic documentation with MkDocs, see [here](https://fpgmaas.github.io/cookiecutter-uv/features/mkdocs/#enabling-the-documentation-on-github).
To enable the code coverage reports, see [here](https://fpgmaas.github.io/cookiecutter-uv/features/codecov/).

## Releasing a new version

- Create an API Token on [PyPI](https://pypi.org/).
- Add the API Token to your projects secrets with the name `PYPI_TOKEN` by visiting [this page](https://github.com/zeeshansayyed/file-whisperer/settings/secrets/actions/new).
- Create a [new release](https://github.com/zeeshansayyed/file-whisperer/releases/new) on Github.
- Create a new tag in the form `*.*.*`.

For more details, see [here](https://fpgmaas.github.io/cookiecutter-uv/features/cicd/#how-to-trigger-a-release).

---

Repository initiated with [fpgmaas/cookiecutter-uv](https://github.com/fpgmaas/cookiecutter-uv).

</details>
