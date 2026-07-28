"""
LOGICAL BRUTALISM :: PAYLOAD :: EXPRESS/HTMX TEMPLATES
Generated file contents for the `init express-htmx` scaffold.

Author: Matheus Lacerda Ferreira
License: MIT
"""

# ---------------------------------------------------------------------------
# package.json :: Pre-configured with TailwindCSS build scripts
# ---------------------------------------------------------------------------
def generate_express_package_json(project_name: str) -> str:
    return f"""\
{{
  "name": "{project_name}",
  "version": "1.0.0",
  "description": "Logical Brutalism Express Instance",
  "main": "server.js",
  "scripts": {{
    "start": "node server.js",
    "dev": "node server.js",
    "build:css": "npx tailwindcss -i ./public/css/input.css -o ./public/css/output.css",
    "watch:css": "npx tailwindcss -i ./public/css/input.css -o ./public/css/output.css --watch"
  }},
  "keywords": [],
  "author": "",
  "license": "ISC"
}}
"""

# ---------------------------------------------------------------------------
# server.js :: Main Application Entry Point
# ---------------------------------------------------------------------------
EXPRESS_SERVER_JS = """\
/**
 * LOGICAL BRUTALISM :: EXPRESS ENGINE
 * Core HTTP Server configuration.
 */

const express = require('express');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

// View Engine: EJS
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

// Middleware
app.use(express.static(path.join(__dirname, 'public')));
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

// Routes
const indexRoutes = require('./routes/index');
app.use('/', indexRoutes);

// Server Init
app.listen(PORT, () => {
  console.log(`\\n[SYS] EXPRESS ENGINE INITIALIZED`);
  console.log(`[SYS] PORT: ${PORT}`);
  console.log(`[SYS] NODE_ENV: ${process.env.NODE_ENV || 'development'}\\n`);
});
"""

# ---------------------------------------------------------------------------
# routes/index.js :: Request Handlers and HTMX Swap Logic
# ---------------------------------------------------------------------------
EXPRESS_ROUTES_INDEX_JS = """\
const express = require('express');
const router = express.Router();

/**
 * GET /
 * Renders the primary dashboard view using base layout.
 */
router.get('/', (req, res) => {
  res.render('index', { title: 'Dashboard' });
});

/**
 * GET /api/status
 * HTMX Partial Endpoint: Returns a high-density B2B server status block.
 * Simulates system data retrieval.
 */
router.get('/api/status', (req, res) => {
  // Simulate telemetry data
  const latencyMs = Math.floor(Math.random() * 25) + 5;
  const timestamp = new Date().toISOString();
  
  res.render('partials/status_block', { 
    latency: latencyMs,
    timestamp: timestamp,
    status_code: '200 OK'
  });
});

module.exports = router;
"""

# ---------------------------------------------------------------------------
# views/base.ejs :: Master Template
# ---------------------------------------------------------------------------
EXPRESS_BASE_EJS = """\
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Logical Brutalism :: <%- title %></title>
    
    <!-- Tailwind Output -->
    <link href="/css/output.css" rel="stylesheet">

    <!-- Absolute Typography :: Iosevka Family -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Iosevka+Aile:wght@400;500;600;700&family=Iosevka:wght@400;500;600;700&display=swap" rel="stylesheet">
    
    <!-- Core Dependencies -->
    <script src="https://unpkg.com/htmx.org@1.9.10" integrity="sha384-D1Kt99CQMDuVetoL1lrYwg5t+9QdHe7NLX/SoJYkXDFfX37iInKRy5xLSi8nO7UC" crossorigin="anonymous"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>
  </head>
  <body class="bg-lb-void text-lb-text font-struct h-screen w-screen overflow-hidden flex items-center justify-center">
    
    <div class="border border-lb-surface p-6 max-w-3xl w-full mx-4 h-[80vh] flex flex-col">
      <header class="border-b-2 border-lb-surface pb-3 mb-6 flex justify-between items-end">
        <div>
          <h1 class="font-code text-lb-amber uppercase tracking-widest text-lg">
            [SYS] EXPRESS/EJS ENVIRONMENT
          </h1>
          <p class="font-struct text-lb-text-dim text-sm mt-1">
            Server-Driven UI Protocol Active.
          </p>
        </div>
        <div class="text-right">
          <code class="text-xs text-lb-text-dim">HTMX_READY = 1</code>
        </div>
      </header>

      <main class="flex-grow overflow-y-auto space-y-4 font-code text-sm">
        <%- body %>
      </main>

      <footer class="mt-6 pt-3 border-t border-lb-surface">
        <code class="font-code text-lb-error text-xs uppercase block">
          Axiom III Active: Boundary distortions (border-radius) will result in compilation failure.
        </code>
      </footer>
    </div>
    
  </body>
</html>
"""

