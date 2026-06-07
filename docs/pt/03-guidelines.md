# 03 :: Princípios Gerativos e Diretrizes de Execução

O desenvolvimento front-end segue sete regras. Uma Pull Request que quebra qualquer uma delas é rejeitada automaticamente.

## P-01 :: Cor Segue Estado

Nenhuma cor é escolhida por gosto. Antes de aplicar `background-color` ou `color`, defina o estado funcional: neutro, aviso, bloqueado, ativo? Só depois injete o token. Decorativo sem função é proibido.

## P-02 :: Ângulo Como Compromisso

Regra CSS base: `* { border-radius: 0 !important; }`. O digital opera em grids cartesianos (`X` e `Y`). Curvas criam anti-aliasing desnecessário e dão a falsa sensação de suavidade onde o sistema é rígido. Ângulo de 90° é compromisso estrutural explícito.

## P-03 :: Mono Para Máquina, Sans Para Humano

A restrição força o cérebro a mudar de modo. Quando o usuário vê `--font-code` (Iosevka Mono), sabe que aquele dado exige atenção analítica. Quando vê `--font-struct` (Iosevka Aile), sabe que pode ler fluidamente. Misturar os papéis é como misturar camadas físicas e de aplicação no modelo OSI.

## P-04 :: Âmbar Uma Vez Por Tela

Múltiplos pontos âmbar competem entre si e destroem a hierarquia visual. Quando o sistema apresenta a bifurcação principal `(Next Node)`, o token `--color-amber` deve dominar sozinho a tela. Se houver concorrência, o usuário hesita.

## P-05 :: Espaço É Silêncio

Módulos não flutuam sem lógica. Se você usa `var(--space-1)`, está declarando proximidade intrínseca — o cérebro lê como um único objeto. Distribuir vazios aleatoriamente (ex: `justify-content: space-evenly`) sem critério é falha de modelo lógico. O branco da tela é barreira sonora.

## P-06 :: Feedback Imediato

Determinação paramétrica: `* { transition: none !important; animation: none !important; }` (exceto o Componente Loader Padrão).

Máquinas de estado transicionam no tempo de clock. Delay artificial em CSS distorce a confiabilidade do sistema. Clicar e reagir deve ter delta T tendendo a zero. Estados são discretos: `[1 | 0]`.

## P-07 :: ASCII Antes de Ícone

Lógica anti-dependência de assets pesados (SVGs, React-icons, Font Awesome).

Vetores padrão:
- Fechar: `[x]`
- Expandir/Recolher: `[+]` / `[-]`
- Ação Processual: `[>]` ou `->`

A carga da página cai, o browser dispensa requests extras, e o parser emula interfaces POSIX/Unix que nunca saem de moda.
