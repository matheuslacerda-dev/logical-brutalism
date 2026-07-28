"""
LOGICAL BRUTALISM :: PAYLOAD :: VITE/STATIC TEMPLATES
Generated file contents for the `init vite-static` scaffold.

Author: Matheus Lacerda Ferreira
License: MIT
"""

# ---------------------------------------------------------------------------
# index.html :: Sterile, High-Density Structural Template
# ---------------------------------------------------------------------------
VITE_INDEX_HTML = """\
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Logical Brutalism :: Static Instance</title>
    
    <!-- Absolute Typography :: Iosevka Family -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Iosevka+Aile:wght@400;500;600;700&family=Iosevka:wght@400;500;600;700&display=swap" rel="stylesheet">
  </head>
  <body class="bg-lb-void text-lb-text font-struct h-screen w-screen overflow-hidden flex items-center justify-center">
    
    <div class="border border-lb-surface p-6 max-w-2xl w-full mx-4">
      <header class="border-b-2 border-lb-surface pb-3 mb-6">
        <h1 class="font-code text-lb-amber uppercase tracking-widest text-lg">
          [SYS] Vite Environment Initialized
        </h1>
        <p class="font-struct text-lb-text-dim text-sm mt-1">
          Static asset compilation and Hot Module Replacement active.
        </p>
      </header>

      <main class="space-y-4">
        <p>
          The frontend build pipeline operates strictly under Logical Brutalism governance.
        </p>
        <ul class="list-none space-y-2 font-code text-sm">
          <li class="flex items-center gap-2">
            <span class="text-lb-amber">[+]</span> TailwindCSS injected via PostCSS
          </li>
          <li class="flex items-center gap-2">
            <span class="text-lb-amber">[+]</span> Alpine.js initialized (Parasitic Reactivity)
          </li>
          <li class="flex items-center gap-2">
            <span class="text-lb-amber">[+]</span> HTMX.org initialized (Server-Driven UI Ready)
          </li>
        </ul>
        
        <div x-data="{ count: 0 }" class="mt-6 border border-lb-surface p-4 flex justify-between items-center">
          <span class="font-code text-sm">Alpine.js Telemetry:</span>
          <div class="flex items-center gap-4">
            <span class="font-code text-lb-white text-xl" x-text="count"></span>
            <button @click="count++" class="px-4 py-1 border border-lb-surface hover:bg-lb-surface text-lb-text font-code text-sm">
              INCREMENT
            </button>
          </div>
        </div>
      </main>

      <footer class="mt-6 pt-3 border-t border-lb-surface">
        <code class="font-code text-lb-error text-xs uppercase block">
          Axiom III Active: Boundary distortions (border-radius) will result in compilation failure.
        </code>
      </footer>
    </div>

    <script type="module" src="/main.js"></script>
  </body>
</html>
"""

# ---------------------------------------------------------------------------
# main.js :: Application Entry Point
# ---------------------------------------------------------------------------
VITE_MAIN_JS = """\
/**
 * LOGICAL BRUTALISM :: VITE ENTRY POINT
 * Initializes the static environment and reactive dependencies.
 */

// Import structural CSS (Tailwind + LB Enforcements)
import './style.css'

// Import core dependencies
import 'htmx.org'
import Alpine from 'alpinejs'

// Initialize Alpine as a global parasite
window.Alpine = Alpine
Alpine.start()

console.log('[SYS] Logical Brutalism :: Environment Active')
"""

# ---------------------------------------------------------------------------
# tailwind.config.js :: Strict Configuration
# ---------------------------------------------------------------------------
VITE_TAILWIND_CONFIG = """\
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./**/*.{js,ts,jsx,tsx}",
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
# postcss.config.js :: PostCSS Configuration
# ---------------------------------------------------------------------------
VITE_POSTCSS_CONFIG = """\
export default {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}
"""

# ---------------------------------------------------------------------------
# style.css :: Tailwind Directives & Base Enforcement
# ---------------------------------------------------------------------------
VITE_STYLE_CSS = """\
/* =========================================================================
   LOGICAL BRUTALISM :: VITE STYLESHEET
   "What does not resolve, does not exist."
   ========================================================================= */

@tailwind base;
@tailwind components;
@tailwind utilities;

/* PARAMETRIC ENFORCEMENT LAYER (P-02 + P-06) */
@layer base {
  *, *::before, *::after {
    border-radius: 0 !important;
    transition: none !important;
    animation: none !important;
    box-shadow: none !important;
  }
}
"""
