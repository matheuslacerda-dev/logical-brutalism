# 04 :: ANATOMY AND MATHEMATICS OF CORE COMPONENTS

Every component must strictly respect the "Structural Truth" API. Standardization does not suffer variations among micro-frontends or page routes. Subcomponents couple to universal rules.

## 1. COMPONENT :: PRIMARY AND SECONDARY BUTTON

This is the executing node. The user's main actuator to engage an HTTP request or revert a mutable state.

*   **Mandatory Geometry:** The computed height of the bounding-box (`min-height`) must strictly lock at `44px`, following full WCAG compliance for touch targets in mobile environments.
*   **CSS `transition`:** Totally null (`none`).
*   **Border Declarations:** Primary border applied as 1px solid (`border: 1px solid var(--color-surface)`), no exceptions.
*   **Exposed Focus State:** Omitting outline is a severe failure in Logical Brutalism. Target injection requires a minimum `outline: 2px solid var(--color-amber)` paired with `outline-offset: 2px` to create a noticeable tracking on keyboard "tabbing" for assistive engineering.
*   **Primary Appearance:** `background-color: var(--color-amber)` and font color adjusted to `#0A0A0A` via high contrast token in Light System or fixed dark, always mapping `--font-code` (`JetBrains Mono`). Transmits direct robotic order.

## 2. COMPONENT :: ERROR STATE (MAXIMUM HONESTY)

Native modals or conventional toast blocks generate dissimulation and do not report traceability. Failure components encapsulate all four Norman layers simultaneously exposed brutally next to the `border-left: 4px solid var(--color-error)`:

| LAYER ID | FUNCTIONAL DESCRIPTIVE | STYLIZATION RENDERING SPECIFICATION |
| :---: | :--- | :--- |
| **01** | **Fault Code** (What failed server/browser side?) | CSS: `font-family: var(--font-code); color: var(--color-error);` ex: `[ERR_503_DB_TIMEOUT]` (Formatted string). |
| **02** | **Script Title** (In which business instance is it located?) | CSS: `font-family: var(--font-code); color: var(--color-white);` (Dark Mode). |
| **03** | **Organic Description** (Why did the event occur?) | CSS: `font-family: var(--font-struct); color: var(--color-text);` Only this string admits natural verbosity in human language (Inter). |
| **04** | **Action Vector** (The recovery command / front try-catch) | CSS: `font-family: var(--font-code); color: var(--color-amber);` ex: `> INITIATE NEW REQUEST`. Instinctively clickable via hover outline. |

## 3. COMPONENT :: PROCESSING LOADER

The only tolerable anomaly in the system that will possess pseudo-cyclical representations referencing the passage of time on the `setInterval()` chronological axis.

**Specific Parametric Rules for Brutalist Loader:**
1.  **Absolute ASCII Priority:** Instead of opaque GIF files or circular spin animations with dozens of `keyframes`, it outputs a simple array executed at `80ms` via raw JS.
2.  **Classic Vectorization (Array Base):** `['\|', '/', '-', '\\' ]`. Allocation of the mutable string simulates continuous machine movement operating background tasks without extensive GPU repaint overhead. Changing `inner-text` signals that the node (node thread) retains the CPU lock.
3.  **Strict Linear Bar (Bulk Data Alternative):** For requests reporting measurable front-end progress (`loaded / total`), the DOM implements a strict rectangular div. Advance by absolute steps (raw progress bar `border-radius: 0`), never a deceitful smoothed transition that hides locked frames of the TCP protocol.
