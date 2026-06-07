# 01 :: Fundamentos e Axiomas

O Brutalismo Lógico é construído sobre três premissas simples. Todo componente do sistema deve segui-las. Não são sugestões — são a base de tudo.

## Os Três Axiomas

| ID | Axioma | O que significa | Por que importa |
| :--- | :--- | :--- | :--- |
| **I** | **Função Precede Forma** | Um elemento na tela existe para transmitir uma informação ou fazer o usuário agir. Se não faz nenhum dos dois, é poluição visual. | O cérebro processa o "para que serve" antes de pensar se é bonito. O usuário precisa entender a função em frações de segundo. |
| **II** | **Estrutura Exposta** | A hierarquia e o estado da aplicação devem ser óbvios em menos de 100ms. O sistema não pode esconder como funciona por baixo de camadas visuais. | Ambiguidade sobrecarrega a memória. Quando a estrutura é clara, o usuário aprende a usar sozinho. |
| **III** | **Restrição Como Ferramenta** | Menos escolhas = mais consistência. Uma paleta com 6 tokens bem definidos é melhor que 20 cores soltas sem regra. | Restrição não limita a criação. Ela direciona o foco do usuário para o que realmente importa. |

## Os Cinco Pilares

Esses pilares definem como o sistema é pensado e mantido.

### 1. Estrutura Exposta
A interface não esconde seus processos. Elementos que lembram terminais de computador — fontes `monospace`, grids rígidos, arranjos `ASCII` — não são nostalgia. São a forma mais direta de mostrar informação: um caractere tem largura fixa, dados alinhados em grid são encontrados instantaneamente pelo olho.

### 2. O Vazio Absoluto
O fundo da tela precisa anular todo ruído visual. A cor `#0A0A0A` drena emissões de luz desnecessárias, criando um zero visual sobre o qual as informações importantes operam.

### 3. O Ponto de Gatilho
A única cor que foge da escala de cinza. O âmbar (`#FFB000`) é inspirado nos monitores de fósforo P3 dos anos 1970. Ele aparece apenas para ações críticas no lado do cliente (`POST`, `PUT`, `DELETE`). A cor não decora; ela dispara ação.

### 4. A Frieza Calculista
O sistema rejeita modismos. A metodologia é: avalia a necessidade, usa a ferramenta testada, entrega o módulo documentado com cobertura total. Pragmatismo não se emociona, entrega a build.

### 5. Textura e Autoridade
O uso controlado de grids rígidos e "ruído estrutural" sobre componentes transmite solidez. É a confirmação de que o sistema foi construído com engenharia metódica, não com templates prontos de plataforma B2C.
