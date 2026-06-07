# 02 :: Sistema de Cores e Tokens

Os tokens CSS abaixo são a camada visual primária. São rígidos e não aceitam variações como `rgba()` sem justificativa extrema. Alterar um token sem motivo quebra a hierarquia global.

## Regra de Ouro

Nunca injete valores hexadecimais fixos diretamente no código. Nunca sobrescreva propriedades nativas com modificadores não listados. Use apenas as CSS Custom Properties abaixo.

## Tema 1: Void-First (Dark)

Este é o tema principal. Use em dashboards, ambientes de visualização controlada e ferramentas internas.

| CSS Token | Valor Hex | Função | Carga Visual |
| :--- | :--- | :--- | :--- |
| `--color-void` | `#0A0A0A` | Fundo primário. Base do vazio absoluto. | Mínima possível |
| `--color-amber` | `#FFB000` | Ponto de ação crítica (Gatilho P3). Limite: **máximo 1 elemento por tela**. Contraste sobre o void: `AAA (10.81:1)`. | Alerta máximo, imediato |
| `--color-surface` | `#1E1E1E` | Bordas de cards, painéis, separação de contexto. Profundidade `1` no eixo Z. | Neutro estrutural |
| `--color-text` | `#888888` | Texto de leitura longa. Reduz fadiga ocular em parágrafos. | Baixa |
| `--color-white` | `#F0F0F0` | Dados brutos, títulos de seção, output direto do sistema. | Moderada |
| `--color-error` | `#FF4444` | Falhas, timeouts, erros `4xx`/`5xx`. Ativa leitura imediata de urgência. | Crítica |

## Tema 2: Infinity-White (Light)

Opcional. Use apenas quando a luz ambiente for tão intensa que o tema escuro cause fadiga real.

* `--color-infinity`: `#E3E3E3` (Industrial Concrete)
* `--color-accent`: `#B35900` (Oxidized Amber — ajustado para manter contraste `AAA` no claro)
* `--color-surface`: `#CCCCCC` (Drafting Board — separação discreta de painéis)
* `--color-text`: `#4D4D4D` (Graphite HB — leitura longa sem cansaço)
* `--color-ink`: `#0A0A0A` (Absolute Void — dados críticos e absolutos, absorve 100% da atenção)
* `--color-error`: `#BE123C` (Emergency Stop — calibrado para não vibrar sobre o cinza)

## Tipografia

Uma família, dois pesos. Sem exceção. A partir da **v1.3**, o sistema migrou para **Iosevka** — uma fonte desenhada para densidade máxima de informação.

### 1. A Camada Humana
**Fonte:** `Iosevka Aile`  
**Token:** `--font-struct`  
**Uso:** Artigos, instruções, descrições, qualquer coisa que o usuário precise ler como texto.  
**Por que:** Mantém a densidade e clareza da família Iosevka, mas com proporções otimizadas para leitura contínua. Altura-x elevada e terminais abertos minimizam erros de leitura.

### 2. A Camada Lógica
**Fonte:** `Iosevka` (Mono)  
**Token:** `--font-code`  
**Uso:** Labels de ação, strings JSON, UUIDs, timestamps, tags de infraestrutura, código.  
**Por que:** Alinhamento vertical fixo. Cada caractere ocupa o mesmo espaço. Não há ambiguidade entre `1`, `I` e `l`. Identificação instantânea de um dado contra outro. A Iosevka foi desenhada especificamente para caber mais caracteres por linha sem perder legibilidade — essencial para dashboards de alta densidade.

## Escalas e Espaçamento

Base: `1rem` = `16px`.

**Tipografia (Tamanho / Altura da Linha):**
* `Display`: 2.5rem (40px) / `1.1`
* `Title`: 1.375rem (22px) / `1.3`
* `Body`: 1rem (16px) / `1.5`
* `Small`: 0.875rem (14px) / `1.5`
* `Label/Code`: 0.75rem (12px) / `1.0`

**Espaçamento (O Silêncio Estrutural):**
Margens declaram vizinhança; padding declara agrupamento (Lei de Gestalt no DOM):
* `--space-1` = `0.25rem` (4px): Ícone ao lado de texto
* `--space-2` = `0.5rem` (8px): Labels internos
* `--space-3` = `1rem` (16px): Bloco primário
* `--space-4` = `1.5rem` (24px): Componentes interdependentes
* `--space-5` = `2rem` (32px): Isolamento de seções
* `--space-6` = `3rem` (48px): Arquitetura macro, quebra de fluxo de leitura
