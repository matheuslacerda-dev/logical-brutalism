# LOGISCHER BRUTALISMUS v1.2.0 :: OFFIZIELLE DOKUMENTATION

> "Was kein Problem löst, existiert nicht."

Ein Designsystem für Kontexte mit hoher Informationsdichte. Jede visuelle Entscheidung ist durch Funktion gerechtfertigt. Technische Wahrheit ist die höchste Form der Ästhetik.

**AUTOR:** Matheus Lacerda Ferreira  
**STATUS:** LEBENDIGES DOKUMENT  

---

## 00 :: ZENTRALE THESE UND URSPRUNG

Logischer Brutalismus entstand nicht in einem Dubliner Café aus Ästhetik-Theorien. Er entstand aus der Notwendigkeit. In instabilen Umgebungen ist Logik die einzige Metrik, die nicht versagt. Wenn Plan X ausgeführt wird, ist Ergebnis Y unvermeidlich. Das ist keine Kälte; es ist Überleben.

Genauso wie die brutalistische Architektur den Beton offenlegt und dekorative Oberflächen verweigert, legt der Logische Brutalismus die Softwarelogik offen. Keine visuellen Schichten, die der Funktion widersprechen, kein Ornament ohne Information.

| ANSATZ | KRITERIUM | ERGEBNIS |
| :--- | :--- | :--- |
| Minimalismus | Entfernt, bis es elegant aussieht | Ästhetik durch Subtraktion |
| Web-Brutalismus | Entfernt, bis es roh aussieht | Hässlichkeit als Statement |
| **Logischer Brutalismus** | **Entfernt, bis nur noch Funktion bleibt** | **Strukturelle Wahrheit** |

---

## 01 :: DIE DREI AXIOME

Prämissen abgeleitet davon, wie Menschen Informationen verarbeiten (Kahnemans System 1 und System 2).

* **AXIOM I: FUNKTION GEHT DER FORM VORAUS.** Ein DOM-Knoten existiert ausschließlich, um Daten zu übertragen oder eine Aktion einzuleiten. Wenn er beides nicht tut, stellt er kognitives Rauschen dar. Affordanzen vor Signifikanten.
* **AXIOM II: OFFENGELEGTE STRUKTUR.** Die Topologie und der hierarchische Baum des Anwendungszustands müssen in `t < 100ms` lesbar sein. Das Framework darf interne Prozesse nicht verdecken.
* **AXIOM III: BESCHRÄNKUNG ALS WERKZEUG.** Reduzierung der Eingabeauswahl = Maximierung der Ausgabekonsistenz. Eine Designmatrix aus 6 mathematisch gesteuerten Tokens generiert eine bessere Architektur als Systeme mit über 20 unbegründeten Farben.

---

## 02 :: DIE FÜNF SÄULEN

