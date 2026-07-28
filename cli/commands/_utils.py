#!/usr/bin/env python3
"""
LOGICAL BRUTALISM :: CLI SHARED UTILITIES
Common functions for all CLI scaffold commands.
Extracted to eliminate duplication across init_django / init_fastapi / etc.

Author: Matheus Lacerda Ferreira
License: MIT
"""

import os
import platform
import shutil
import stat
import subprocess
import sys
import urllib.request

# ---------------------------------------------------------------------------
# CONSTANTS
# ---------------------------------------------------------------------------
TAILWIND_VERSION = "v3.4.19"
TAILWIND_BASE_URL = (
    f"https://github.com/tailwindlabs/tailwindcss/releases/download/{TAILWIND_VERSION}"
)

# ANSI CORE COLORS
C_AMBER = "\033[38;5;214m"
C_ERROR = "\033[38;5;196m"
C_OK = "\033[38;5;82m"
C_DIM = "\033[38;5;242m"
C_VOID = "\033[0m"


# ---------------------------------------------------------------------------
# LOGGING
# ---------------------------------------------------------------------------
def log(step, msg):
    """Structured step log output."""
    print(f" {C_AMBER}[{step}]{C_VOID} {msg}")


def ok(msg):
    """Success confirmation."""
    print(f" {C_OK}[+]{C_VOID} {msg}")


def err(msg):
    """Error log and hard exit."""
    print(f"\n {C_ERROR}[ERROR]{C_VOID} {msg}\n")
    sys.exit(1)


# ---------------------------------------------------------------------------
# SUBPROCESS
# ---------------------------------------------------------------------------
def run(cmd, cwd=None):
    """Execute subprocess with strict error propagation.

    Inherits stdio so the user sees real-time output from uv/django-admin/etc.
    """
    try:
        subprocess.run(cmd, cwd=cwd, check=True)
    except FileNotFoundError:
        err(f"Binary not found: '{cmd[0]}'. Is it installed and on PATH?")
    except subprocess.CalledProcessError as e:
        err(f"Command failed with exit code {e.returncode}: {' '.join(cmd)}")


# ---------------------------------------------------------------------------
# FILE I/O
# ---------------------------------------------------------------------------
def write_file(path, content):
    """Atomic file write with automatic directory creation."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


# ---------------------------------------------------------------------------
# UV OPERATIONS
# ---------------------------------------------------------------------------
def check_uv():
    """Validate `uv` binary exists on PATH. Hard failure if missing."""
    if shutil.which("uv") is None:
        err(
            "'uv' binary not found.\n"
            "  Logical Brutalism CLI requires 'uv' for high-performance scaffolding.\n"
            "  Install it before proceeding: curl -LsSf https://astral.sh/uv/install.sh | sh"
        )


def cleanup_uv_scaffolding(project_dir):
    """Remove auto-generated files from `uv init` that conflict with project structure."""
    for artifact in ["hello.py", "main.py"]:
        artifact_path = os.path.join(project_dir, artifact)
        if os.path.isfile(artifact_path):
            os.remove(artifact_path)

    src_dir = os.path.join(project_dir, "src")
    if os.path.isdir(src_dir):
        shutil.rmtree(src_dir)


def guard_existing_dir(project_dir):
    """Abort if the project directory already exists."""
    if os.path.exists(project_dir):
        err(
            f"Directory already exists: {project_dir}\n"
            f"  Aborting to prevent data loss. Remove it or choose another name."
        )


# ---------------------------------------------------------------------------
# TAILWINDCSS STANDALONE
# ---------------------------------------------------------------------------
def resolve_tailwind_binary():
    """Determine the correct TailwindCSS standalone binary for the host OS/arch.

    Returns:
        tuple: (download_url, local_binary_name)
    """
    system = platform.system()
    machine = platform.machine().lower()

    os_map = {"Linux": "linux", "Darwin": "macos", "Windows": "windows"}
    arch_map = {
        "x86_64": "x64",
        "amd64": "x64",
        "aarch64": "arm64",
        "arm64": "arm64",
    }

    os_key = os_map.get(system)
    arch_key = arch_map.get(machine)

    if not os_key or not arch_key:
        err(
            f"Unsupported platform: {system}/{machine}.\n"
            f"  TailwindCSS Standalone CLI supports: Linux/macOS/Windows on x64/arm64."
        )

    ext = ".exe" if system == "Windows" else ""
    binary_name = f"tailwindcss-{os_key}-{arch_key}{ext}"
    local_name = f"tailwindcss{ext}"
    url = f"{TAILWIND_BASE_URL}/{binary_name}"

    return url, local_name


def download_tailwind(url, dest_path):
    """Download TailwindCSS standalone binary with progress feedback."""
    try:
        def _report(block_num, block_size, total_size):
            if total_size > 0:
                downloaded = block_num * block_size
                pct = min(100, int(downloaded * 100 / total_size))
                mb_down = downloaded / (1024 * 1024)
                mb_total = total_size / (1024 * 1024)
                print(
                    f"\r {C_DIM}    [{pct:3d}%] {mb_down:.1f}/{mb_total:.1f} MB{C_VOID}",
                    end="",
                    flush=True,
                )

        urllib.request.urlretrieve(url, dest_path, reporthook=_report)
        print()  # Newline after progress bar

        # Set executable permission on Unix
        if platform.system() != "Windows":
            st = os.stat(dest_path)
            os.chmod(
                dest_path,
                st.st_mode | stat.S_IEXEC | stat.S_IXGRP | stat.S_IXOTH,
            )
    except Exception as e:
        err(f"Failed to download TailwindCSS standalone binary.\n  URL: {url}\n  Error: {e}")


# ---------------------------------------------------------------------------
# GITIGNORE
# ---------------------------------------------------------------------------
def append_gitignore_tailwind(project_dir):
    """Append TailwindCSS binary and output exclusions to .gitignore."""
    gitignore_path = os.path.join(project_dir, ".gitignore")
    entries = (
        "\n# Logical Brutalism :: TailwindCSS Standalone Binary\n"
        "tailwindcss\n"
        "tailwindcss.exe\n"
        "\n# Tailwind compiled output\n"
        "static/css/output.css\n"
    )
    try:
        with open(gitignore_path, "a", encoding="utf-8") as f:
            f.write(entries)
        ok(".gitignore updated :: tailwindcss binary excluded")
    except Exception:
        pass  # Non-critical


# ---------------------------------------------------------------------------
# DEPLOYMENT SUMMARY
# ---------------------------------------------------------------------------
def print_summary(project_name, local_tw_name, run_cmd):
    """Print the final deployment summary block."""
    print(f"\n {C_AMBER}{'=' * 64}{C_VOID}")
    print(f" {C_AMBER}[DEPLOYMENT COMPLETE]{C_VOID}")
    print(f" {C_AMBER}{'=' * 64}{C_VOID}\n")
    print(f" {C_DIM}Project:{C_VOID}    {project_name}/")
    print(f" {C_DIM}Tailwind:{C_VOID}   ./{local_tw_name} -i static/css/input.css -o static/css/output.css")
    print(f" {C_DIM}Server:{C_VOID}     {run_cmd}\n")
    print(f" {C_AMBER}[>]{C_VOID} WHAT DOES NOT RESOLVE, DOES NOT EXIST.\n")
