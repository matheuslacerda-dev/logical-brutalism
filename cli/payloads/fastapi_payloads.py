"""
LOGICAL BRUTALISM :: PAYLOAD :: FASTAPI TEMPLATES
All generated file contents for the `init fastapi` scaffold.

Templates use Jinja2 syntax (not Django template language).
Static files referenced via url_for('static', path='...').

Author: Matheus Lacerda Ferreira
License: MIT
"""

# ---------------------------------------------------------------------------
# main.py :: FastAPI Application Entry Point
# ---------------------------------------------------------------------------
FASTAPI_MAIN = """\
\"\"\"
LOGICAL BRUTALISM :: FASTAPI ENGINE
What does not resolve, does not exist.
\"\"\"

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from core.config import APP_TITLE, APP_VERSION
from routers import dashboard

# ---------------------------------------------------------------------------
# APPLICATION INSTANCE
# ---------------------------------------------------------------------------
app = FastAPI(
    title=APP_TITLE,
    version=APP_VERSION,
    docs_url="/docs",
    redoc_url=None,
)

# Mount static file server
app.mount("/static", StaticFiles(directory="static"), name="static")

# Jinja2 template engine
templates = Jinja2Templates(directory="templates")

# Router registration
app.include_router(dashboard.router)


# ---------------------------------------------------------------------------
# HEALTH ENDPOINT
# ---------------------------------------------------------------------------
@app.get("/health", tags=["system"])
async def health_check():
    \"\"\"System liveness probe. Returns operational status.\"\"\"
    return {
        "status": "operational",
        "engine": "logical-brutalism",
        "version": APP_VERSION,
    }


@app.get("/", tags=["system"])
async def root(request: Request):
    \"\"\"Root redirect to dashboard.\"\"\"
    return templates.TemplateResponse("index.html", {
        "request": request,
    })
"""

# ---------------------------------------------------------------------------
# core/config.py :: Application Configuration
# ---------------------------------------------------------------------------
FASTAPI_CONFIG = """\
\"\"\"
LOGICAL BRUTALISM :: CORE CONFIGURATION
Centralized parametric constants for the FastAPI engine.
\"\"\"

from pathlib import Path

# Base directory (project root)
BASE_DIR = Path(__file__).resolve().parent.parent

# Application identity
APP_TITLE = "Logical Brutalism :: Engineering Instance"
APP_VERSION = "0.1.0"
DEBUG = True

# Infrastructure paths
TEMPLATES_DIR = BASE_DIR / "templates"
STATIC_DIR = BASE_DIR / "static"
"""

# ---------------------------------------------------------------------------
# routers/dashboard.py :: Dashboard Router with Polars DataFrame
# ---------------------------------------------------------------------------
FASTAPI_DASHBOARD = """\
\"\"\"
LOGICAL BRUTALISM :: DASHBOARD ROUTER
Demonstrates Server-Driven UI with HTMX partial rendering
and Polars DataFrame manipulation.
\"\"\"

from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
import polars as pl

router = APIRouter(prefix="/dashboard", tags=["dashboard"])
templates = Jinja2Templates(directory="templates")


@router.get("/")
async def dashboard_index(request: Request):
    \"\"\"Full page render: Infrastructure node status from Polars DataFrame.\"\"\"

    df = pl.DataFrame({
        "node": [
            "auth-gateway",
            "db-primary",
            "cache-layer",
            "api-core",
            "queue-worker",
        ],
        "status": ["ONLINE", "ONLINE", "DEGRADED", "ONLINE", "ONLINE"],
        "latency_ms": [12, 45, 230, 18, 34],
        "uptime": ["99.99%", "99.95%", "97.80%", "99.98%", "99.91%"],
        "region": ["us-east-1", "us-east-1", "eu-west-1", "us-east-1", "ap-south-1"],
    })

    return templates.TemplateResponse("dashboard/index.html", {
        "request": request,
        "columns": df.columns,
        "rows": df.to_dicts(),
    })


@router.get("/partial/metrics")
async def metrics_partial(request: Request):
    \"\"\"Server-Driven UI: Returns an HTML partial for HTMX swap.

    This endpoint returns raw HTML — not a full page.
    HTMX on the client swaps this fragment into the DOM without a full reload.
    Data is sourced from a Polars DataFrame to demonstrate the integration.
    \"\"\"

    df = pl.DataFrame({
        "metric": ["P95 Latency", "Memory Footprint", "CPU Usage", "Throughput"],
        "value": ["23ms", "412 MB", "18.2%", "1.2k rps"],
        "delta": ["-3ms", "+12 MB", "-0.4%", "+200 rps"],
        "status": ["NOMINAL", "NOMINAL", "NOMINAL", "PEAK"],
    })

    return templates.TemplateResponse("dashboard/partials/metrics.html", {
        "request": request,
        "metrics": df.to_dicts(),
    })
"""

