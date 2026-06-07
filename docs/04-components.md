# 04 :: Core Component Anatomy and Mathematics

Every component must respect the API of "Structural Truth". Standardization does not vary between micro-frontends or page routes. Inherited subcomponents couple universal rules.

## 1. Primary and Secondary Button

The execution node. The point where the user fires an HTTP request or reverts a state.

*   **Geometry:** `min-height` locked at `44px`. WCAG compliance for mobile touch targets.
*   **Transition:** `none`. States are discrete.
*   **Border:** `1px solid var(--color-surface)` on secondary, no exceptions.
*   **Visible Focus:** Omitting `outline` is a serious failure. Use `outline: 2px solid var(--color-amber)` with `outline-offset: 2px` for perceptible tracking during keyboard tabbing.
*   **Primary:** `background-color: var(--color-amber)` with text `#0A0A0A` and font `--font-code` (`Iosevka`). Conveys direct, robotic order.

## 2. Error State (Maximum Honesty)

Native modals or conventional toasts hide the problem. The Logical Brutalism error component exposes four simultaneous layers, with `border-left: 4px solid var(--color-error)`:

| Layer | What it communicates | Rendering |
| :---: | :--- | :--- |
| **01** | **Failure Code** (What broke?) | `font-family: var(--font-code); color: var(--color-error);` Ex: `[ERR_503_DB_TIMEOUT]` |
| **02** | **Route Title** (Where are we?) | `font-family: var(--font-code); color: var(--color-white);` (Dark Mode) |
| **03** | **Organic Description** (Why did it happen?) | `font-family: var(--font-struct); color: var(--color-text);` The only layer that admits natural language (Iosevka Aile). |
| **04** | **Action Vector** (What to do now?) | `font-family: var(--font-code); color: var(--color-amber);` Ex: `> START NEW REQUEST`. Clickable, with outline on hover. |

## 3. Processing Loader

The only system anomaly that may have movement — because indicating that something is happening is function, not decoration.

**Specific Rules:**
1.  **ASCII First:** Instead of GIFs or CSS spinners with dozens of `keyframes`, use a simple array updated every `80ms` via JS: `['|', '/', '-', '\']`. The `inner-text` changes and signals that the thread is busy, without GPU repaint overhead.
2.  **Linear Bar (Alternative):** For uploads/downloads with measurable progress, use a strict rectangular div. Step-by-step absolute advancement (`border-radius: 0`), no smoothed transition hiding TCP-locked frames.
