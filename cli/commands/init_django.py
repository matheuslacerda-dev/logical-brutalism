#!/usr/bin/env python3
"""
LOGICAL BRUTALISM :: INIT DJANGO COMMAND
Deterministic pipeline to scaffold a Django project under LB governance.

Pipeline:
  [00] Validate `uv` binary on PATH
  [01] Initialize project with `uv init`
  [02] Install dependencies: django, django-htmx
  [03] Scaffold Django project (config module)
  [04] Patch config/settings.py
  [05] Download TailwindCSS Standalone CLI (v3.4.x)
  [06] Generate LB file structure
  [07] Finalize and print deployment summary

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

from cli.payloads.base_html import BASE_HTML
from cli.payloads.tailwind_config import TAILWIND_CONFIG
from cli.payloads.input_css import INPUT_CSS

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
# INTERNAL UTILITIES
# ---------------------------------------------------------------------------
def _log(step, msg):
    """Structured step log output."""
    print(f" {C_AMBER}[{step}]{C_VOID} {msg}")


def _ok(msg):
    """Success confirmation."""
    print(f" {C_OK}[+]{C_VOID} {msg}")


def _err(msg):
    """Error log and hard exit."""
    print(f"\n {C_ERROR}[ERROR]{C_VOID} {msg}\n")
    sys.exit(1)


def _run(cmd, cwd=None):
    """Execute subprocess with strict error propagation.

    Inherits stdio so the user sees real-time output from uv/django-admin.
    """
    try:
        subprocess.run(cmd, cwd=cwd, check=True)
    except FileNotFoundError:
        _err(f"Binary not found: '{cmd[0]}'. Is it installed and on PATH?")
    except subprocess.CalledProcessError as e:
        _err(f"Command failed with exit code {e.returncode}: {' '.join(cmd)}")


def _write_file(path, content):
    """Atomic file write with automatic directory creation."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


# ---------------------------------------------------------------------------
# PIPELINE STEPS
# ---------------------------------------------------------------------------
def _check_uv():
    """Step 00: Validate `uv` binary exists on PATH."""
    if shutil.which("uv") is None:
        _err(
            "'uv' binary not found.\n"
            "  Logical Brutalism CLI requires 'uv' for high-performance scaffolding.\n"
            "  Install it before proceeding: curl -LsSf https://astral.sh/uv/install.sh | sh"
        )


def _resolve_tailwind_binary():
    """Determine the correct TailwindCSS standalone binary for the host OS/arch.

    Returns:
        tuple: (download_url, local_binary_name)
    """
    system = platform.system()
    machine = platform.machine().lower()

    os_map = {
        "Linux": "linux",
        "Darwin": "macos",
        "Windows": "windows",
    }
    # Normalize architecture identifiers across platforms
    arch_map = {
        "x86_64": "x64",
        "amd64": "x64",
        "aarch64": "arm64",
        "arm64": "arm64",
    }

    os_key = os_map.get(system)
    arch_key = arch_map.get(machine)

    if not os_key or not arch_key:
        _err(
            f"Unsupported platform: {system}/{machine}.\n"
            f"  TailwindCSS Standalone CLI supports: Linux/macOS/Windows on x64/arm64."
        )

    ext = ".exe" if system == "Windows" else ""
    binary_name = f"tailwindcss-{os_key}-{arch_key}{ext}"
    local_name = f"tailwindcss{ext}"
    url = f"{TAILWIND_BASE_URL}/{binary_name}"

    return url, local_name


def _cleanup_uv_scaffolding(project_dir):
    """Remove auto-generated files from `uv init` that conflict with Django structure."""
    # uv init may create hello.py, main.py, or a src/ directory
    for artifact in ["hello.py", "main.py"]:
        artifact_path = os.path.join(project_dir, artifact)
        if os.path.isfile(artifact_path):
            os.remove(artifact_path)

    src_dir = os.path.join(project_dir, "src")
    if os.path.isdir(src_dir):
        shutil.rmtree(src_dir)


