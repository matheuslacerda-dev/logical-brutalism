# Logical Brutalism v1.4.0 :: Official Documentation

> "What does not resolve, does not exist."

A design system for high-information-density contexts. Every visual decision is justified by function. Technical truth is the highest form of aesthetics.

**Author:** Matheus Lacerda Ferreira  
**Origin:** Brazil :: Ilha Solteira  
**Status:** Living Document

---

## 00 :: Central Thesis and Origin

Logical Brutalism was not born in a café theorizing about aesthetics. It was born from necessity. In unstable environments, the only metric that never fails is logic. If plan X is executed, result Y is inevitable. This is not coldness; it is survival.

Just as brutalist architecture exposes concrete and rejects decorative cladding, Logical Brutalism exposes the logic of software. No visual layers that contradict function, no ornament without information.

| Approach | Criterion | Result |
| :--- | :--- | :--- |
| Minimalism | Remove until it looks elegant | Aesthetics by subtraction |
| Web Brutalism | Remove until it looks raw | Ugliness as statement |
| **Logical Brutalism** | **Remove until only function remains** | **Structural truth** |

---

## 01 :: The Three Axioms

Premises derived from how humans process information (Kahneman's System 1 and System 2).

* **Axiom I: Function Precedes Form.** An element exists to transmit information or guide action. If it does neither, it is cognitive noise. Affordances before signifiers.
* **Axiom II: Exposed Structure.** The logic of hierarchy and state must be readable in under 100ms. The system does not hide how it works.
* **Axiom III: Restriction as a Tool.** Fewer options = consistency. A palette of 6 tokens with rigid rules is superior to 20 colors without criteria.

---

## 02 :: The Five Pillars

1.  **Exposed Structure (Raw Code):** Logic does not hide behind unnecessary abstraction. Terminal, monospace, and ASCII are the language because everything boils down to data.
2.  **The Absolute Void (#0A0A0A):** The low-stimulus environment needed to focus. The silence of those who build robust systems against the noise of the world.
3.  **The Trigger Point (#FFB000):** The only concession to color. The deploy that works, the action that matters. Surgical, never decorative.
4.  **Calculated Coldness (The Persona):** Senior-level coldness. Does not get emotional about trendy frameworks. Chooses the tool, executes, delivers.
5.  **Texture and Authority:** Calculated imperfection. The grain over the digital that separates the software craftsman from the template robot.

---

## 03 :: Color System and Tokens

The palette is a system of attention hierarchy. Using a token outside its role breaks the logic.

### Theme 1: Void-First (Dark)
* `--color-void` **(#0A0A0A)**: Primary background. Absence of noise.
* `--color-amber` **(#FFB000)**: Unique action (P3 phosphor from 1970). Maximum one per screen. AAA contrast (10.81:1).
* `--color-surface` **(#1E1E1E)**: Card borders, context separation.
* `--color-text` **(#888888)**: Continuous reading. Avoids pure-white visual fatigue.
* `--color-white` **(#F0F0F0)**: Critical data, titles.
* `--color-error` **(#FF4444)**: Errors and alerts. Activates System 1 for immediate reading.

### Theme 2: Infinity-White (Light Extension)
* `--color-infinity` **(#E3E3E3)**: Industrial Concrete. Main background, bounces light without blinding.
* `--color-accent` **(#B35900)**: Oxidized Amber. Unique action calibrated for AAA contrast in light mode.
* `--color-surface` **(#CCCCCC)**: Drafting Board. Structural separation.
* `--color-text` **(#4D4D4D)**: Graphite HB. Scanning without fatigue.
* `--color-ink` **(#0A0A0A)**: Absolute Void. Critical ink for logical typography.
* `--color-error` **(#BE123C)**: Emergency Stop. Technical red, does not vibrate against gray.

---

## 04 :: Typography and Spacing

Two families. Rigid functional roles.

* `--font-struct` (**Iosevka Aile**): The Human Layer. Metrics for legibility. Use for continuous reading content.
* `--font-code` (**Iosevka**): The Logic Layer. Parsing code, IDs, timestamps, status. The voice of the system.

**Base Scale (rem = 16px):**
* Display: 2.5rem (40px) | Title: 1.375rem (22px) | Body: 1rem (16px) | Small: 0.875rem (14px) | Label/Code: 0.75rem (12px)

**Spacing (The Structural Silence):**
Tokens from `--space-1` (0.25rem) to `--space-6` (3rem) determine logical proximity. Elements of the same context stay close; different contexts demand spatial barriers.

---

## 05 :: Generative Principles (Execution Guidelines)

* **P-01 Color Follows State:** Identify the state (active, error, neutral) before the color.
* **P-02 Angle as Commitment:** `border-radius: 0`. The system does not soften reality.
* **P-03 Mono for Machine, Sans for Human:** Semantic distinction, not aesthetic.
* **P-04 Amber Once Per Screen:** Competition destroys hierarchy.
* **P-05 Space Is Silence:** Use spacing for logical relation, not to fill void.
* **P-06 Immediate Feedback:** `transition: none`. States are discrete. Smooth transition is machine hesitation.
* **P-07 ASCII Before Icon:** Textual symbols (`[+]`, `[x]`, `[>]`) reduce overhead and external dependency.

---

## 06 :: Core Component Anatomy

### Button
No transition. `min-height: 44px`. The primary state uses `--color-amber` on the background. Visible focus via `outline` offset.

### Error State (Maximum Honesty)
The 4 mandatory Norman layers, mapped with error border-left:
1.  **Code** (What failed) -> Iosevka + Error Color
2.  **Title** (Where it failed) -> Iosevka + White/Ink Color
3.  **Description** (Why it failed) -> Iosevka Aile + Text Color
4.  **Action** (What to do) -> Iosevka + Amber Color

### Loader
The only element where movement is allowed, because waiting feedback is function.
Loader via ASCII (`| / - \`) alternated via JS or strict linear bar.

---

## 07 :: Accessibility & Evaluation Criteria

Accessibility is consistency with Axiom I. The system has documented AAA and AA contrast (e.g., Amber over Void hits 10.81:1).

**Audit Checklist (If the answer is "No", the design failed):**
- [ ] Do all colors strictly belong to the 6 tokens?
- [ ] Does the most important component have the unique action token?
- [ ] Do interactive elements have `focus-visible` and 44px touch targets?
- [ ] Do raw data and system labels use Iosevka?
- [ ] **Blind Test:** If we remove color from the screen, does the information hierarchy survive on typography and space alone?

---

## Execution Manifesto

I build because I have something to deliver.

I reject gradients because visual transition implies state transition, and states are discrete.

I reject rounded borders because precision has edges.

I use monospace for system data because parsing requires alignment.

I use amber because one unambiguous signal is worth more than ten competitors.

I am not trying to impress. I am trying to reduce cognitive load.

The interface is logic made perceptible.
The structure is exposed.
The plan is solid.
The rest is noise.

Mission Status: **INEVITABLE.**
