# BRUTALISMO LÓGICO v1.2.1 :: DOCUMENTAÇÃO OFICIAL

> "O que não resolve, não existe."

Um sistema de design para contextos de alta densidade de informação. Cada decisão visual é justificada por função. A verdade técnica é a maior forma de estética.

**AUTOR:** Matheus Lacerda Ferreira  
**ORIGEM:** Brasil :: Ilha Solteira  
**STATUS:** DOCUMENTO VIVO  

---

## 00 :: TESE CENTRAL E ORIGEM

O Brutalismo Lógico não nasceu em um café de Dublin teorizando sobre estética. Nasceu da necessidade. Em ambientes de instabilidade, a única métrica que não falha é a lógica. Se o plano X é executado, o resultado Y é inevível. Isso não é frieza, é sobrevivência.

Assim como a arquitetura brutalista expõe o concreto e recusa revestimento decorativo, o Brutalismo Lógico expõe a lógica do software. Sem camadas visuais que contradigam a função, sem ornamento sem informação.

| ABORDAGEM | CRITÉRIO | RESULTADO |
| :--- | :--- | :--- |
| Minimalismo | Remove até parecer elegante | Estética pela subtração |
| Brutalismo Web | Remove até parecer bruto | Feiura como statement |
| **Brutalismo Lógico** | **Remove até só restar função** | **Verdade estrutural** |

---

## 01 :: OS TRÊS AXIOMAS

As premissas derivadas de como humanos processam informação (Sistema 1 e Sistema 2 de Kahneman).

* **AXIOMA I: FUNÇÃO PRECEDE FORMA.** Um elemento existe para transmitir informação ou guiar ação. Se não faz nenhum dos dois, é ruído cognitivo. Affordances antes de signifiers.
* **AXIOMA II: ESTRUTURA EXPOSTA.** A lógica de hierarquia e estado deve ser legível em menos de 100ms. O sistema não esconde como funciona.
* **AXIOMA III: RESTRIÇÃO COMO FERRAMENTA.** Menos opções = consistência. Uma paleta de 6 tokens com regras rígidas é superior a 20 cores sem critério.

---

## 02 :: OS CINCO PILARES