def _patch_settings(settings_path):
    """Programmatically inject LB configuration into Django's generated settings.py.

    Modifications:
      1. INSTALLED_APPS += 'django_htmx'
      2. MIDDLEWARE += 'django_htmx.middleware.HtmxMiddleware'
      3. TEMPLATES DIRS -> [BASE_DIR / 'templates']
      4. STATICFILES_DIRS = [BASE_DIR / 'static']
    """
    with open(settings_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = []
    installed_apps_patched = False
    middleware_patched = False
    staticfiles_patched = False

    for line in lines:
        # 1. Inject django_htmx into INSTALLED_APPS (after staticfiles)
        if "django.contrib.staticfiles" in line and not installed_apps_patched:
            new_lines.append(line)
            new_lines.append("\n")
            new_lines.append("    # -- Logical Brutalism :: HTMX Engine --\n")
            new_lines.append("    'django_htmx',\n")
            installed_apps_patched = True
            continue

        # 2. Inject HtmxMiddleware into MIDDLEWARE (after CommonMiddleware)
        if "django.middleware.common.CommonMiddleware" in line and not middleware_patched:
            new_lines.append(line)
            new_lines.append("    'django_htmx.middleware.HtmxMiddleware',\n")
            middleware_patched = True
            continue

        # 3. Patch TEMPLATES DIRS (handle both quote styles)
        if "'DIRS': []" in line:
            new_lines.append(line.replace("'DIRS': []", "'DIRS': [BASE_DIR / 'templates']"))
            continue
        if '"DIRS": []' in line:
            new_lines.append(line.replace('"DIRS": []', '"DIRS": [BASE_DIR / "templates"]'))
            continue

        # 4. Append STATICFILES_DIRS after STATIC_URL
        if line.strip().startswith("STATIC_URL") and not staticfiles_patched:
            new_lines.append(line)
            new_lines.append("STATICFILES_DIRS = [BASE_DIR / 'static']\n")
            staticfiles_patched = True
            continue

        new_lines.append(line)

    with open(settings_path, "w", encoding="utf-8") as f:
        f.writelines(new_lines)


def _download_tailwind(url, dest_path):
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
        print()  # Newline after progress

        # Set executable permission on Unix
        if platform.system() != "Windows":
            st = os.stat(dest_path)
            os.chmod(
                dest_path,
                st.st_mode | stat.S_IEXEC | stat.S_IXGRP | stat.S_IXOTH,
            )
    except Exception as e:
        _err(f"Failed to download TailwindCSS standalone binary.\n  URL: {url}\n  Error: {e}")


# ---------------------------------------------------------------------------
# MAIN PIPELINE
# ---------------------------------------------------------------------------
def run(project_name):
    """Execute the full `init django` deployment pipeline.

    Args:
        project_name: Name of the Django project directory to create.
    """
    project_dir = os.path.join(os.getcwd(), project_name)

    # Guard: prevent overwriting existing directories
    if os.path.exists(project_dir):
        _err(
            f"Directory already exists: {project_dir}\n"
            f"  Aborting to prevent data loss. Remove it or choose another name."
        )

    # -- Step 00: Validate uv ------------------------------------------------
    _log("00", "Validating uv binary...")
    _check_uv()
    _ok("uv detected on PATH.")

    # -- Step 01: Initialize project with uv ----------------------------------
    _log("01", f"Initializing project: {project_name}")
    _run(["uv", "init", "--no-workspace", project_name])
    _cleanup_uv_scaffolding(project_dir)
    _ok(f"Project directory created :: {project_dir}")

    # -- Step 02: Install Django dependencies ---------------------------------
    _log("02", "Installing dependencies: django, django-htmx")
    _run(["uv", "add", "django", "django-htmx"], cwd=project_dir)
    _ok("Dependencies locked and installed.")

    # -- Step 03: Scaffold Django project -------------------------------------
    _log("03", "Scaffolding Django project (config module)")
    _run(
        ["uv", "run", "django-admin", "startproject", "config", "."],
        cwd=project_dir,
    )
    _ok("Django project generated :: config/")

    # -- Step 04: Patch config/settings.py ------------------------------------
    _log("04", "Patching config/settings.py")
    settings_path = os.path.join(project_dir, "config", "settings.py")

    if not os.path.isfile(settings_path):
        _err(f"settings.py not found at: {settings_path}\n  Django scaffolding may have failed.")

    _patch_settings(settings_path)
    _ok("INSTALLED_APPS += django_htmx")
    _ok("MIDDLEWARE += HtmxMiddleware")
    _ok("TEMPLATES DIRS -> templates/")
    _ok("STATICFILES_DIRS -> static/")

    # -- Step 05: Download TailwindCSS Standalone CLI -------------------------
    _log("05", f"Downloading TailwindCSS Standalone CLI ({TAILWIND_VERSION})")
    url, local_name = _resolve_tailwind_binary()
    tailwind_path = os.path.join(project_dir, local_name)
    _log("05", f"Source: {url}")
    _download_tailwind(url, tailwind_path)
    _ok(f"TailwindCSS binary deployed :: {local_name}")

    # -- Step 06: Generate LB file structure ----------------------------------
    _log("06", "Generating Logical Brutalism file structure")

    css_dir = os.path.join(project_dir, "static", "css")
    js_dir = os.path.join(project_dir, "static", "js")
    templates_dir = os.path.join(project_dir, "templates")

    os.makedirs(css_dir, exist_ok=True)
    os.makedirs(js_dir, exist_ok=True)
    os.makedirs(templates_dir, exist_ok=True)

    # Copy core CSS from package data
    script_dir = os.path.dirname(os.path.abspath(__file__))
    core_css_source = os.path.normpath(
        os.path.join(script_dir, "..", "..", "core", "logical-brutalism.css")
    )

    try:
        shutil.copy2(core_css_source, os.path.join(css_dir, "logical-brutalism.css"))
        _ok("Core CSS matrix injected :: static/css/logical-brutalism.css")
    except FileNotFoundError:
        _err(
            f"Core CSS not found at: {core_css_source}\n"
            f"  Package data may be corrupted. Reinstall logical-brutalism."
        )

    # Write Tailwind input.css
    _write_file(os.path.join(css_dir, "input.css"), INPUT_CSS)
    _ok("Tailwind input directive :: static/css/input.css")

    # Write base.html
    _write_file(os.path.join(templates_dir, "base.html"), BASE_HTML)
    _ok("Root template injected :: templates/base.html")

    # Write tailwind.config.js
    _write_file(os.path.join(project_dir, "tailwind.config.js"), TAILWIND_CONFIG)
    _ok("Tailwind config locked :: tailwind.config.js")

    # -- Step 07: Finalize ----------------------------------------------------
    _log("07", "Finalizing deployment")

    # Update .gitignore with tailwind binary exclusion
    gitignore_path = os.path.join(project_dir, ".gitignore")
    gitignore_append = (
        "\n# Logical Brutalism :: TailwindCSS Standalone Binary\n"
        "tailwindcss\n"
        "tailwindcss.exe\n"
        "\n# Tailwind compiled output\n"
        "static/css/output.css\n"
    )

    try:
        with open(gitignore_path, "a", encoding="utf-8") as f:
            f.write(gitignore_append)
        _ok(".gitignore updated :: tailwindcss binary excluded")
    except Exception:
        pass  # Non-critical: user can add manually

    # -- Deployment Summary ---------------------------------------------------
    print(f"\n {C_AMBER}{'=' * 64}{C_VOID}")
    print(f" {C_AMBER}[DEPLOYMENT COMPLETE]{C_VOID}")
    print(f" {C_AMBER}{'=' * 64}{C_VOID}\n")
    print(f" {C_DIM}Project:{C_VOID}    {project_name}/")
    print(f" {C_DIM}Settings:{C_VOID}   config/settings.py")
    print(f" {C_DIM}Template:{C_VOID}   templates/base.html")
    print(f" {C_DIM}Tailwind:{C_VOID}   ./{local_name} -i static/css/input.css -o static/css/output.css")
    print(f" {C_DIM}Server:{C_VOID}     cd {project_name} && uv run python manage.py runserver\n")
    print(f" {C_AMBER}[>]{C_VOID} WHAT DOES NOT RESOLVE, DOES NOT EXIST.\n")
