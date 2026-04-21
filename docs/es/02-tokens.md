# 02 :: SISTEMA DE COLORES Y ESPECIFICACIONES DE TOKENS

Capa de datos primordial inflexible, sin soporte a valores alfa erráticos.

## DIRECTRICES DE USO
No emplear declaraciones inline. Uso estricto de las CSS Custom Properties de diccionario:

### TEMA 1: VOID-FIRST (DARK)
| CSS TOKEN | VALOR HEX | PROPOSICIÓN ARQUITECTÓNICA |
| :--- | :--- | :--- |
| `--color-void` | `#0A0A0A` | Vacío absoluto. |
| `--color-amber` | `#FFB000` | Punto de acción (Max=1). Contraste: `AAA (10.81:1)`. |
| `--color-surface` | `#1E1E1E` | Delimitador paramétrico. `Z-Axis=1`. |
| `--color-text` | `#888888` | Buffer de lectura larga. |
| `--color-white` | `#F0F0F0` | Títulos y strings directos de sistema. |
| `--color-error` | `#FF4444` | Fallos críticos y urgencias (Sistema 1). |

## TIPOGRAFÍA

### 1. La Capa Humana (`--font-struct`: Inter)
Métricas dirigidas a lecturas continuas mediante alturas X dominantes. Previene la degradación en los barridos retinianos.

### 2. La Capa Lógica (`--font-code`: JetBrains Mono)
Impide la ligadura morfológica abstracta, procesando cadenas en base visual de matriz cartesiana `O(1)`.

## ESPACIOS (`--space-1` a `--space-6`)
Implementa las leyes absolutas de la Gestalt mediante orden DOM, variando proximidades desde `4px` al macro buffer de `48px`.
