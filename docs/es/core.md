# BRUTALISMO LÓGICO v1.2.1 :: DOCUMENTACIÓN OFICIAL

> "Lo que no resuelve, no existe."

Un sistema de diseño para contextos de alta densidad de información. Cada decisión visual está justificada por su función. La verdad técnica es la mayor forma de estética.

**AUTOR:** Matheus Lacerda Ferreira  
**ESTADO:** DOCUMENTO VIVO  

---

## 00 :: TESIS CENTRAL Y ORIGEN

El Brutalismo Lógico no nació en un café de Dublín teorizando sobre estética. Nació de la necesidad. En entornos de inestabilidad, la única métrica que no falla es la lógica. Si el plan X se ejecuta, el resultado Y es inevitable. Esto no es frialdad; es supervivencia.

Al igual que la arquitectura brutalista expone el hormigón y rechaza revestimientos, el Brutalismo Lógico expone la lógica del software. Sin capas visuales que contradigan la función, sin ornamento sin información.

| ENFOQUE | CRITERIO | RESULTADO |
| :--- | :--- | :--- |
| Minimalismo | Remueve hasta parecer elegante | Estética por sustracción |
| Brutalismo Web | Remueve hasta parecer crudo | Fealdad como declaración |
| **Brutalismo Lógico** | **Remueve hasta que solo quede función** | **Verdad Estructural** |

---

## 01 :: LOS TRES AXIOMAS

Premisas derivadas de cómo los humanos procesan información (Sistema 1 y Sistema 2 de Kahneman).

* **AXIOMA I: LA FUNCIÓN PRECEDE A LA FORMA.** Un nodo DOM existe únicamente para transmitir datos o instar a una acción. Si no hace ninguna de las dos cosas, constituye ruido cognitivo. Affordances antes de signifiers.
* **AXIOMA II: ESTRUCTURA EXPUESTA.** La topología y el árbol jerárquico del estado de la aplicación deben ser legibles en `t < 100ms`. El marco no puede enmascarar los procesos internos.
* **AXIOMA III: LA RESTRICCIÓN COMO HERRAMIENTA.** Reducción de la entrada de opciones = Maximización de la coherencia de salida. Una matriz de diseño compuesta por 6 tokens controlados matemáticamente genera una arquitectura superior a sistemas de más de 20 colores sin criterio.

---

## 02 :: LOS CINCO PILARES

1.  **Estructura Expuesta (Raw Code):** La lógica no se esconde tras abstracciones innecesarias. Terminal, monoespaciado y ASCII son el lenguaje porque todo se reduce a datos.
2.  **El Vacío Absoluto (#0A0A0A):** El entorno de bajo estímulo necesario para concentrarse. El silencio de quienes construyen sistemas robustos contra el ruido del mundo.
3.  **El Punto de Gatillo (#FFB000 / Original #00FF00):** La única concesión al color. El deploy que funciona, la acción que importa. Quirúrgico, nunca decorativo.
4.  **La Frialdad Calculada (La Persona):** Frialdad de nivel senior. No se emociona con frameworks de moda. Elige la herramienta, ejecuta, entrega.
5.  **Textura y Autoridad:** Imperfección calculada. El grano sobre lo digital que separa al artesano de software del robot de plantillas.

---

## 03 :: SISTEMA DE COLORES Y TOKENS

La paleta es un sistema jerárquico de atención. Usar un token fuera de su rol rompe la lógica.

### TEMA 1: VOID-FIRST (OSCURO)
* `--color-void` **(#0A0A0A)**: Fondo primario. Ausencia de ruido.
* `--color-amber` **(#FFB000)**: Acción singular (Fósforo P3 de 1970). Máximo uno por pantalla. Contraste AAA (10.81:1).
* `--color-surface` **(#1E1E1E)**: Bordes de tarjetas, separación de contextos.
* `--color-text` **(#888888)**: Lectura continua. Previene la fatiga visual del blanco puro.
* `--color-white` **(#F0F0F0)**: Datos críticos, títulos.
* `--color-error` **(#FF4444)**: Errores y alertas. Activa el Sistema 1 para lectura inmediata.

### TEMA 2: INFINITY-WHITE (EXTENSIÓN CLARA)
* `--color-infinity` **(#E3E3E3)**: Hormigón Industrial. Fondo principal.
* `--color-accent` **(#B35900)**: Ámbar Oxidado. Acción singular calibrada para contraste AAA en claro.
* `--color-surface` **(#CCCCCC)**: Tablero de dibujo. Separación de estructuras.
* `--color-text` **(#4D4D4D)**: Grafito HB. Escaneo sin fatiga.
* `--color-ink` **(#0A0A0A)**: Vacío Absoluto. Tinta crítica para tipografía lógica.
* `--color-error` **(#BE123C)**: Parada de Emergencia. Rojo técnico.

---

## 04 :: TIPOGRAFÍA Y ESPACIADO

* `--font-struct` (**Inter**): La Capa Humana. Úsese para contenido de lectura continua.
* `--font-code` (**JetBrains Mono**): La Capa Lógica. Parseo de código, IDs, timestamps, estados.

**Escala Base (rem = 16px):**
* Display: 2.5rem | Title: 1.375rem | Body: 1rem | Small: 0.875rem | Label: 0.75rem

**Espaciado (Silencio Estructural):**
Tokens desde `--space-1` (0.25rem) hasta `--space-6` (3rem) dictan la proximidad lógica.

---

## 05 :: PRINCIPIOS GENERATIVOS (DIRECTRICES DE EJECUCIÓN)

* **P-01 EL COLOR SIGUE AL ESTADO:** Identifica el estado antes que el color.
* **P-02 EL ÁNGULO COMO COMPROMISO:** `border-radius: 0`. El sistema no suaviza la realidad.
* **P-03 MONO PARA MÁQUINA, SANS PARA HUMANO:** Distinción semántica, no estética.
* **P-04 ÁMBAR UNA VEZ POR PANTALLA:** La concurrencia destruye la jerarquía.
* **P-05 EL ESPACIO ES SILENCIO:** Usa espaciado para relación lógica, no para llenar vacíos.
* **P-06 FEEDBACK INMEDIATO:** `transition: none`. Las transiciones suaves implican vacilación de la máquina.
* **P-07 ASCII ANTES QUE ICONO:** Símbolos de texto (`[+]`, `[x]`, `[>]`) reducen latencia.

---

## 06 :: ANATOMÍA DE COMPONENTES CORE

### BOTÓN
Sin transición. `min-height: 44px`. Focus visible vía `outline` offset.

### ESTADO DE ERROR (Máxima Honestidad)
Las 4 capas de Norman:
1.  **Código** (Qué falló) -> Mono + Error Color
2.  **Título** (Dónde falló) -> Mono + White
3.  **Descripción** (Por qué falló) -> Inter + Text Color
4.  **Acción** (Qué hacer) -> Mono + Amber Color

### LOADER
Loader vía ASCII (`| / - \`) iterado vía JS JS, o barra lineal estricta.

ESTADO DE LA MISIÓN: **INEVITABLE.**
