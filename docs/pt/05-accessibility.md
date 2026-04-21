# 05 :: AUDITORIA DE ACESSIBILIDADE E CHECKLIST RESTRITO (WCAG 2.1+)

O Brutalismo Lógico rejeita o conceito de que acessibilidade é "feature". Requisitos estritos de processamento e legibilidade não são opções amáveis, correspondem diretamente à obediência cega ao Axioma I (Função Precede Forma). A matemática aplicada à taxonomia da cor resolve ambiguidades passíveis de falhas cognitivas nos usuários de extremidade, daltônicos, e hard-users em ambientes altamente ofuscantes no mercado de trabalho B2B.

## A TEOREMA DOS CONTRASTES
Toda fonte sobre toda superfície precisa renderizar sem degradação. O limite AAA é mantido em escrutínio sobre os tokens mestres do design system. A conformidade não exige abstração visual via "cores mais bonitinhas"; exige matemática linear:

1.  A ação primária (`--color-amber`: `#FFB000`) calculada sobre o painel base (`--color-void` dark mode: `#0A0A0A`) produz um **Contraste de Proporção de 10.81:1**, batendo folgado o mínimo exigido AAA (`7.0:1`) da WCAG. Impossível passar despercebido e sem fadiga excessiva.
2.  Textos regulares (com `--color-text`: `#888888`) projetados sobre a mesma superfície em `#0A0A0A` mantém performance na base exigida de conformidade AA (min 4.5:1), gerando `5.13:1`. Absorve impacto de leitura mas exalta identificadores.

## A REGRA DO "TESTE CEGO" (DESVIO DA CROMA EM ZERO)

A regra final das especificações estipula e encerra instabilidades focais de interface:

**Axioma Teste-Cego:**
Se na build em ambiente local as camadas CSS do front-end forem sobrestadas por um filtro global na tag `:root` contendo `filter: grayscale(100%);`, o sistema DEVE sobreviver inalterado hierarquicamente em capacidade de indexação ocular. A leitura estrutural garante fluidez no uso exclusivo do eixo das ordenadas (y) da arquitetura tipográfica e do espaçamento funcional (`--space`), revelando se as cores esconderam ou camuflaram lixo subestrutural de navegação.

## AUDITORIA MACRO DO KERNEL BRUTALISTA: CHECKLIST ZERO-TRUST
Qualquer committer no processo de engatar componentes no `master/main` reponde binariamente (TRUE/FALSE) à verificação imperativa. O preenchimento com `FALSE` bloqueia por regra o pipeline da Request:

*   `[ ]` Todas e cada uma das especificações de cor do componente pertencem apenas aos arrays de `Tokens Globais` declarados em `/docs/02-tokens.md`?
*   `[ ]` Existe zero concorrência tática para o token Ação (`--color-amber` ou `#FFB000` dark / `#B35900` light)? Retém o foco paramétrico universal singular?
*   `[ ]` Falsos cognatos de foco apagados com `outline: none` foram expurgados? O `focus-visible` tem override customizado explícito nos links e form inputs?
*   `[ ]` Os limites modulares (`touch targets` e nós de ativação HTML) cravam rigorosos `min-height: 44px` nas matrizes ativas (botoes de formulários preenchidos)?
*   `[ ]` O parser de dados crus obedece perfeitamente ao instanciamento de `--font-code` (Mono), garantido alinhamento por vertical no render da engine de layoting do browser?
*   `[ ]` A árvore ARIA HTML aciona a restrição máxima semântica exigida, em particular o uso de blocos dinâmicos e injeções Reactivas/JS aplicando o invólucro do atributo `role="alert"` em caixas referenciadas no Item de Erros (Norman Layers)?