1.  **Estrutura Exposta (Raw Code):** A lógica não se esconde atrás de abstração desnecessária. Terminal, monospace e ASCII são a linguagem porque tudo se resume a dados.
2.  **O Vazio Absoluto (#0A0A0A):** O ambiente de baixo estímulo necessário para focar. O silêncio de quem constrói sistemas robustos contra o ruído do mundo.
3.  **O Ponto de Gatilho (#FFB000 / #00FF00 original):** A única concessão à cor. O deploy que funciona, a ação que importa. Cirúrgico, nunca decorativo.
4.  **A Frieza Calculista (A Persona):** Frieza de sênior. Não se emociona com framework modinha. Escolhe a ferramenta, executa, entrega.
5.  **Textura e Autoridade:** Imperfeição calculada. O grão sobre o digital que separa o artesão do software do robô de template.

---

## 03 :: SISTEMA DE CORES E TOKENS

A paleta é um sistema de hierarquia de atenção. Usar um token fora do seu papel quebra a lógica.

### TEMA 1: VOID-FIRST (DARK)
* `--color-void` **(#0A0A0A)**: Fundo primário. Ausência de ruído.
* `--color-amber` **(#FFB000)**: Ação única (Fósforo P3 de 1970). Máximo um por tela. Contraste AAA (10.81:1).
* `--color-surface` **(#1E1E1E)**: Bordas de card, separação de contexto.
* `--color-text` **(#888888)**: Leitura contínua. Evita fadiga visual do branco puro.
* `--color-white` **(#F0F0F0)**: Dados críticos, títulos.
* `--color-error` **(#FF4444)**: Erros e alertas. Ativa Sistema 1 de leitura imediata.

### TEMA 2: INFINITY-WHITE (LIGHT EXTENSION)
* `--color-infinity` **(#E3E3E3)**: Industrial Concrete. Fundo principal, rebate luz sem ofuscar.
* `--color-accent` **(#B35900)**: Oxidized Amber. Ação única calibrada para contraste AAA no claro.
* `--color-surface` **(#CCCCCC)**: Drafting Board. Separação de estrutura.
* `--color-text` **(#4D4D4D)**: Graphite HB. Escaneamento sem fadiga.
* `--color-ink` **(#0A0A0A)**: Absolute Void. Tinta crítica para tipografia lógica.
* `--color-error` **(#BE123C)**: Emergency Stop. Vermelho técnico, não vibra contra o cinza.

---

## 04 :: TIPOGRAFIA E ESPAÇAMENTO

Duas famílias. Papéis funcionais rígidos.

* `--font-struct` (**Inter**): A Camada Humana. Métricas para legibilidade. Use para conteúdo de leitura contínua.
* `--font-code` (**JetBrains Mono**): A Camada Lógica. Parsing de código, IDs, timestamps, status. A voz do sistema.

**Escala Base (rem = 16px):**
* Display: 2.5rem (40px) | Title: 1.375rem (22px) | Body: 1rem (16px) | Small: 0.875rem (14px) | Label/Code: 0.75rem (12px)

**Espaçamento (O Silêncio Estrutural):**
Tokens de `--space-1` (0.25rem) a `--space-6` (3rem) determinam a proximidade lógica. Elementos do mesmo contexto ficam próximos; contextos diferentes exigem barreiras espaciais.

---

## 05 :: PRINCÍPIOS GERATIVOS (DIRETRIZES DE EXECUÇÃO)

* **P-01 COR SEGUE ESTADO:** Identifique o estado (ativo, erro, neutro) antes da cor.
* **P-02 ÂNGULO COMO COMPROMISSO:** `border-radius: 0`. O sistema não suaviza a realidade.
* **P-03 MONO PARA MÁQUINA, SANS PARA HUMANO:** Distinção semântica, não estética.
* **P-04 ÂMBAR UMA VEZ POR TELA:** Concorrência destrói hierarquia.
* **P-05 ESPAÇO É SILÊNCIO:** Use espaçamento para relação lógica, não para preencher vazio.
* **P-06 FEEDBACK IMEDIATO:** `transition: none`. Estados são discretos. Transição suave é hesitação da máquina.
* **P-07 ASCII ANTES DE ÍCONE:** Símbolos textuais (`[+]`, `[x]`, `[>]`) reduzem overhead e dependência externa.

---

## 06 :: ANATOMIA DE COMPONENTES CORE

### BOTÃO
Sem transição. `min-height: 44px`. O estado primário usa `--color-amber` no background. Focus visível via `outline` offset.

### ESTADO DE ERRO (Máxima Honestidade)
As 4 camadas de Norman obrigatórias, mapeadas com border-left error:
1.  **Código** (O que falhou) -> JetBrains Mono + Error Color
2.  **Título** (Onde falhou) -> JetBrains Mono + White/Ink Color
3.  **Descrição** (Por que falhou) -> Inter + Text Color
4.  **Ação** (O que fazer) -> JetBrains Mono + Amber Color

### LOADER
Único elemento com movimento permitido, pois feedback de espera é função.
Loader via ASCII (`| / - \`) alternado via JS ou barra linear estrita.

---

## 07 :: ACESSIBILIDADE & CRITÉRIOS DE AVALIAÇÃO

Acessibilidade é consistência com o Axioma I. O sistema possui contraste AAA e AA documentado (ex: Amber sobre Void bate 10.81:1).

**Checklist de Auditoria (Se a resposta for "Não", o design falhou):**
- [ ] Todas as cores pertencem estritamente aos 6 tokens?
- [ ] O componente mais importante tem o token de ação única?
- [ ] Elementos interativos possuem `focus-visible` e touch targets de 44px?
- [ ] Os dados crus e labels do sistema usam JetBrains Mono?
- [ ] **Teste Cego:** Se removermos a cor da tela, a hierarquia de informação sobrevive apenas via tipografia e espaço?

---

## MANIFESTO DE EXECUÇÃO

Construo porque tenho algo pra entregar.

Recuso gradientes porque transição visual implica transição de estado, e estados são discretos.

Recuso bordas arredondadas porque precisão tem arestas.

Uso monospace para dados do sistema porque parsing requer alinhamento.

Uso âmbar porque um sinal inequívoco vale mais que dez concorrentes.

Não estou tentando impressionar. Estou tentando reduzir carga cognitiva.

A interface é a lógica tornada perceptível.
A estrutura está exposta.
O plano é sólido.
O resto é ruído.

STATUS DA MISSÃO: **INEVITÁVEL.**
