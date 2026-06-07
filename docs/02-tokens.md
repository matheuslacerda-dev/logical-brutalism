# 02 :: Color System and Tokens

The CSS tokens below are the primary visual layer. They are rigid and do not accept variations like `rgba()` without extreme justification. Changing a token without reason breaks the global hierarchy.

## Golden Rule

Never inject fixed hexadecimal values directly into code. Never overwrite native properties with unlisted modifiers. Use only the CSS Custom Properties below.

## Theme 1: Void-First (Dark)

This is the main theme. Use it in dashboards, controlled visualization environments, and internal tools.

| CSS Token | Hex Value | Function | Visual Load |
| :--- | :--- | :--- | :--- |
| `--color-void` | `#0A0A0A` | Primary background. Base of the absolute void. | Absolute minimum |
| `--color-amber` | `#FFB000` | Critical action point (P3 Trigger). Limit: **maximum 1 element per screen**. Contrast over void: `AAA (10.81:1)`. | Maximum alert, immediate |
| `--color-surface` | `#1E1E1E` | Card borders, panels, context separation. Depth `1` on the Z-axis. | Structural neutral |
| `--color-text` | `#888888` | Long-form reading text. Reduces eye fatigue in paragraphs. | Low |
| `--color-white` | `#F0F0F0` | Raw data, section titles, direct system output. | Moderate |
| `--color-error` | `#FF4444` | Failures, timeouts, `4xx`/`5xx` errors. Triggers immediate urgency reading. | Critical |

## Theme 2: Infinity-White (Light)

Optional. Use only when ambient light is so intense that the dark theme causes real fatigue.

* `--color-infinity`: `#E3E3E3` (Industrial Concrete)
* `--color-accent`: `#B35900` (Oxidized Amber — adjusted to maintain `AAA` contrast in light mode)
* `--color-surface`: `#CCCCCC` (Drafting Board — discrete panel separation)
* `--color-text`: `#4D4D4D` (Graphite HB — long reading without exhaustion)
* `--color-ink`: `#0A0A0A` (Absolute Void — critical and absolute data, absorbs 100% of attention)
* `--color-error`: `#BE123C` (Emergency Stop — calibrated not to vibrate over gray)

## Typography

One family, two weights. No exceptions. Starting from **v1.3**, the system migrated to **Iosevka** — a typeface designed for maximum information density.

### 1. The Human Layer
**Font:** `Iosevka Aile`  
**Token:** `--font-struct`  
**Use:** Articles, instructions, descriptions, anything the user needs to read as text.  
**Why:** Maintains the density and clarity of the Iosevka family, but with proportions optimized for continuous reading. High x-height and open terminals minimize reading errors.

### 2. The Logic Layer
**Font:** `Iosevka` (Mono)  
**Token:** `--font-code`  
**Use:** Action labels, JSON strings, UUIDs, timestamps, infrastructure tags, code.  
**Why:** Fixed vertical alignment. Each character occupies the same space. No ambiguity between `1`, `I`, and `l`. Instant identification of one datum against another. Iosevka was specifically designed to fit more characters per line without losing legibility — essential for high-density dashboards.

## Scales and Spacing

Base: `1rem` = `16px`.

**Typography (Size / Line Height):**
* `Display`: 2.5rem (40px) / `1.1`
* `Title`: 1.375rem (22px) / `1.3`
* `Body`: 1rem (16px) / `1.5`
* `Small`: 0.875rem (14px) / `1.5`
* `Label/Code`: 0.75rem (12px) / `1.0`

**Spacing (The Structural Silence):**
Margins declare neighborhood; padding declares grouping (Gestalt Law in the DOM):
* `--space-1` = `0.25rem` (4px): Icon next to text
* `--space-2` = `0.5rem` (8px): Internal labels
* `--space-3` = `1rem` (16px): Primary block
* `--space-4` = `1.5rem` (24px): Interdependent components
* `--space-5` = `2rem` (32px): Section isolation
* `--space-6` = `3rem` (48px): Macro architecture, reading flow break
