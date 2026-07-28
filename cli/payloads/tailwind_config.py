"""
LOGICAL BRUTALISM :: PAYLOAD :: TAILWIND CONFIG
Strict Tailwind v3.4.x configuration that enforces:
- Zero border-radius (Axiom III / P-02)
- Zero transitions and animations (P-06)
- LB color tokens and typography
"""

TAILWIND_CONFIG = """/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
  ],
  theme: {
    borderRadius: {
      none: '0',
      DEFAULT: '0',
    },
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
    transitionProperty: false,
    transitionDuration: false,
    transitionTimingFunction: false,
    transitionDelay: false,
    animation: false,
  },
}
"""
