[![Release](https://img.shields.io/github/v/release/zeeshansayyed/file-whisperer)](https://img.shields.io/github/v/release/zeeshansayyed/file-whisperer)
[![Build status](https://img.shields.io/github/actions/workflow/status/zeeshansayyed/file-whisperer/main.yml?branch=main)](https://github.com/zeeshansayyed/file-whisperer/actions/workflows/main.yml?query=branch%3Amain)
[![codecov](https://codecov.io/gh/zeeshansayyed/file-whisperer/branch/main/graph/badge.svg)](https://codecov.io/gh/zeeshansayyed/file-whisperer)
[![Commit activity](https://img.shields.io/github/commit-activity/m/zeeshansayyed/file-whisperer)](https://img.shields.io/github/commit-activity/m/zeeshansayyed/file-whisperer)
[![License](https://img.shields.io/github/license/zeeshansayyed/file-whisperer)](https://img.shields.io/github/license/zeeshansayyed/file-whisperer)

- **Documentation** <https://zeeshansayyed.github.io/file-whisperer/>

# 🤫 File-Whisperer: AI-Powered File Organization

**(Because your file manager shouldn't look like a digital tornado hit it)**

---

👋 **Tired of digital chaos?** Got thousands of files scattered across your computer with names like `IMG_20240315_143022.jpg`, `document (1).pdf`, and `Untitled-final-FINAL-v2.docx`? We feel your pain! **File-Whisperer** is here to bring AI-powered sanity to your file organization.

**The Problem:**

Let's be honest: we're all guilty of it. Downloads folders that look like digital graveyards, desktop screenshots everywhere, and documents with names that made sense at 2 AM but are complete mysteries now. Manual file organization is tedious, time-consuming, and let's face it – we never get around to it.

## **Our Solution: AI That Actually Gets Your Files**

**File-Whisperer** is a command-line tool that uses Large Language Models (LLMs) to intelligently organize your local files. It doesn't just move files randomly – it **understands context**, **respects your privacy**, and **learns your preferences** over time.

Think of it as having a super-smart digital assistant who actually understands what `Screenshot 2024-07-04 at 10.20.15 AM.png` should be called and where it belongs.

## **✨ How It Works**

File-Whisperer follows a simple, transparent workflow that keeps you in control:

```bash
file-whisperer scan /path/to/messy/folder     # Analyze your files
file-whisperer organize                       # Get AI recommendations
file-whisperer review                         # Approve/reject suggestions
file-whisperer apply                          # Execute approved changes
```

### **🧠 Smart AI Decision Making**

For each file, our AI can:

1. **📋 Direct Recommendation**: "This looks like a bank statement from March 2024 → `Documents/Finance/2024/Bank_Statement_March_2024.pdf`"

2. **🔍 Content Analysis Request**: "I need to read the file contents to properly categorize this document. May I?"

3. **❓ Smart Questioning**: For sensitive files or unclear cases, it asks targeted questions:
   - "What type of document is this?"
   - "What project or category does this relate to?"
   - "When was this created or relevant?"

## **🚀 Key Features**

### **Privacy-First Approach**

- **You control content access**: AI only reads files with your explicit permission
- **Sensitive file detection**: Automatically flags files with keywords like "passport", "visa", "tax"
- **Local processing**: Your files never leave your machine unnecessarily

### **Smart Memory System**

- **File fingerprinting**: Remembers every file it's organized using content hashes
- **Duplicate detection**: "Hey, I've seen this file before!"
- **Zero redundant work**: Never processes the same file twice

### **Learning & Adaptation**

- **Interaction logging**: Tracks what you approve/reject to learn your preferences
- **Evolving intelligence**: Periodically updates its understanding based on your patterns
- **Personalized suggestions**: Gets better at predicting your organization style over time

### **Human-in-the-Loop Design**

- **Review before action**: Nothing happens without your approval
- **Transparent reasoning**: See why the AI made each suggestion
- **Granular control**: Approve/reject individual recommendations

## **📋 Commands**

| Command    | Description                                          |
| ---------- | ---------------------------------------------------- |
| `scan`     | Analyze files and collect metadata                   |
| `organize` | Generate AI-powered organization recommendations     |
| `review`   | Interactive approval process for suggestions         |
| `apply`    | Execute approved file moves and renames              |
| `learn`    | Update AI understanding based on interaction history |
| `config`   | Manage settings and preferences                      |

## **🛠️ Installation**

```bash
# Install from PyPI (coming soon!)
pip install file-whisperer

# Or install from source
git clone https://github.com/zeeshansayyed/file-whisperer.git
cd file-whisperer
uv sync
```

## **🚀 Quick Start**

```bash
# Point File-Whisperer at your messy folder
file-whisperer scan ~/Downloads

# Get AI recommendations
file-whisperer organize

# Review and approve suggestions
file-whisperer review

# Apply approved changes
file-whisperer apply
```

## **🏗️ Architecture**

File-Whisperer is built with a clean, modular architecture:

- **`scanner`**: File discovery and metadata extraction
- **`organizer`**: LLM integration and recommendation generation
- **`reviewer`**: Interactive approval interface
- **`executor`**: Safe file operations with rollback capability
- **`memory`**: File indexing and interaction logging
- **`config`**: Settings and preference management

## **🛠️ Tech Stack**

- **Python 3.9+**: Modern Python with type hints
- **LLM Integration**: OpenAI GPT, Anthropic Claude, or local models
- **CLI Framework**: Rich terminal interface with progress bars
- **File Operations**: Safe, atomic file moves with backup
- **Storage**: SQLite for file indexing and interaction history

## **🗺️ Roadmap**

### **v1.0 - Core Intelligence**

- 🚧 Basic file scanning and metadata extraction
- 🚧 LLM-powered organization recommendations
- 🚧 Interactive review process
- 🚧 Safe file operations with rollback

### **v1.1 - Enhanced Learning**

- 🔄 Advanced preference learning
- 🔄 Custom organization templates
- 🔄 Batch processing for similar files

### **v2.0 - Cloud Integration**

- 🔮 Direct cloud drive organization
- 🔮 Cross-platform file sync
- 🔮 Team/shared organization patterns

## **🌱 Contributing**

We use [uv](https://docs.astral.sh/uv/) for dependency management:

```bash
# Clone and setup
git clone https://github.com/zeeshansayyed/file-whisperer.git
cd file-whisperer
uv sync

# Run tests
uv run pytest

# Format code
uv run ruff format

# Type checking
uv run mypy .
```

## **📄 License**

MIT License - see [LICENSE](LICENSE) for details.

---

**🌱 Contributing (Future is Bright!)**

<details>
    <summary>**Ready to whisper your files into perfect organization?** 🗂️✨</summary>

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

## </details>

Repository initiated with [fpgmaas/cookiecutter-uv](https://github.com/fpgmaas/cookiecutter-uv).
