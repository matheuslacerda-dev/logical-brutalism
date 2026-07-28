#!/usr/bin/env python3
"""
LOGICAL BRUTALISM :: CLI ENGINE
Parametric Engine Deployment for Backend Infrastructure.

Usage:
  logical-brutalism init django <project_name>   Scaffold a Django project under LB governance.
  logical-brutalism deploy                       Legacy: copy core CSS/JS and inject base.html.

Author: Matheus Lacerda Ferreira
License: MIT
"""

import argparse
import os
import sys

# ---------------------------------------------------------------------------
# ANSI CORE COLORS
# ---------------------------------------------------------------------------
C_AMBER = "\033[38;5;214m"
C_VOID = "\033[0m"

# ---------------------------------------------------------------------------
# BRAND IDENTITY
# ---------------------------------------------------------------------------
ASCII_ART = rf"""{C_AMBER}
  _      ____   _____ _____ _____          _      
 | |    / __ \ / ____|_   _/ ____|   /\   | |     
 | |   | |  | | |  __  | || |       /  \  | |     
 | |   | |  | | | |_ | | || |      / /\ \ | |     
 | |___| |__| | |__| |_| || |____ / ____ \| |____ 
 |______\____/ \_____|_____\_____/_/    \_\______|

  ____  _____  _    _ _______       _      _____  _____ __  __ 
 |  _ \|  __ \| |  | |__   __|/\   | |    |_   _|/ ____|  \/  |
 | |_) | |__) | |  | |  | |  /  \  | |      | | | (___ | \  / |
 |  _ <|  _  /| |  | |  | | / /\ \ | |      | |  \___ \| |\/| |
 | |_) | | \ \| |__| |  | |/ ____ \| |____ _| |_ ____) | |  | |
 |____/|_|  \_\____/   |_/_/    \_\______|_____|_____/|_|  |_|

 :: WHAT DOES NOT RESOLVE, DOES NOT EXIST. ::{C_VOID}
"""

# ---------------------------------------------------------------------------
# LEGACY DEPLOY PAYLOAD (backward compatibility)
# ---------------------------------------------------------------------------
HTML_PAYLOAD = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Logical Brutalism :: Engineering Instance</title>

  <!-- Absolute Typography -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Iosevka+Aile:wght@400;500;600;700&family=Iosevka:wght@400;500;600;700&display=swap" rel="stylesheet">

  <!-- Parasitic Dependencies (HTMX/Alpine) -->
  <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>
  <script src="https://unpkg.com/htmx.org@1.9.12"></script>

  <!-- Central Visual Matrix -->
  <link rel="stylesheet" href="/static/css/logical-brutalism.css">

  <!-- Tailwind Hook with Brutalist Plugin -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="/static/js/logical-brutalism-tailwind.js"></script>

  <script>
    tailwind.config = {
      theme: {
        extend: {
          colors: {
            'lb-void': 'var(--color-void)',
            'lb-amber': 'var(--color-amber)',
            'lb-surface': 'var(--color-surface)',
            'lb-text': 'var(--color-text)',
            'lb-white': 'var(--color-white)',
            'lb-error': 'var(--color-error)',
          },
          fontFamily: {
            'struct': ['Iosevka Aile', 'sans-serif'],
            'code': ['Iosevka', 'monospace'],
          }
        }
      },
      corePlugins: {
        borderRadius: false,
        transitionProperty: false,
        transitionDuration: false,
        transitionTimingFunction: false,
        transitionDelay: false,
        animation: false,
      }
    }
  </script>
