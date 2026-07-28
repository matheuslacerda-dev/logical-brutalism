#!/usr/bin/env python3
"""
LOGICAL BRUTALISM :: DASH COMMAND
Deterministic pipeline to scaffold a standalone B2B dashboard template in the current directory.

Pipeline:
  [00] Generate dashboard.html in the current working directory
  [01] Finalize and print deployment summary

Author: Matheus Lacerda Ferreira
License: MIT
"""

import os

from cli.commands._utils import (
    log,
    ok,
    write_file,
    C_AMBER,
    C_DIM,
    C_VOID,
)

from cli.payloads.dashboard_payloads import DASHBOARD_HTML

# ---------------------------------------------------------------------------
# MAIN PIPELINE
# ---------------------------------------------------------------------------
def run_pipeline():
    """Execute the `dash` command. Creates dashboard.html in the CWD."""
    cwd = os.getcwd()
    target_file = os.path.join(cwd, "dashboard.html")

    # -- Step 01: Inject HTML template ---------------------------------------
    log("01", f"Injecting B2B high-density control panel template into {cwd}")
    write_file(target_file, DASHBOARD_HTML)
    ok("Generated :: dashboard.html")

    # -- Step 02: Finalize ----------------------------------------------------
    log("02", "Finalizing deployment")
    
    # Print summary
    print(f"\n {C_AMBER}{'=' * 64}{C_VOID}")
    print(f" {C_AMBER}[DEPLOYMENT COMPLETE]{C_VOID}")
    print(f" {C_AMBER}{'=' * 64}{C_VOID}\n")
    print(f" {C_DIM}Target:{C_VOID}     {target_file}")
    print(f" {C_DIM}Command:{C_VOID}    npx serve .\n")
    print(f" {C_AMBER}[>]{C_VOID} WHAT DOES NOT RESOLVE, DOES NOT EXIST.\n")