# ---------------------------------------------------------------------------
# templates/base.html :: Jinja2 Base Template (FastAPI)
# ---------------------------------------------------------------------------
FASTAPI_BASE_HTML = """\
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{% block title %}Logical Brutalism{% endblock %} :: Engineering Instance</title>

  <!-- Absolute Typography :: Iosevka Family -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Iosevka+Aile:wght@400;500;600;700&family=Iosevka:wght@400;500;600;700&display=swap" rel="stylesheet">

  <!-- Alpine.js :: Parasitic Reactivity Layer -->
  <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>

  <!-- HTMX :: Server-Driven UI Engine -->
  <script src="https://unpkg.com/htmx.org@1.9.12"></script>

  <!-- Logical Brutalism :: Core Visual Matrix -->
  <link rel="stylesheet" href="{{ url_for('static', path='css/logical-brutalism.css') }}">

  <!-- Tailwind :: Compiled Structural Output -->
  <link rel="stylesheet" href="{{ url_for('static', path='css/output.css') }}">

  {% block extra_head %}{% endblock %}
</head>
<body class="bg-lb-void text-lb-text font-struct">

  {% block content %}{% endblock %}

  {% block extra_js %}{% endblock %}
</body>
</html>
"""

# ---------------------------------------------------------------------------
# templates/index.html :: Root Landing Page
# ---------------------------------------------------------------------------
FASTAPI_INDEX_HTML = """\
{% extends "base.html" %}

{% block title %}System{% endblock %}

{% block content %}
<div style="max-width: 960px; margin: 0 auto; padding: var(--space-5) var(--space-4);">

  <div style="border: 1px solid var(--color-surface); padding: var(--space-5);">
    <h1 class="font-code" style="color: var(--color-amber); font-size: 1rem; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: var(--space-3);">
      [SYS_ACK] Deployment Successful
    </h1>
    <p class="font-struct" style="color: var(--color-text); font-size: 1rem; line-height: 1.6;">
      The FastAPI engine now operates under Logical Brutalism governance.<br>
      HTMX and Alpine.js are embedded in the template layer.<br>
      Polars is available for high-performance data manipulation.
    </p>

    <div style="margin-top: var(--space-4); border-top: 1px solid var(--color-surface); padding-top: var(--space-3); display: flex; gap: var(--space-3);">
      <a href="/dashboard" class="btn">[>] DASHBOARD</a>
      <a href="/health" class="btn" style="background: transparent; color: var(--color-text); border: 1px solid var(--color-surface);">[>] HEALTH</a>
      <a href="/docs" class="btn" style="background: transparent; color: var(--color-text); border: 1px solid var(--color-surface);">[>] API DOCS</a>
    </div>

    <div style="margin-top: var(--space-4); border-top: 1px solid var(--color-surface); padding-top: var(--space-3);">
      <code class="font-code" style="color: var(--color-error); font-size: 0.75rem; text-transform: uppercase;">
        Restriction in Effect: Axiom III violation triggers systemic failure.
      </code>
    </div>
  </div>

</div>
{% endblock %}
"""

