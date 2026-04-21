# LOGICAL BRUTALISM v1.1.1 :: OFFICIAL DOCUMENTATION

> "If it doesn't solve a problem, it doesn't exist."

A design system for high-density information contexts. Every visual decision is justified by function. Technical truth is the highest form of aesthetics.

**AUTHOR:** Matheus Lacerda Ferreira  
**ORIGIN:** Brazil :: Ilha Solteira  
**DESTINATION:** Cork, Ireland :: MTU  
**STATUS:** LIVING DOCUMENT  

---

## 00 :: CENTRAL THESIS AND ORIGIN

Logical Brutalism was not born in a Dublin cafe theorizing about aesthetics. It was born out of necessity. In environments of instability, the only metric that doesn't fail is logic. If plan X is executed, result Y is inevitable. This isn't coldness; it's survival.

Just as brutalist architecture exposes concrete and refuses decorative coating, Logical Brutalism exposes software logic. No visual layers that contradict function, no ornament without information.

| APPROACH | CRITERION | RESULT |
| :--- | :--- | :--- |
| Minimalism | Removes until it looks elegant | Aesthetics through subtraction |
| Web Brutalism | Removes until it looks raw | Ugliness as a statement |
| **Logical Brutalism** | **Removes until only function remains** | **Structural Truth** |

---

## 01 :: THE THREE AXIOMS

