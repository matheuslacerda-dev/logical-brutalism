#!/usr/bin/env python3
"""
LOGICAL BRUTALISM :: INIT EXPRESS-HTMX COMMAND
Deterministic pipeline to scaffold an Express/EJS project under LB governance.

Pipeline:
  [00] Validate `npm` binary on PATH
  [01] Initialize project structure and package.json
  [02] Install core backend dependencies: express, ejs
  [03] Install frontend build dependencies: tailwindcss
  [04] Generate structural directories (views, public, routes)
  [05] Inject Express logic and LB templates (EJS + Tailwind)
  [06] Finalize and print deployment summary

Author: Matheus Lacerda Ferreira
License: MIT
"""

import os
import shutil

from cli.commands._utils import (
    log,
    ok,
    err,
    run,
    write_file,
    guard_existing_dir,
    C_AMBER,
    C_DIM,
    C_VOID,
)

from cli.payloads.express_payloads import (
    generate_express_package_json,
    EXPRESS_SERVER_JS,
    EXPRESS_ROUTES_INDEX_JS,
    EXPRESS_BASE_EJS,
    EXPRESS_INDEX_EJS,
    EXPRESS_PARTIAL_EJS,
    EXPRESS_TAILWIND_CONFIG,
    EXPRESS_INPUT_CSS,
)

def check_npm():
    """Validate `npm` binary exists on PATH."""
    if shutil.which("npm") is None:
        err(
            "'npm' binary not found.\n"
            "  Logical Brutalism CLI requires Node.js/NPM for Express scaffolding.\n"
            "  Install Node.js before proceeding."
        )

# ---------------------------------------------------------------------------
# MAIN PIPELINE
# ---------------------------------------------------------------------------
def run_pipeline(project_name):
    """Execute the full `init express-htmx` deployment pipeline.

    Args:
        project_name: Name of the Express project directory to create.
    """
    project_dir = os.path.join(os.getcwd(), project_name)

    # Guard: prevent overwriting
    guard_existing_dir(project_dir)

    npm_bin = shutil.which("npm")

    # -- Step 00: Validate NPM -----------------------------------------------
    log("00", "Validating npm binary...")
    check_npm()
    ok("Node package manager detected on PATH.")

    # -- Step 01: Initialize project structure -------------------------------
    log("01", f"Initializing Express project: {project_name}")
    os.makedirs(project_dir)
    write_file(
        os.path.join(project_dir, "package.json"),
        generate_express_package_json(project_name)
    )
    ok(f"Project directory and package.json created :: {project_dir}")

    # -- Step 02: Install core dependencies -----------------------------------
    log("02", "Installing core backend dependencies: express, ejs")
    run([npm_bin, "install", "express", "ejs"], cwd=project_dir)
    ok("Express and EJS locked.")

    # -- Step 03: Install frontend build dependencies -------------------------
    log("03", "Installing frontend build tooling: tailwindcss (v3)")
    run([npm_bin, "install", "-D", "tailwindcss@^3.4.17"], cwd=project_dir)
    ok("TailwindCSS installed as dev dependency.")

    # -- Step 04: Generate structural directories -----------------------------
    log("04", "Generating structural directories")
    dirs = [
        os.path.join(project_dir, "views", "partials"),
        os.path.join(project_dir, "public", "css"),
        os.path.join(project_dir, "routes"),
    ]
    for d in dirs:
        os.makedirs(d, exist_ok=True)
    ok("Directories created :: /views/partials, /public/css, /routes")

    # -- Step 05: Inject Logic and Templates ----------------------------------
    log("05", "Injecting Express logic and LB templates")
    
    # Server and Routes
    write_file(os.path.join(project_dir, "server.js"), EXPRESS_SERVER_JS)
    ok("Entry point :: server.js")
    
    write_file(os.path.join(project_dir, "routes", "index.js"), EXPRESS_ROUTES_INDEX_JS)
    ok("Routes module :: routes/index.js")

    # Views
    write_file(os.path.join(project_dir, "views", "base.ejs"), EXPRESS_BASE_EJS)
    write_file(os.path.join(project_dir, "views", "index.ejs"), EXPRESS_INDEX_EJS)
    write_file(os.path.join(project_dir, "views", "partials", "status_block.ejs"), EXPRESS_PARTIAL_EJS)
    ok("EJS Views :: base.ejs, index.ejs, partials/status_block.ejs")

    # Tailwind
    write_file(os.path.join(project_dir, "tailwind.config.js"), EXPRESS_TAILWIND_CONFIG)
    write_file(os.path.join(project_dir, "public", "css", "input.css"), EXPRESS_INPUT_CSS)
    ok("Tailwind config and inputs injected.")

    # -- Step 06: Finalize ----------------------------------------------------
    log("06", "Finalizing deployment")
    
    # Print summary
    print(f"\n {C_AMBER}{'=' * 64}{C_VOID}")
    print(f" {C_AMBER}[DEPLOYMENT COMPLETE]{C_VOID}")
    print(f" {C_AMBER}{'=' * 64}{C_VOID}\n")
    print(f" {C_DIM}Project:{C_VOID}    {project_name}/")
    print(f" {C_DIM}CSS Build:{C_VOID}  cd {project_name} && npm run build:css")
    print(f" {C_DIM}Server:{C_VOID}     cd {project_name} && npm start\n")
    print(f" {C_AMBER}[>]{C_VOID} WHAT DOES NOT RESOLVE, DOES NOT EXIST.\n")
