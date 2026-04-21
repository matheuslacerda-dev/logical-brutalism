# 02 :: SISTEMA DE CORES E ESPECIFICAÇÃO DE TOKENS

Os tokens CSS a seguir formam a camada de dados primordial. São rígidos e não suportam extensões como variações de canal alfa (`rgba()`) que não passem por justificação extrema em merge requests. A alteração indevida de um token destrói a hierarquia global.

## DIRETRIZES DE USO DOS TOKENS GLOBAIS
É expressamente proibido injetar valores fixos hexadecimais in-line no código ou sobrescrever as propriedades nativas através de modificadores atômicos não listados. Utilize uso restrito das "CSS Custom Properties" mapeadas abaixo:

### TEMA 1: VOID-FIRST (DARK)
Arquitetura primária para ambientes de visualização controlados e dashboards complexos.

| CSS TOKEN | VALOR HEX | PROPOSIÇÃO E FUNÇÃO ARQUITETURAL | OVERHEAD COGNITIVO |
| :--- | :--- | :--- | :--- |
| `--color-void` | `#0A0A0A` | Fundo primário não nulo. Base de cálculo do vazio absoluto. | Mínimo absoluto |
| `--color-amber` | `#FFB000` | Ponto crítico de ação (Gatilho P3). Limitação: `Max(n=1)` por Viewport. Avaliação de Contraste text over void: `AAA (10.81:1)`. | Imediato de Máxima Alerta |
| `--color-surface` | `#1E1E1E` | Delimitador de context-box e painéis. Define profundidade = `1` no Z-Axis. | Neutro Estrutural |
| `--color-text` | `#888888` | Buffer de leitura estendido. Diminui a carga ocular no processamento de parágrafos. | Baixo |
| `--color-white` | `#F0F0F0` | Dados brutos que não exigem ação, cabeçalhos de section e output direto do sistema. | Primário Moderado |
| `--color-error` | `#FF4444` | Falha nos workers, timeout, `4xx` ou `5xx`. Bypass ativo no córtex pré-frontal via engajamento direto de "urgência". | Prioridade Crítica |

### TEMA 2: INFINITY-WHITE (LIGHT EXTENSION)
Opcional, acionado exclusivamente em circunstâncias extrínsecas que imponham fadiga luminosa extrema. O fundo não atinge luminosidade total (`#FFFFFF`), garantindo sobrevida de retinas.

* `--color-infinity`: `#E3E3E3` (Industrial Concrete).
* `--color-accent`: `#B35900` (Oxidized Amber. O ajuste lumínico necessário para manter o contraste `AAA`).
* `--color-surface`: `#CCCCCC` (Drafting Board. Diferenciação discreta de paneis).
* `--color-text`: `#4D4D4D` (Graphite HB. Semântica alinhada com cor de leitura longa).
* `--color-ink`: `#0A0A0A` (Absolute Void. Letras cruciais e data points absolutos, absorve 100% da radiação visual focada).
* `--color-error`: `#BE123C` (Emergency Stop. Valor em `hsl()` corrigido para não vibrar visualmente no canvas cinza).

## TIPOGRAFIA

As fontes não emitem sentimentos; processam "arrays" de letras. Duas instâncias paramétricas:

### 1. A Camada Humana
**Font-Family Definida:** `Inter`
**Variável CSS:** `--font-struct`
**Aplicação:** Artigos, instruções macro, meta descrições.
**Justificativa:** Desenvolvida microscopicamente para leitura digital ótima baseada em alturas-x elevadas e abertura nos terminais, minimiza as taxas de erros no ato de sacada retiniana pela página.

### 2. A Camada Lógica
**Font-Family Definida:** `JetBrains Mono`
**Variável CSS:** `--font-code`
**Aplicação:** Componentes iterativos, labels de ações, strings JSON, UUIDs, carimbos temporais, tags analíticas da infraestrutura.
**Justificativa:** Os eixos de alinhamento vertical da Mono bloqueiam a leitura fluida mas garantem `100%` de identificação paramétrica `O(1)` ocular de um dado contra outro. Ausência de ambiguidade nas ligaduras: `1`, `I`, `l` não competem.

## ESCALAS LINEARES E VETORES DE COMPOSIÇÃO

As dimensões operam através de predeterminações matemáticas, base fundamental `1rem` = `16px`.

**Escala Tipográfica (Tamanho / Line-Height):**
* `Display`: 2.5rem (40px) / `1.1`
* `Title`: 1.375rem (22px) / `1.3`
* `Body`: 1rem (16px) / `1.5`
* `Small`: 0.875rem (14px) / `1.5`
* `Label/Code`: 0.75rem (12px) / `1.0`

**Espaçamento Espacial (O Silêncio Estrutural):**
As margens declaram vizinhança lógica; um "padding" determina agrupamento funcional (Lei de Gestalt implementada no DOM):
* `--space-1` = `0.25rem` (4px): Ligações subatômicas (ex: ícone ao lado de texto no box)
* `--space-2` = `0.5rem` (8px): Distância base em labels.
* `--space-3` = `1rem` (16px): Identidade primária de bloco.
* `--space-4` = `1.5rem` (24px): Divisão de componentes interdependentes.
* `--space-5` = `2rem` (32px): Isolamento de Seções.
* `--space-6` = `3rem` (48px): Arquitetura Macro, rompimento do fluxo de leitura do usuário.