Premises derived from how humans process information (Kahneman's System 1 and System 2).

* **AXIOM I: FUNCTION PRECEDES FORM.** A DOM node exists solely to transmit data or prompt an action. If it does neither, it constitutes cognitive noise. Affordances before signifiers.
* **AXIOM II: EXPOSED STRUCTURE.** The topology and hierarchical tree of the application state must be readable in `t < 100ms`. The framework cannot cover internal processes.
* **AXIOM III: CONSTRAINT AS A TOOL.** Input choice reduction = Output consistency maximization. A design matrix consisting of 6 mathematically controlled tokens generates superior architecture to systems of 20+ ungrounded colors.

---

## 02 :: THE FIVE PILLARS

1.  **Exposed Structure (Raw Code):** Logic does not hide behind unnecessary abstraction. Terminal, monospace, and ASCII are the language because everything boils down to data.
2.  **Absolute Void (#0A0A0A):** The low-stimulus environment required for focus. The silence of those who build robust systems against world noise.
3.  **The Trigger Point (#FFB000 / Original #00FF00):** The only concession to color. The deploy that works, the action that matters. Surgical, never decorative.
4.  **Calculated Coldness (The Persona):** Senior coldness. Does not get emotional over trendy frameworks. Chooses the tool, executes, delivers.
5.  **Texture and Authority:** Calculated imperfection. The grain over digital that separates the software craftsman from the template-bot.

---

## 03 :: COLOR SYSTEM AND TOKENS

The palette is a hierarchy of attention system. Using a token outside its designated role breaks the logic.

### THEME 1: VOID-FIRST (DARK)
* `--color-void` **(#0A0A0A)**: Primary background. Absence of noise.
* `--color-amber` **(#FFB000)**: Singular action (P3 Phosphor from 1970). Max one per screen. AAA Contrast (10.81:1).
* `--color-surface` **(#1E1E1E)**: Card boundaries, context separation.
* `--color-text` **(#888888)**: Continuous reading. Prevents visual fatigue from pure white.
* `--color-white` **(#F0F0F0)**: Critical data, headers.
* `--color-error` **(#FF4444)**: Errors and alerts. Activates System 1 for immediate reading.

### THEME 2: INFINITY-WHITE (LIGHT EXTENSION)
* `--color-infinity` **(#E3E3E3)**: Industrial Concrete. Primary background, bounces light without glaring.
* `--color-accent` **(#B35900)**: Oxidized Amber. Singular action calibrated for AAA contrast in light mode.
* `--color-surface` **(#CCCCCC)**: Drafting Board. Structural separation.
* `--color-text` **(#4D4D4D)**: Graphite HB. Fatigue-free scanning.
* `--color-ink` **(#0A0A0A)**: Absolute Void. Critical ink for logical typography.
* `--color-error` **(#BE123C)**: Emergency Stop. Technical red, does not vibrate against gray.

---

## 04 :: TYPOGRAPHY AND SPACING

Two families. Strict functional roles.

* `--font-struct` (**Inter**): The Human Layer. Metrics for readability. Use for continuous reading content.
* `--font-code` (**JetBrains Mono**): The Logical Layer. Code parsing, IDs, timestamps, status. The voice of the system.

**Base Scale (rem = 16px):**
* Display: 2.5rem (40px) | Title: 1.375rem (22px) | Body: 1rem (16px) | Small: 0.875rem (14px) | Label/Code: 0.75rem (12px)

**Spacing (Structural Silence):**
Tokens from `--space-1` (0.25rem) to `--space-6` (3rem) dictate logical proximity. Elements within the same context remain close; different contexts require spatial barriers.

---

## 05 :: GENERATIVE PRINCIPLES (EXECUTION GUIDELINES)

* **P-01 COLOR FOLLOWS STATE:** Identify the state (active, error, neutral) before the color.
* **P-02 ANGLE AS COMMITMENT:** `border-radius: 0`. The system does not soften reality.
* **P-03 MONO FOR MACHINE, SANS FOR HUMAN:** Semantic distinction, not aesthetic.
* **P-04 AMBER ONCE PER SCREEN:** Concurrency destroys hierarchy.
* **P-05 SPACE IS SILENCE:** Use spacing for logical relation, not to fill emptiness.
* **P-06 IMMEDIATE FEEDBACK:** `transition: none`. States are discrete. Smooth transitions mean machine hesitation.
* **P-07 ASCII BEFORE ICON:** Textual symbols (`[+]`, `[x]`, `[>]`) reduce overhead and external dependencies.

---

## 06 :: CORE COMPONENT ANATOMY

### BUTTON
No transition. `min-height: 44px`. Primary state uses `--color-amber` background. Focus visible via `outline` offset.

### ERROR STATE (Maximum Honesty)
Mandatory 4 Norman layers, mapped with border-left error:
1.  **Code** (What failed) -> JetBrains Mono + Error Color
2.  **Title** (Where it failed) -> JetBrains Mono + White/Ink Color
3.  **Description** (Why it failed) -> Inter + Text Color
4.  **Action** (What to do) -> JetBrains Mono + Amber Color

### LOADER
The only element allowed movement, because wait feedback is function.
Loader via ASCII (`| / - \`) alternated via JS, or strict linear bar.

---

## 07 :: ACCESSIBILITY & EVALUATION CRITERIA

Accessibility is consistency with Axiom I. The system has documented AAA and AA contrast (e.g., Amber on Void hits 10.81:1).

**Audit Checklist (If the answer is "No", the design has failed):**
- [ ] Do all colors belong strictly to the 6 tokens?
- [ ] Does the most important component hold the singular action token?
- [ ] Do interactive elements have `focus-visible` and 44px touch targets?
- [ ] Do raw data and system labels use JetBrains Mono?
- [ ] **Blind Test:** If color is stripped from the screen, does the information hierarchy survive purely via typography and spacing?

---

## EXECUTION MANIFESTO

I build because I have something to deliver.
I refuse gradients because visual transitions imply state transitions, and states are discrete.
I refuse rounded borders because precision has edges.
I use monospace for system data because parsing requires alignment.
I use amber because one unequivocal signal is worth more than ten competitors.
I am not trying to impress. I am trying to reduce cognitive load.

The interface is logic rendered perceptible.
The structure is exposed.
The plan is solid.
Everything else is noise.

MISSION STATUS: **INEVITABLE.**
