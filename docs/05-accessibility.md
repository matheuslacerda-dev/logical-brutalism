# 05 :: Accessibility Audit and Restricted Checklist (WCAG 2.1+)

In Logical Brutalism, accessibility is not a "feature". It is direct obedience to Axiom I: **Function Precedes Form**. An interface that part of the users cannot use is an interface that failed before it existed.

Color mathematics resolves ambiguities for colorblind users, low-vision users, and operators in high-glare environments.

## The Contrast Theorem

Every font on every surface must be legible. The AAA limit is kept under scrutiny:

1.  Primary action (`--color-amber`: `#FFB000`) over background (`--color-void`: `#0A0A0A`) produces **contrast of 10.81:1**, above the AAA minimum (`7.0:1`). Impossible to go unnoticed.
2.  Regular text (`--color-text`: `#888888`) over `#0A0A0A` maintains **5.13:1**, passing AA (minimum 4.5:1). Reads well without demanding maximum attention.

## The "Blind Test" Rule

**Blind Test Axiom:**
If in the local build you apply a filter `filter: grayscale(100%)` to the `:root` tag, the system MUST remain navigable and hierarchical. The typographic structure and functional spacing (`--space`) must be enough to guide the eye. If hierarchy disappears without color, the system was using color to hide structural trash.

## Brutalist Kernel Zero-Trust Checklist

Every committer answers binarily (TRUE/FALSE) before merging. A `FALSE` blocks the pipeline:

*   `[ ]` Do all component colors come only from the `Global Tokens` in `/docs/02-tokens.md`?
*   `[ ]` Is there zero competition for the Action token (`--color-amber` or `#FFB000` dark / `#B35900` light)? Does it retain singular parametric focus?
*   `[ ]` Have false focus cognates with `outline: none` been removed? Does `focus-visible` have an explicit custom override on links and inputs?
*   `[ ]` Do tactile targets (`touch targets`) and activation nodes enforce `min-height: 44px` on interactive elements?
*   `[ ]` Do raw data and system labels use `--font-code` (Mono), guaranteeing perfect vertical alignment on browser render?
*   `[ ]` Does the ARIA HTML tree apply maximum semantics, in particular `role="alert"` on error boxes (Norman Layers)?