1.  **Offengelegte Struktur (Raw Code):** Die Logik versteckt sich nicht hinter unnötiger Abstraktion. Terminal, Monospace und ASCII sind die Sprache, weil alles auf Daten hinausläuft.
2.  **Absolute Leere (#0A0A0A):** Die für den Fokus notwendige reizarme Umgebung. Das Schweigen derer, die robuste Systeme gegen den Lärm der Welt bauen.
3.  **Der Triggerpunkt (#FFB000 / Original #00FF00):** Das einzige Zugeständnis an die Farbe. Das funktionierende Deploy, die Aktion, auf die es ankommt. Chirurgisch, niemals dekorativ.
4.  **Kalkulierte Kälte (Die Senior-Persona):** Senior-Kälte. Keine Emotionen bei trendigen Frameworks. Wählt das Werkzeug, führt aus, liefert.
5.  **Textura und Autorität:** Kalkulierte Unvollkommenheit. Die Körnung über dem Digitalen, die den Software-Handwerker vom Vorlagen-Bot trennt.

---

## 03 :: FARBSYSTEM UND TOKENS

Die Palette ist ein hierarchisches System der Aufmerksamkeit. Die Verwendung eines Tokens außerhalb seiner zugewiesenen Rolle bricht die Logik.

### THEMA 1: VOID-FIRST (DUNKEL)
* `--color-void` **(#0A0A0A)**: Primärer Hintergrund. Abwesenheit von Rauschen.
* `--color-amber` **(#FFB000)**: Einzige Aktion (P3-Phosphor von 1970). Maximal einer pro Bildschirm. AAA-Kontrast (10.81:1).
* `--color-surface` **(#1E1E1E)**: Kartenränder, Kontexttrennung.
* `--color-text` **(#888888)**: Kontinuierliches Lesen. Verhindert visuelle Ermüdung durch reines Weiß.
* `--color-white` **(#F0F0F0)**: Kritische Daten, Überschriften.
* `--color-error` **(#FF4444)**: Fehler und Warnungen. Aktiviert System 1 für sofortiges Lesen.

### THEME 2: INFINITY-WHITE (HELLE ERWEITERUNG)
* `--color-infinity` **(#E3E3E3)**: Industrie-Beton. Primärer Hintergrund.
* `--color-accent` **(#B35900)**: Oxidierter Bernstein. Singular action calibrada.
* `--color-surface` **(#CCCCCC)**: Reißbrett. Trennung der Strukturen.
* `--color-text` **(#4D4D4D)**: Grafit HB. Scannen ohne Ermüdung.
* `--color-ink` **(#0A0A0A)**: Absolute Leere. Tinta für logische Typografie.
* `--color-error` **(#BE123C)**: Nothalt. Technisches Rot.

---

## 04 :: TYPOGRAFIE UND ABSTÄNDE

* `--font-struct` (**Inter**): Die Menschliche Schicht. Für kontinuierliches Lesen.
* `--font-code` (**JetBrains Mono**): Die Logische Schicht. Code-Parsing, IDs, Zeitstempel.

**Basis-Skala (rem = 16px):**
* Display: 2.5rem | Title: 1.375rem | Body: 1rem | Small: 0.875rem | Label: 0.75rem

**Abstände (Strukturelle Stille):**
Tokens von `--space-1` (0.25rem) bis `--space-6` (3rem) diktieren die logische Nähe.

---

## 05 :: GENERATIVE PRINZIPIEN (AUSFÜHRUNGSRICHTLINIEN)

* **P-01 FARBE FOLGT ZUSTAND:** Bestimmen Sie den Zustand vor der Farbe.
* **P-02 WINKEL ALS VERPFLICHTUNG:** `border-radius: 0`. Das System entschärft die Realität nicht.
* **P-03 MONO FÜR DIE MASCHINE, SANS FÜR DEN MENSCHEN:** Semantische Unterscheidung, nicht ästhetisch.
* **P-04 BERNSTEIN EINMAL PRO BILDSCHIRM:** Konkurrenz zerstört Hierarchie.
* **P-05 RAUM IST STILLE:** Nutzen Sie Abstand für logische Relation.
* **P-06 SOFORTIGES FEEDBACK:** `transition: none`. Statusübergänge sind diskret.
* **P-07 ASCII VOR DEM ICON:** Textsymbole (`[+]`, `[x]`, `[>]`) reduzieren Latenz.

---

## 06 :: KERNKOMPONENTEN-ANATOMIE

### BUTTON
Keine Transition. `min-height: 44px`. Focus sichtbar via `outline` offset.

### FEHLERZUSTAND (Maximale Ehrlichkeit)
Eine Kombination aus den 4 Norman-Schichten:
1.  **Code** (Was schiefgelaufen ist) -> Mono + Error Color
2.  **Titel** (Wo es passiert ist) -> Mono + White
3.  **Beschreibung** (Warum es passiert ist) -> Inter + Text Color
4.  **Aktion** (Was zu tun ist) -> Mono + Amber Color

MISSIONSSTATUS: **UNVERMEIDLICH.**
