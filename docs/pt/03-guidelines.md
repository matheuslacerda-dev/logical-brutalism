# 03 :: PRINCÍPIOS GERATIVOS E DIRETRIZES DE EXECUÇÃO

O desenvolvimento front-end é governado através desses sete processadores mnemônicos inquebráveis. Uma Pull Request que ofenda um princípio gerativo é estaticamente rejeitada, assumindo falha de integridade.

## P-01 :: COR SEGUE ESTADO (COLOR_FOLLOWS_STATE)
Nenhuma propriedade `background-color` ou `color` obedece a anseios estéticos. Deve-se avaliar a precondição na State Machine: estado "neutro", estado "aviso", estado "bloqueado"? Apenas e após isso há injeção de classes de token. Decorativos são anti-matemáticos.

## P-02 :: ÂNGULO COMO COMPROMISSO (BORDER_RADIUS_ZERO)
Regra primária CSS: `* { border-radius: 0 !important; }`. O sistema digital opera em malhas quadriculares por padrão nativo cartesiano (`X` e `Y`). Simular curvas introduz anti-aliasing ineficiente e cria percepções psicológicas de suavização sobre instâncias que falham catastroficamente no kernel. O ângulo de 90° explicita compromisso estrutural rígido.

## P-03 :: MONO PARA MÁQUINA, SANS PARA HUMANO (SEMANTIC_DISTINCTION)
A restrição da diretiva determina que o cérebro humano mude de estado automático. O bloco visual em `--font-code` imediatamente informa que o dado exige escrutínio analítico e tomada de decisão. O conteúdo em `--font-struct` engaja absorção passiva de leitura contínua. Misturar suas aplicações equivale a mesclar as camadas física e de aplicação no modelo OSI da interface.

## P-04 :: ÂMBAR UMA VEZ POR TELA (AMBER_SINGULARITY)
Múltiplas submissões conflitam fluxos. Quando o sistema apresenta ao usuário a bifurcação primária para proceder `(Next Node)`, o token `--color-amber` tem a obrigação de dominar isoladamente a tela. Uma concorrência com o mesmo token em dois pontos destruirá imediatamente a indexação hierárquica mental e inserirá inércia decisória.

## P-05 :: ESPAÇO É SILÊNCIO (SPACE_IS_SILENCE)
Módulos não flutuam aleatoriamente. Se `var(--space-1)` é invocado, declarou-se proximidade intrínseca; as variáveis computam como um único objeto sintático em arrays do cérebro de quem lê. Em contrapartida, justificar layout apenas distribuindo vazios irrestritamente caracteriza falha de modelo lógico (ex `justify-content: space-evenly`). O branco da tela dita a barreira sonora.

## P-06 :: FEEDBACK IMEDIATO (NO_TRANSITION)
Determinação paramétrica: `* { transition: none !important; animation: none !important; }` (A exceção é alocada ao Componente Loader Padrão).
Máquinas de estado finito executam suas transições de estado no tempo de clock sem retardamento artificial. Um processamento CSS simulando curvas bézier via tempo atrasa intencionalmente o pipeline e distorce a confiabilidade do sistema. Interfaces estéreis exigem mudanças instantâneas. Clicar e reagir possui um delta T mínimo tendendo a `0`.

## P-07 :: ASCII ANTES DE ÍCONE (ASCII_FIRST_METRIC)
Lógica anti-dependência de assets estáticos (ex. SVG pesados, bibliotecas React-icons, font-awesome).
Vetores:
- Fechar Instância: `[x]`
- Extensão em Accordion: `[+]` / `[-]`
- Ação Processual: `[>]` ou `->`
A carga da página decai, o render browser dispensa request no DOM virtual, e o parser emula interfaces POSIX/Unix que nunca depreciam a estética informacional base.
