# 03 :: Generative Principles and Execution Guidelines

Front-end development follows seven rules. A Pull Request that breaks any of them is automatically rejected.

## P-01 :: Color Follows State

No color is chosen by taste. Before applying `background-color` or `color`, define the functional state: neutral, warning, blocked, active? Only then inject the token. Decorative without function is forbidden.

## P-02 :: Angle as Commitment

Base CSS rule: `* { border-radius: 0 !important; }`. The digital operates on Cartesian grids (`X` and `Y`). Curves create unnecessary anti-aliasing and give a false sense of softness where the system is rigid. A 90° angle is explicit structural commitment.

## P-03 :: Mono for Machine, Sans for Human

The restriction forces the brain to switch modes. When the user sees `--font-code` (Iosevka Mono), they know that data demands analytical attention. When they see `--font-struct` (Iosevka Aile), they know they can read fluidly. Mixing the roles is like mixing physical and application layers in the OSI model.

## P-04 :: Amber Once Per Screen

Multiple amber points compete with each other and destroy visual hierarchy. When the system presents the main fork `(Next Node)`, the `--color-amber` token must dominate the screen alone. If there is competition, the user hesitates.

## P-05 :: Space Is Silence

Modules do not float without logic. If you use `var(--space-1)`, you are declaring intrinsic proximity — the brain reads it as a single object. Distributing voids randomly (e.g., `justify-content: space-evenly`) without criteria is a logical model failure. The screen's white is a sound barrier.

## P-06 :: Immediate Feedback

Parametric determination: `* { transition: none !important; animation: none !important; }` (except for the Standard Loader Component).

State machines transition at clock time. Artificial delay in CSS distorts system reliability. Clicking and reacting must have delta T tending to zero. States are discrete: `[1 | 0]`.

## P-07 :: ASCII Before Icon

Anti-dependency logic on heavy assets (SVGs, React-icons, Font Awesome).

Standard vectors:
- Close: `[x]`
- Expand/Collapse: `[+]` / `[-]`
- Procedural Action: `[>]` or `->`

Page load drops, the browser skips extra requests, and the parser emulates POSIX/Unix interfaces that never go out of style.
