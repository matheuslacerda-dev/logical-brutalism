# 04 :: ANATOMIA E MATEMÁTICA DOS COMPONENTES CORE

Todo componente deve respeitar estritamente a API da "Verdade Estrutural". A padronização não sofre variações entre micro-frontends ou rotas de páginas. Subcomponentes herdados acoplam regras universais.

## 1. COMPONENTE :: BOTÃO PRIMÁRIO E SECUNDÁRIO

Trata-se do nódulo executor. O atuador principal do usuário para engatar requisição HTTP ou reverter estado mutável.

*   **Geometria Obrigatória:** A altura computada do `bounding-box` (`min-height`) precisa travar fixamente em `44px` seguindo conformidade total WCAG de alvos táteis em ambientes mobile.
*   **CSS `transition`:** Totalmente nulo (`none`).
*   **Declarações de Border:** Border primária se aplica como 1px sólido (`border: 1px solid var(--color-surface)`), sem exceção.
*   **Focus State Exposto:** Omitir outline é falha severa em Brutalismo Lógico. A injeção na subclasse requer no mínimo `outline: 2px solid var(--color-amber)` acompanhado de `outline-offset: 2px` para criar tracking perceptível no "tabbing" do teclado por eng. assistivas.
*   **Aparência Primária:** `background-color: var(--color-amber)` e cor do font ajustada a `#0A0A0A` via token de alto contraste no Light System ou fixo dark, sempre mapeando `--font-code` (`JetBrains Mono`). Transmite ordem robótica direta.

## 2. COMPONENTE :: ESTADO DE ERRO (MÁXIMA HONESTIDADE)

Os modais nativos ou blocos de toasts convencionais geram dissimulação e não reportam rastreabilidade. Componentes de falha encapsulam quatro camadas de Norman simultaneamente expostas de forma brutalista ao lado do `border-left: 4px solid var(--color-error)`:

| ID LAYER | DESCRITIVO FUNCIONAL | ESPECIFICAÇÃO DE RENDERIZAÇÃO ESTILIZADA |
| :---: | :--- | :--- |
| **01** | **Código da Falha** (O que falhou no server/browser?) | CSS: `font-family: var(--font-code); color: var(--color-error);` ex: `[ERR_503_DB_TIMEOUT]` (String formatada). |
| **02** | **Título do Roteiro** (Em qual instância de negócio se encontra?) | CSS: `font-family: var(--font-code); color: var(--color-white);` (Dark Mode). |
| **03** | **A Descrição Orgânica** (Por que ocorreu o evento?) | CSS: `font-family: var(--font-struct); color: var(--color-text);` Apenas esta string admite verbosidade natural em língua humana (Inter). |
| **04** | **Vetor da Ação** (O comando de recovery / try-catch front) | CSS: `font-family: var(--font-code); color: var(--color-amber);` ex: `> INICIAR NOVO REQUEST`. Clicável instintivamente via outline hover. |

## 3. COMPONENTE :: LOADER DE PROCESSAMENTO

A única anomalia tolerável do sistema que possuirá representações pseudo-cíclicas que remetem à passagem no eixo cronológico de `setInterval()`.

**Regras Paramétricas Específicas do Loader Brutalista:**
1.  **Prioridade Absoluta ASCII:** Em lugar de arquivos GIF opacos ou spin animations circulares com dezenas de `keyframes`, itula-se um simples output de array executado a `80ms` via JS bruto.
2.  **Vetorização Clássica (Array Base):** `['\|', '/', '-', '\\' ]`. A alocação da string mutável simula movimento contínuo da máquina operando background tasks sem overhead de repaint GPU extenso. O `inner-text` varia e sinaliza que o nó (node thread) está retendo o lock da CPU.
3.  **Barra Linear Estrita (Alternativa de Bulk Data):** Para requisições que reportam progresso mensurável no front (`loaded / total`), o DOM implementa uma div retangular estrita. Avanço por degraus absolutos (progress bar bruta `border-radius: 0`), jamais transição suavizada enganadora que oculta frames trancados do protocolo tcp.
