"""
LOGICAL BRUTALISM :: PAYLOAD :: TAILWIND INPUT CSS
Entry point for TailwindCSS Standalone CLI compilation.
Includes parametric enforcement layer (P-02 + P-06).
"""

INPUT_CSS = """\
/* =========================================================================
   LOGICAL BRUTALISM :: TAILWIND INPUT DIRECTIVE
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
  }
}
"""