# ---------------------------------------------------------------------------
# views/index.ejs :: Main Dashboard View
# ---------------------------------------------------------------------------
EXPRESS_INDEX_EJS = """\
<%- include('base', { title: title, body: `
  <div class="space-y-6">
    <div class="border border-lb-surface p-4">
      <p class="mb-4">
        The backend build pipeline operates strictly under Logical Brutalism governance.
      </p>
      <ul class="list-none space-y-2">
        <li class="flex items-center gap-2">
          <span class="text-lb-amber">[+]</span> EJS Templating Engine Configured
        </li>
        <li class="flex items-center gap-2">
          <span class="text-lb-amber">[+]</span> TailwindCSS build script active
        </li>
      </ul>
    </div>

    <!-- HTMX Server Status Demonstration -->
    <div>
      <div class="flex justify-between items-center mb-2">
        <span class="text-lb-text-dim text-xs uppercase tracking-widest">Telemetry Stream</span>
        <button 
          hx-get="/api/status" 
          hx-swap="afterbegin" 
          hx-target="#log-stream"
          class="px-3 py-1 border border-lb-surface hover:bg-lb-surface text-lb-text text-xs uppercase cursor-pointer">
          PULL METRICS
        </button>
      </div>
      
      <!-- Stream Container: New blocks will be prepended here -->
      <div id="log-stream" class="border border-lb-surface bg-[#050505] min-h-[120px] max-h-[300px] overflow-y-auto">
        <!-- Initial empty state -->
      </div>
    </div>
  </div>
`}) %>
"""

# ---------------------------------------------------------------------------
# views/partials/status_block.ejs :: High-Density HTMX Fragment
# ---------------------------------------------------------------------------
EXPRESS_PARTIAL_EJS = """\
<div class="border-b border-lb-surface flex items-center justify-between px-3 py-2 text-xs">
  <div class="flex items-center gap-4">
    <span class="text-lb-text-dim">[<%= timestamp %>]</span>
    <span>SYS_METRICS_PULL</span>
  </div>
  <div class="flex items-center gap-4">
    <span class="text-lb-amber font-bold"><%= latency %>ms</span>
    <span class="text-lb-text-dim">STATUS: <%= status_code %></span>
  </div>
</div>
"""

# ---------------------------------------------------------------------------
# tailwind.config.js :: Strict Configuration
# ---------------------------------------------------------------------------
EXPRESS_TAILWIND_CONFIG = """\
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./views/**/*.ejs",
    "./public/**/*.js"
  ],
  theme: {
    borderRadius: {
      none: '0',
      DEFAULT: '0',
    },
    boxShadow: {
      none: 'none',
      DEFAULT: 'none',
    },
    extend: {
      colors: {
        'lb-void': '#0A0A0A',
        'lb-amber': '#FFB000',
        'lb-surface': '#222222',
        'lb-text': '#CCCCCC',
        'lb-text-dim': '#888888',
        'lb-white': '#FFFFFF',
        'lb-error': '#FF3333',
      },
      fontFamily: {
        'struct': ['Iosevka Aile', 'sans-serif'],
        'code': ['Iosevka', 'monospace'],
      },
      spacing: {
        '1': '0.25rem',
        '2': '0.5rem',
        '3': '1rem',
        '4': '1.5rem',
        '5': '2rem',
        '6': '3rem',
      },
    },
  },
  corePlugins: {
    borderRadius: false,
    boxShadow: false,
    transitionProperty: false,
    transitionDuration: false,
    transitionTimingFunction: false,
    transitionDelay: false,
    animation: false,
  },
}
"""

# ---------------------------------------------------------------------------
# public/css/input.css :: Tailwind Directives & Base Enforcement
# ---------------------------------------------------------------------------
EXPRESS_INPUT_CSS = """\
/* =========================================================================
   LOGICAL BRUTALISM :: EXPRESS STYLESHEET
   "What does not resolve, does not exist."
   ========================================================================= */

@tailwind base;
@tailwind components;
@tailwind utilities;

/* PARAMETRIC ENFORCEMENT LAYER */
@layer base {
  *, *::before, *::after {
    border-radius: 0 !important;
    transition: none !important;
    animation: none !important;
    box-shadow: none !important;
  }
}
"""
