# 05 :: Auditoria de Acessibilidade e Checklist Restrito (WCAG 2.1+)

No Brutalismo Lógico, acessibilidade não é "feature". É obediência direta ao Axioma I: **Função Precede Forma**. Uma interface que parte dos usuários não consegue usar é uma interface que falhou antes de existir.

A matemática da cor resolve ambiguidades para daltônicos, usuários com baixa visão e operadores em ambientes com muita luz.

## O Teorema dos Contrastes

Toda fonte sobre toda superfície precisa ser legível. O limite AAA é mantido em escrutínio:

1.  Ação primária (`--color-amber`: `#FFB000`) sobre o fundo (`--color-void`: `#0A0A0A`) produz **contraste de 10.81:1**, acima do mínimo AAA (`7.0:1`). Impossível passar despercebido.
2.  Texto regular (`--color-text`: `#888888`) sobre `#0A0A0A` mantém **5.13:1**, passando no AA (mínimo 4.5:1). Lê-se bem sem exigir atenção máxima.

## A Regra do "Teste Cego"

**Axioma Teste-Cego:**
Se na build local você aplicar um filtro `filter: grayscale(100%)` na tag `:root`, o sistema DEVE continuar navegável e hierárquico. A estrutura tipográfica e o espaçamento funcional (`--space`) devem ser suficientes para guiar o olho. Se a hierarquia sumir sem cor, o sistema estava usando cor para esconder lixo estrutural.

## Checklist Zero-Trust do Kernel Brutalista

Todo committer responde binariamente (TRUE/FALSE) antes de mergear. Um `FALSE` bloqueia o pipeline:

*   `[ ]` Todas as cores do componente vêm apenas dos `Tokens Globais` em `/docs/02-tokens.md`?
*   `[ ]` Existe zero concorrência pelo token de Ação (`--color-amber` ou `#FFB000` dark / `#B35900` light)? Ele mantém foco singular?
*   `[ ]` Falsos cognatos de foco com `outline: none` foram removidos? O `focus-visible` tem override customizado explícito em links e inputs?
*   `[ ]` Alvos táteis (`touch targets`) e nós de ativação cravam `min-height: 44px` nos elementos interativos?
*   `[ ]` Dados crus e labels do sistema usam `--font-code` (Mono), garantindo alinhamento vertical perfeito no render do browser?
*   `[ ]` A árvore ARIA HTML aplica semântica máxima, em particular `role="alert"` nas caixas de erro (Norman Layers)?