</head>
<body class="bg-lb-void text-lb-text font-struct p-8">

  <div class="max-w-4xl mx-auto border border-lb-surface bg-lb-void p-6 mt-12">
    <h1 class="font-code text-lb-amber text-lg uppercase tracking-widest mb-4">
      [SYS_ACK] Deployment Successful
    </h1>
    <p class="font-struct text-lb-text text-base">
      The visual foundation of the project now operates under Logical Brutalism governance.<br>
      The reactive libraries HTMX and Alpine.js are embedded and mapped in the DOM tree.<br>
      Every fluid transition or radius distortion has been natively vetoed in the Tailwind injector.
    </p>
    <div class="mt-6 border-t border-lb-surface pt-4">
      <code class="font-code text-lb-error text-xs uppercase">Restriction in Effect: Adding or transmuting palette variables will incur a formal systemic failure (Axiom III Violation).</code>
    </div>
  </div>

</body>
</html>
"""


# ---------------------------------------------------------------------------
# LEGACY DEPLOY COMMAND
# ---------------------------------------------------------------------------
def _cmd_deploy(_args):
    """Execute the legacy deployment protocol (copy CSS/JS + inject base.html)."""
    print(f"{C_AMBER}[STARTING DEPLOYMENT PROTOCOL]{C_VOID}\n")

    # Dynamic paths based on installer directory (OS-independent distribution)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    core_css_source = os.path.join(
        script_dir, "..", "core", "logical-brutalism.css"
    )
    core_js_source = os.path.join(
        script_dir, "..", "core", "logical-brutalism-tailwind.js"
    )

    # 1. Copy CSS and JS core resources to target infrastructure
    css_dir = os.path.join(os.getcwd(), "static", "css")
    js_dir = os.path.join(os.getcwd(), "static", "js")

    try:
        # Read primary CSS file dynamically
        with open(core_css_source, "r", encoding="utf-8") as source_file:
            css_content = source_file.read()

        os.makedirs(css_dir, exist_ok=True)
        css_path = os.path.join(css_dir, "logical-brutalism.css")
        with open(css_path, "w", encoding="utf-8") as f:
            f.write(css_content)
        print(f" [+] ROOT CSS MATRIX INJECTED :: {css_path}")

        # Read Tailwind plugin dynamically
        with open(core_js_source, "r", encoding="utf-8") as source_file:
            js_content = source_file.read()

        os.makedirs(js_dir, exist_ok=True)
        js_path = os.path.join(js_dir, "logical-brutalism-tailwind.js")
        with open(js_path, "w", encoding="utf-8") as f:
            f.write(js_content)
        print(f" [+] TAILWIND PLUGIN INJECTED :: {js_path}")

    except Exception as e:
        print(f" [ERR] Failed to copy core infrastructure files: {e}")
        sys.exit(1)

    # 2. Inject base.html
    html_path = os.path.join(os.getcwd(), "base.html")
    try:
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(HTML_PAYLOAD)
        print(f" [+] ROOT TEMPLATE (BASE.HTML) INJECTED :: {html_path}")
    except Exception as e:
        print(f" [ERR] Failed to write base HTML: {e}")
        sys.exit(1)

    print(f"\n{C_AMBER}[DEPLOYMENT COMPLETE IN O(1)]{C_VOID}")
    print(
        "The B2B infrastructure has been toggled. Returning to primary shell...\n"
    )


# ---------------------------------------------------------------------------
# INIT DJANGO COMMAND
# ---------------------------------------------------------------------------
def _cmd_init_django(args):
    """Route to the init django pipeline."""
    from cli.commands.init_django import run

    run(args.project_name)


# ---------------------------------------------------------------------------
# INIT FASTAPI COMMAND
# ---------------------------------------------------------------------------
def _cmd_init_fastapi(args):
    """Route to the init fastapi pipeline."""
    from cli.commands.init_fastapi import run_pipeline

    run_pipeline(args.project_name)


# ---------------------------------------------------------------------------
# INIT VITE-STATIC COMMAND
# ---------------------------------------------------------------------------
def _cmd_init_vite_static(args):
    """Route to the init vite-static pipeline."""
    from cli.commands.init_vite_static import run_pipeline

    run_pipeline(args.project_name)


# ---------------------------------------------------------------------------
# INIT EXPRESS-HTMX COMMAND
# ---------------------------------------------------------------------------
def _cmd_init_express_htmx(args):
    """Route to the init express-htmx pipeline."""
    from cli.commands.init_express_htmx import run_pipeline

    run_pipeline(args.project_name)


# ---------------------------------------------------------------------------
# DASH COMMAND
# ---------------------------------------------------------------------------
def _cmd_dash(args):
    """Route to the dash pipeline."""
    from cli.commands.init_dashboard import run_pipeline

    run_pipeline()


# ---------------------------------------------------------------------------
# ARGPARSE CONFIGURATION
# ---------------------------------------------------------------------------
def _build_parser():
    """Construct the CLI argument parser with subcommands."""
    parser = argparse.ArgumentParser(
        prog="logical-brutalism",
        description="Logical Brutalism :: Parametric Engine Deployment CLI",
        epilog="\"What does not resolve, does not exist.\"",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    subparsers = parser.add_subparsers(
        dest="command",
        title="commands",
        description="Available deployment commands:",
    )

    # -- deploy (legacy) --
    deploy_parser = subparsers.add_parser(
        "deploy",
        help="Legacy: copy core CSS/JS to static/ and inject base.html.",
    )
    deploy_parser.set_defaults(func=_cmd_deploy)

    # -- dash --
    dash_parser = subparsers.add_parser(
        "dash",
        help="Scaffold a standalone B2B high-density control panel HTML template in the current directory.",
    )
    dash_parser.set_defaults(func=_cmd_dash)

    # -- init --
    init_parser = subparsers.add_parser(
        "init",
        help="Initialize a new project under Logical Brutalism governance.",
    )

    init_subparsers = init_parser.add_subparsers(
        dest="framework",
        title="frameworks",
        description="Available framework scaffolds:",
    )

    # -- init django --
    init_django_parser = init_subparsers.add_parser(
        "django",
        help="Scaffold a Django project with uv, django-htmx, and TailwindCSS Standalone CLI.",
    )
    init_django_parser.add_argument(
        "project_name",
        help="Name of the Django project directory to create.",
    )
    init_django_parser.set_defaults(func=_cmd_init_django)

    # -- init fastapi --
    init_fastapi_parser = init_subparsers.add_parser(
        "fastapi",
        help="Scaffold a FastAPI project with uvicorn, Polars, HTMX, and TailwindCSS Standalone CLI.",
    )
    init_fastapi_parser.add_argument(
        "project_name",
        help="Name of the FastAPI project directory to create.",
    )
    init_fastapi_parser.set_defaults(func=_cmd_init_fastapi)

    # -- init vite-static --
    init_vite_parser = init_subparsers.add_parser(
        "vite-static",
        help="Scaffold a vanilla Vite project with HTMX, Alpine, and TailwindCSS.",
    )
    init_vite_parser.add_argument(
        "project_name",
        help="Name of the Vite project directory to create.",
    )
    init_vite_parser.set_defaults(func=_cmd_init_vite_static)

    # -- init express-htmx --
    init_express_parser = init_subparsers.add_parser(
        "express-htmx",
        help="Scaffold an Express.js project with EJS, HTMX, Alpine, and TailwindCSS.",
    )
    init_express_parser.add_argument(
        "project_name",
        help="Name of the Express project directory to create.",
    )
    init_express_parser.set_defaults(func=_cmd_init_express_htmx)



    return parser


# ---------------------------------------------------------------------------
# ENTRY POINT
# ---------------------------------------------------------------------------
def main():
    """CLI entry point. Dispatches to subcommands via argparse."""
    print(ASCII_ART)

    parser = _build_parser()
    args = parser.parse_args()

    # If no subcommand provided, print help
    if not hasattr(args, "func"):
        parser.print_help()
        sys.exit(0)

    # If 'init' was provided but no framework specified
    if args.command == "init" and not getattr(args, "framework", None):
        parser.parse_args(["init", "--help"])
        sys.exit(0)

    # Dispatch to the resolved command handler
    args.func(args)


if __name__ == "__main__":
    main()
