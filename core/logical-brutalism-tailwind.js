/**
 * LOGICAL BRUTALISM :: TAILWIND PLUGIN v1.3
 * AUTHOR: Matheus Lacerda Ferreira
 * 
 * Injecting the parametric matrix into Tailwind CSS.
 * Zero roundness. Zero transition. Pure structure.
 * v1.3: Migrated to Iosevka font family.
 */

const plugin = require('tailwindcss/plugin');

module.exports = plugin(
  function ({ addBase }) {
    // Aggressive Global Override to disable all rounding and transitions
    addBase({
      '*': {
        'border-radius': '0 !important',
        'transition': 'none !important',
        'animation': 'none !important',
      },
      ':root': {
        '--color-void': '#0A0A0A',
        '--color-amber': '#FFB000',
        '--color-surface': '#1E1E1E',
        '--color-text': '#888888',
        '--color-white': '#F0F0F0',
        '--color-error': '#FF4444',
      },
      '[data-theme="infinity-white"]': {
        '--color-void': '#E3E3E3',
        '--color-amber': '#B35900',
        '--color-surface': '#CCCCCC',
        '--color-text': '#4D4D4D',
        '--color-white': '#0A0A0A',
        '--color-error': '#BE123C',
      }
    });
  },
  {
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
        spacing: {
          '1': '0.25rem',
          '2': '0.5rem',
          '3': '1rem',
          '4': '1.5rem',
          '5': '2rem',
          '6': '3rem',
        },
        fontFamily: {
          'struct': ['Iosevka Aile', 'sans-serif'],
          'code': ['Iosevka', 'monospace'],
        }
      },
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
);
