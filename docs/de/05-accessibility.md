# 05 :: ZUGÄNGLICHKEITS-AUDIT (WCAG 2.1+)

## DAS KONTRAST THEOREM
Barrierefreiheit stellt nicht nur eine Funktion dar; sie entspricht dem Axiom I.
`--color-amber` berechnet auf `--color-void` erzielt eine **Kontrastrate von 10.81:1** - die normative AAA Grenze liegt bei `7.0:1`.

## DER "BLINDTEST" (CROMATISCHE NULLABWEICHUNG)
Wendet der Architekt den Filter `filter: grayscale(100%);` am Wurzelknoten `:root` an, darf das System den Anwender nicht behindern. Topologie über Zeichenfolge muss siegreich sein.

## MACRO AUDIT: ZERO-TRUST CHECKLIST
(FALSCH blockiert die Integration im Haupt-Branch):
*   `[ ]` Ist jede Auszeichnung eine registrierte Farbvariable aus `/docs/02-tokens.md`?
*   `[ ]` Konkurriert der bernsteinfarbene Trigger mit einem gleichwertigen visuellen Punkt?
*   `[ ]` Besteht die Höhe interaktiver Elemente von mindestens `44px`?
*   `[ ]` Besitzen Fehlermeldungen die strikte `role="alert"` Kapselung und verwenden Monospace für Datenströme?
