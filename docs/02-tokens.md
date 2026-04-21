# 02 :: COLOR SYSTEM AND TOKEN SPECIFICATION

The following CSS tokens form the primordial data layer. They are rigid and do not support extensions like alpha channel variations (`rgba()`) that do not pass extreme justification in merge requests. Improper alteration of a token destroys the global hierarchy.

## GLOBAL TOKEN USAGE GUIDELINES
It is expressly forbidden to inject inline hex codes or overwrite native properties through unlisted atomic modifiers. Strictly use the "CSS Custom Properties" mapped below:

### THEME 1: VOID-FIRST (DARK)
Primary architecture for controlled viewing environments and complex dashboards.

| CSS TOKEN | HEX VALUE | PROPOSITION AND ARCHITECTURAL FUNCTION | COGNITIVE OVERHEAD |
| :--- | :--- | :--- | :--- |
| `--color-void` | `#0A0A0A` | Non-null primary background. Calculation base of the absolute void. | Absolute Minimum |
| `--color-amber` | `#FFB000` | Critical action point (P3 Trigger). Limitation: `Max(n=1)` per Viewport. Contrast text over void: `AAA (10.81:1)`. | Immediate Maximum Alert |
| `--color-surface` | `#1E1E1E` | Context box delimiter and panels. Defines depth = `1` in the Z-Axis. | Structural Neutral |
| `--color-text` | `#888888` | Extended reading buffer. Decreases ocular load when processing paragraphs. | Low |
| `--color-white` | `#F0F0F0` | Raw data not requiring action, section headers, and direct system output. | Moderate Primary |
| `--color-error` | `#FF4444` | Worker failure, timeout, `4xx` or `5xx`. Active bypass into the prefrontal cortex via direct engagement of "urgency." | Critical Priority |

### THEME 2: INFINITY-WHITE (LIGHT EXTENSION)
Optional, triggered exclusively in extrinsic circumstances imposing extreme luminous fatigue. The background never reaches total luminosity (`#FFFFFF`), ensuring retina survival.

* `--color-infinity`: `#E3E3E3` (Industrial Concrete).
* `--color-accent`: `#B35900` (Oxidized Amber. Required luminance adjustment to maintain `AAA` contrast).
* `--color-surface`: `#CCCCCC` (Drafting Board. Discreet panel differentiation).
* `--color-text`: `#4D4D4D` (Graphite HB. Semantics aligned with long text reading color).
* `--color-ink`: `#0A0A0A` (Absolute Void. Crucial letters and absolute data points, absorbing 100% of focused visual radiation).
* `--color-error`: `#BE123C` (Emergency Stop. Value in `hsl()` corrected so it doesn't visually vibrate on the gray canvas).

## TYPOGRAPHY

Fonts do not emit feelings; they process "arrays" of letters. Two parametric instances:

### 1. The Human Layer
**Defined Font-Family:** `Inter`
**CSS Variable:** `--font-struct`
**Application:** Articles, macro instructions, meta descriptions.
**Justification:** Microscopically developed for optimal digital reading based on high x-heights and open terminals. It minimizes error rates during retinal saccades across the page.

### 2. The Logical Layer
**Defined Font-Family:** `JetBrains Mono`
**CSS Variable:** `--font-code`
**Application:** Iterative components, action labels, JSON strings, UUIDs, timestamps, infrastructure analytics tags.
**Justification:** The vertical alignment axes of Mono block fluid reading but ensure `100%` `O(1)` ocular parametric identification of one data point against another. Absence of ligature ambiguity: `1`, `I`, `l` do not compete.

## LINEAR SCALES AND COMPOSITION VECTORS

Dimensions operate via mathematical predeterminations, fundamental base `1rem` = `16px`.

**Typographic Scale (Size / Line-Height):**
* `Display`: 2.5rem (40px) / `1.1`
* `Title`: 1.375rem (22px) / `1.3`
* `Body`: 1rem (16px) / `1.5`
* `Small`: 0.875rem (14px) / `1.5`
* `Label/Code`: 0.75rem (12px) / `1.0`

**Spatial Spacing (Structural Silence):**
Margins declare logical vicinity; a "padding" determines functional grouping (Gestalt Law implemented in the DOM):
* `--space-1` = `0.25rem` (4px): Subatomic links (e.g., icon next to text in box).
* `--space-2` = `0.5rem` (8px): Base distance in labels.
* `--space-3` = `1rem` (16px): Primary block identity.
* `--space-4` = `1.5rem` (24px): Division of interdependent components.
* `--space-5` = `2rem` (32px): Section Isolation.
* `--space-6` = `3rem` (48px): Macro Architecture, breaching the user's reading flow.
