#!/usr/bin/env python3
"""
LOGICAL BRUTALISM :: CLI INITIALIZER
Parametric Engine Deployment for Backend Infrastructure (Django/FastAPI).
Author: Matheus Lacerda Ferreira
License: MIT
"""

import os
import sys

# ANSI CORE COLORS
C_AMBER = '\033[38;5;214m' # Aprox #FFB000 (Oxidized Amber)
C_VOID = '\033[0m'

ASCII_ART = rf"""{C_AMBER}
  _      ____   _____ _____ _____          _      
 | |    / __ \ / ____|_   _/ ____|   /\\   | |     
 | |   | |  | | |  __  | || |       /  \\  | |     
 | |   | |  | | | |_ | | || |      / /\\ \\ | |     
 | |___| |__| | |__| |_| || |____ / ____ \\| |____ 
 |______\\____/ \\_____|_____\\_____/_/    \\_\\______|
                                                  
  ____  _____  _    _ _______       _      _____  _____ __  __ 
 |  _ \\|  __ \\| |  | |__   __|/\\   | |    |_   _|/ ____|  \\/  |
 | |_) | |__) | |  | |  | |  /  \\  | |      | | | (___ | \\  / |
 |  _ <|  _  /| |  | |  | | / /\\ \\ | |      | |  \\___ \\| |\\/| |
 | |_) | | \\ \\| |__| |  | |/ ____ \\| |____ _| |_ ____) | |  | |
 |____/|_|  \\_\\\\____/   |_/_/    \\_\\______|_____|_____/|_|  |_|
                                                               
 :: IF IT DOES NOT SOLVE IT, IT DOES NOT EXIST ::{C_VOID}
"""

CSS_PAYLOAD = """/* LOGICAL BRUTALISM v1.2.0 :: Core Engine */
*, *::before, *::after {
  box-sizing: border-box;
  margin: 0; padding: 0;
  border-radius: 0 !important;
  transition: none !important;
  animation: none !important;
}
:root {
  --color-void: #0A0A0A;
  --color-amber: #FFB000;
  --color-surface: #1E1E1E;
  --color-text: #888888;
  --color-white: #F0F0F0;
  --color-error: #FF4444;
  --font-struct: 'Inter', sans-serif;
  --font-code: 'JetBrains Mono', monospace;
}
[data-theme="infinity-white"] {
  --color-void: #E3E3E3;
  --color-amber: #B35900;
  --color-surface: #CCCCCC;
  --color-text: #4D4D4D;
  --color-white: #0A0A0A;
  --color-error: #BE123C;
}
body {
  background-color: var(--color-void);
  color: var(--color-text);
  font-family: var(--font-struct);
}
"""

HTML_PAYLOAD = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Logical Brutalism :: Engineering Instance</title>
  
  <!-- Absolute Typography -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
  
  <!-- Parasitic Dependencies (HTMX/Alpine) -->
  <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>
  <script src="https://unpkg.com/htmx.org@1.9.10"></script>
  
  <!-- Central Visual Matrix -->
  <link rel="stylesheet" href="/static/css/logical-brutalism.css">
  
  <!-- Tailwind Hook with Brutalist Plugin -->
  <script src="https://cdn.tailwindcss.com"></script>
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
            'struct': ['Inter', 'sans-serif'],
            'code': ['JetBrains Mono', 'monospace'],
          }
        }
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

def main():
    print(ASCII_ART)
    print(f"{C_AMBER}[STARTING DEPLOYMENT PROTOCOL]{C_VOID}\n")

    # 1. Diretório CSS e Arquivo CSS
    css_dir = os.path.join(os.getcwd(), 'static', 'css')
    
    try:
        os.makedirs(css_dir, exist_ok=True)
        css_path = os.path.join(css_dir, 'logical-brutalism.css')
        with open(css_path, 'w', encoding='utf-8') as f:
            f.write(CSS_PAYLOAD)
        print(f" [+] ROOT CSS MATRIX INJECTED :: {css_path}")
    except Exception as e:
        print(f" [ERR] Failed to write CSS Engine: {e}")
        sys.exit(1)

    # 2. base.html template
    html_path = os.path.join(os.getcwd(), 'base.html')
    try:
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(HTML_PAYLOAD)
        print(f" [+] ROOT TEMPLATE (BASE.HTML) INJECTED :: {html_path}")
    except Exception as e:
        print(f" [ERR] Failed to write base HTML: {e}")
        sys.exit(1)
        
    print(f"\n{C_AMBER}[DEPLOYMENT COMPLETE IN O(1)]{C_VOID}")
    print("The B2B infrastructure has been toggled. Returning to primary shell...\n")

if __name__ == '__main__':
    main()
