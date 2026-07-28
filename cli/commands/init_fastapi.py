#!/usr/bin/env python3
"""
LOGICAL BRUTALISM :: INIT FASTAPI COMMAND
Deterministic pipeline to scaffold a FastAPI project under LB governance.

Pipeline:
  [00] Validate `uv` binary on PATH
  [01] Initialize project with `uv init`
  [02] Install dependencies: fastapi, uvicorn, jinja2, python-multipart, polars
  [03] Generate opinionated folder structure
  [04] Generate core/config.py
  [05] Generate main.py (FastAPI engine)
  [06] Generate routers/dashboard.py (Polars + HTMX)
  [07] Download TailwindCSS Standalone CLI (v3.4.x)
  [08] Generate templates (base.html, dashboard, partials)
  [09] Inject core CSS + Tailwind input/config
  [10] Finalize and print deployment summary

Author: Matheus Lacerda Ferreira
License: MIT
"""

import os
import shutil

from cli.commands._utils import (
    TAILWIND_VERSION,
    log,
    ok,
    err,
    run,
    write_file,
    check_uv,
    cleanup_uv_scaffolding,
    guard_existing_dir,
    resolve_tailwind_binary,
    download_tailwind,
    append_gitignore_tailwind,
    print_summary,
)
from cli.payloads.tailwind_config import TAILWIND_CONFIG
from cli.payloads.input_css import INPUT_CSS
from cli.payloads.fastapi_payloads import (
    FASTAPI_MAIN,
    FASTAPI_CONFIG,
    FASTAPI_DASHBOARD,
    FASTAPI_BASE_HTML,
    FASTAPI_INDEX_HTML,
    FASTAPI_DASHBOARD_HTML,
    FASTAPI_METRICS_PARTIAL,
)


# ---------------------------------------------------------------------------
# MAIN PIPELINE
# ---------------------------------------------------------------------------
def run_pipeline(project_name):
    """Execute the full `init fastapi` deployment pipeline.

    Args:
        project_name: Name of the FastAPI project directory to create.
    """
    project_dir = os.path.join(os.getcwd(), project_name)

    # Guard: prevent overwriting
    guard_existing_dir(project_dir)

    # -- Step 00: Validate uv ------------------------------------------------
    log("00", "Validating uv binary...")
    check_uv()
    ok("uv detected on PATH.")

    # -- Step 01: Initialize project with uv ----------------------------------
    log("01", f"Initializing project: {project_name}")
    run(["uv", "init", "--no-workspace", project_name])
    cleanup_uv_scaffolding(project_dir)
    ok(f"Project directory created :: {project_dir}")

    # -- Step 02: Install dependencies ----------------------------------------
    log("02", "Installing dependencies: fastapi, uvicorn, jinja2, python-multipart, polars")
    run(
        ["uv", "add", "fastapi", "uvicorn", "jinja2", "python-multipart", "polars"],
        cwd=project_dir,
    )
    ok("Dependencies locked and installed.")

    # -- Step 03: Generate folder structure -----------------------------------
    log("03", "Generating opinionated folder structure")

    dirs = [
        os.path.join(project_dir, "routers"),
        os.path.join(project_dir, "core"),
        os.path.join(project_dir, "templates", "dashboard", "partials"),
        os.path.join(project_dir, "static", "css"),
        os.path.join(project_dir, "static", "js"),
    ]
    for d in dirs:
        os.makedirs(d, exist_ok=True)

    # Python package __init__.py files
    for pkg in ["routers", "core"]:
        init_path = os.path.join(project_dir, pkg, "__init__.py")
        with open(init_path, "w", encoding="utf-8") as f:
            f.write(f"# LOGICAL BRUTALISM :: {pkg.upper()} PACKAGE\n")

    ok("Directories created :: /routers, /core, /templates, /static")

    # -- Step 04: Generate core/config.py -------------------------------------
    log("04", "Generating core/config.py")
    write_file(os.path.join(project_dir, "core", "config.py"), FASTAPI_CONFIG)
    ok("Configuration module :: core/config.py")

    # -- Step 05: Generate main.py --------------------------------------------
    log("05", "Generating main.py (FastAPI engine)")
    write_file(os.path.join(project_dir, "main.py"), FASTAPI_MAIN)
    ok("Application entry point :: main.py")

    # -- Step 06: Generate routers/dashboard.py --------------------------------
    log("06", "Generating routers/dashboard.py (Polars + HTMX)")
    write_file(
        os.path.join(project_dir, "routers", "dashboard.py"),
        FASTAPI_DASHBOARD,
    )
    ok("Dashboard router :: routers/dashboard.py")
    ok("  -> GET /dashboard/ (full page, Polars DataFrame table)")
    ok("  -> GET /dashboard/partial/metrics (HTMX partial, Server-Driven UI)")

    # -- Step 07: Download TailwindCSS Standalone CLI -------------------------
    log("07", f"Downloading TailwindCSS Standalone CLI ({TAILWIND_VERSION})")
    url, local_name = resolve_tailwind_binary()
    tailwind_path = os.path.join(project_dir, local_name)
    log("07", f"Source: {url}")
    download_tailwind(url, tailwind_path)
    ok(f"TailwindCSS binary deployed :: {local_name}")

    # -- Step 08: Generate templates ------------------------------------------
    log("08", "Generating Jinja2 templates")

    write_file(
        os.path.join(project_dir, "templates", "base.html"),
        FASTAPI_BASE_HTML,
    )
    ok("Base template :: templates/base.html")

    write_file(
        os.path.join(project_dir, "templates", "index.html"),
        FASTAPI_INDEX_HTML,
    )
    ok("Root landing :: templates/index.html")

    write_file(
        os.path.join(project_dir, "templates", "dashboard", "index.html"),
        FASTAPI_DASHBOARD_HTML,
    )
    ok("Dashboard page :: templates/dashboard/index.html")

    write_file(
        os.path.join(project_dir, "templates", "dashboard", "partials", "metrics.html"),
        FASTAPI_METRICS_PARTIAL,
    )
    ok("HTMX partial :: templates/dashboard/partials/metrics.html")

    # -- Step 09: Inject core CSS + Tailwind ----------------------------------
    log("09", "Injecting core CSS and Tailwind configuration")

    # Copy core CSS from package data
    script_dir = os.path.dirname(os.path.abspath(__file__))
    core_css_source = os.path.normpath(
        os.path.join(script_dir, "..", "..", "core", "logical-brutalism.css")
    )

    css_dir = os.path.join(project_dir, "static", "css")

    try:
        shutil.copy2(core_css_source, os.path.join(css_dir, "logical-brutalism.css"))
        ok("Core CSS matrix injected :: static/css/logical-brutalism.css")
    except FileNotFoundError:
        err(
            f"Core CSS not found at: {core_css_source}\n"
            f"  Package data may be corrupted. Reinstall logical-brutalism."
        )

    # Write Tailwind input.css
    write_file(os.path.join(css_dir, "input.css"), INPUT_CSS)
    ok("Tailwind input directive :: static/css/input.css")

    # Write tailwind.config.js
    write_file(os.path.join(project_dir, "tailwind.config.js"), TAILWIND_CONFIG)
    ok("Tailwind config locked :: tailwind.config.js")

    # -- Step 10: Finalize ----------------------------------------------------
    log("10", "Finalizing deployment")
    append_gitignore_tailwind(project_dir)

    # Print summary
    print_summary(
        project_name=project_name,
        local_tw_name=local_name,
        run_cmd=f"cd {project_name} && uv run uvicorn main:app --reload",
    )