# ---------------------------------------------------------------------------
# templates/dashboard/index.html :: Dashboard Full Page
# ---------------------------------------------------------------------------
FASTAPI_DASHBOARD_HTML = """\
{% extends "base.html" %}

{% block title %}Dashboard{% endblock %}

{% block content %}
<div style="max-width: 960px; margin: 0 auto; padding: var(--space-5) var(--space-4);">

  <!-- Header -->
  <div style="border-bottom: 2px solid var(--color-surface); padding-bottom: var(--space-3); margin-bottom: var(--space-5);">
    <h1 class="font-code" style="color: var(--color-amber); font-size: 1rem; text-transform: uppercase; letter-spacing: 0.08em;">
      [SYS] Infrastructure Dashboard
    </h1>
    <p class="font-struct" style="color: var(--color-text); font-size: 0.875rem; margin-top: var(--space-1);">
      Real-time node status. Data sourced from Polars DataFrame.
    </p>
  </div>

  <!-- Node Status Table (Polars DataFrame) -->
  <div style="overflow-x: auto; border: 1px solid var(--color-surface); margin-bottom: var(--space-5);">
    <table style="width: 100%; border-collapse: collapse;">
      <thead>
        <tr>
          {% for col in columns %}
          <th style="text-align: left; padding: var(--space-2) var(--space-3); border-bottom: 2px solid var(--color-surface); background: var(--color-surface); color: var(--color-white); font-family: var(--font-code); text-transform: uppercase; font-size: 0.75rem; letter-spacing: 0.08em;">
            {{ col }}
          </th>
          {% endfor %}
        </tr>
      </thead>
      <tbody>
        {% for row in rows %}
        <tr>
          {% for col in columns %}
          <td class="font-code" style="padding: var(--space-2) var(--space-3); border-bottom: 1px solid var(--color-surface); font-size: 0.875rem;
            {% if col == 'status' and row[col] != 'ONLINE' %}color: var(--color-error);
            {% elif col == 'status' %}color: var(--color-amber);
            {% else %}color: var(--color-text);
            {% endif %}">
            {{ row[col] }}
          </td>
          {% endfor %}
        </tr>
        {% endfor %}
      </tbody>
    </table>
  </div>

  <!-- HTMX :: Server-Driven Metrics Panel -->
  <div style="border: 1px solid var(--color-surface); padding: var(--space-4);">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: var(--space-3); border-bottom: 1px solid var(--color-surface); padding-bottom: var(--space-3);">
      <h2 class="font-code" style="color: var(--color-white); text-transform: uppercase; font-size: 0.875rem; letter-spacing: 0.08em;">
        [>] Live Metrics :: Server-Driven UI
      </h2>
      <button class="btn"
              hx-get="/dashboard/partial/metrics"
              hx-target="#metrics-container"
              hx-swap="innerHTML">
        [REFRESH]
      </button>
    </div>
    <div id="metrics-container"
         hx-get="/dashboard/partial/metrics"
         hx-trigger="load"
         hx-swap="innerHTML">
      <span class="font-code" style="color: var(--color-text); font-size: 0.75rem;">[...] Loading metrics</span>
    </div>
  </div>

  <!-- Navigation -->
  <div style="margin-top: var(--space-4);">
    <a href="/" class="font-code" style="color: var(--color-text); font-size: 0.75rem; text-decoration: none;">[<] BACK TO ROOT</a>
  </div>

</div>
{% endblock %}
"""

# ---------------------------------------------------------------------------
# templates/dashboard/partials/metrics.html :: HTMX Partial (no extends)
# ---------------------------------------------------------------------------
FASTAPI_METRICS_PARTIAL = """\
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: var(--space-3);">
  {% for m in metrics %}
  <div class="lb-card">
    <div class="font-code" style="color: var(--color-text); font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.08em;">
      {{ m.metric }}
    </div>
    <div class="font-code" style="color: var(--color-white); font-size: 1.375rem; margin-top: var(--space-2);">
      {{ m.value }}
    </div>
    <div style="display: flex; justify-content: space-between; margin-top: var(--space-2);">
      <span class="font-code" style="font-size: 0.75rem;
        {% if m.status == 'PEAK' %}color: var(--color-amber);
        {% else %}color: var(--color-text);
        {% endif %}">
        {{ m.status }}
      </span>
      <span class="font-code" style="color: var(--color-text); font-size: 0.75rem;">
        {{ m.delta }}
      </span>
    </div>
  </div>
  {% endfor %}
</div>
"""
