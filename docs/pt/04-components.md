# 04 :: Anatomia e Matemática dos Componentes Core

Todo componente deve respeitar a API da "Verdade Estrutural". A padronização não varia entre micro-frontends ou rotas. Subcomponentes herdados acoplam regras universais.

## 1. Botão Primário e Secundário

O nódulo executor. O ponto onde o usuário dispara uma requisição HTTP ou reverte um estado.

*   **Geometria:** `min-height` travado em `44px`. Conformidade WCAG para alvos táteis em mobile.
*   **Transição:** `none`. Estados são discretos.
*   **Borda:** `1px solid var(--color-surface)` no secundário, sem exceção.
*   **Focus Visível:** Omitir `outline` é falha grave. Use `outline: 2px solid var(--color-amber)` com `outline-offset: 2px` para tracking perceptível no tabbing do teclado.
*   **Primário:** `background-color: var(--color-amber)` com texto `#0A0A0A` e fonte `--font-code` (`Iosevka`). Transmite ordem direta, robótica.

## 2. Estado de Erro (Máxima Honestidade)

Modais nativos ou toasts convencionais escondem o problema. O componente de erro do Brutalismo Lógico expõe quatro camadas simultâneas, com `border-left: 4px solid var(--color-error)`:

| Camada | O que comunica | Renderização |
| :---: | :--- | :--- |
| **01** | **Código da Falha** (O que quebrou?) | `font-family: var(--font-code); color: var(--color-error);` Ex: `[ERR_503_DB_TIMEOUT]` |
| **02** | **Título do Roteiro** (Onde estamos?) | `font-family: var(--font-code); color: var(--color-white);` (Dark Mode) |
| **03** | **Descrição Orgânica** (Por que aconteceu?) | `font-family: var(--font-struct); color: var(--color-text);` Única camada que admite linguagem natural (Iosevka Aile). |
| **04** | **Vetor da Ação** (O que fazer agora?) | `font-family: var(--font-code); color: var(--color-amber);` Ex: `> INICIAR NOVO REQUEST`. Clicável, com outline no hover. |

## 3. Loader de Processamento

A única anomalia do sistema que pode ter movimento — porque indicar que algo está acontecendo é função, não decoração.

**Regras Específicas:**
1.  **ASCII Primeiro:** Em vez de GIFs ou spinners CSS com dezenas de `keyframes`, use um array simples atualizado a cada `80ms` via JS: `['|', '/', '-', '\']`. O `inner-text` muda e sinaliza que a thread está ocupada, sem overhead de repaint GPU.
2.  **Barra Linear (Alternativa):** Para uploads/downloads com progresso mensurável, use uma div retangular estrita. Avanço por degraus absolutos (`border-radius: 0`), sem transição suavizada que esconda frames travados do TCP.
