# 04 :: MATEMÁTICA Y ANATOMÍA CORE DE COMPONENTES

Todas las entidades subyacentes obedecen la macro-API de la "Verdad Estructural".

## 1. COMPONENTE :: BOTÓN 
Actuador puro.
*   **Geometría:** Base mínima bloqueada en `44px` para compatibilidad WCAG AAA de objetivos táctiles.
*   **Contorno (`outline`):** Declaración estática `outline: 2px solid var(--color-amber)` impuesta para garantizar el escaneo en tabbing absoluto sin compromisos opacos.
*   **Inmovilidad de Tiempo:** Animaciones transitorias anuladas `transition: none`.

## 2. COMPONENTE :: ESTADO DE ERROR EXTREMO
Anuladores estáticos de tostadas nativas efímeras. Estructura unida al `border-left: 4px solid error`.
*   **Capa 01 (Código):** Salida ex: `[ERR_503_FAIL]` -> Font Mono.
*   **Capa 02 (Título):** Contextualizador de instancia -> White, Font Mono.
*   **Capa 03 (Descripción):** Legibilidad Humana -> Text Color, Inter.
*   **Capa 04 (Acción):** Vector reparador. 

## 3. COMPONENTE :: LOADER ASCII
Se elimina el polímero del DOM vectorial rotativo, remplazándose con la mutabilidad bruta cronológica implementada por arreglos JavaScript (`['|', '/', '-', '\\' ]`) y operando a frecuencia de ~80ms.
