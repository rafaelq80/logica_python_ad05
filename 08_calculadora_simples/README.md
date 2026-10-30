# Projeto 4 — Calculadora Simples

> Receba dois números e uma operação, e mostre o resultado, como uma calculadora de bolso.

| | |
|---|---|
| **Tema** | Algoritmos |
| **Nível** | Iniciante |
| **O que você vai praticar** | Entrada e saída de dados, variáveis, tipos de dados, estruturas de dados e tomada de decisões |

---

## Contexto

Você já escreveu programas que cumprimentam pessoas, montam listas e contam até 1000. Agora é hora de reunir o que aprendeu e criar algo que as pessoas realmente usam no dia a dia: uma **calculadora**.

O desafio vai além de fazer contas. Uma boa calculadora também precisa reagir bem quando algo não faz sentido, como dividir por zero ou pedir uma operação que ela não conhece.

## O que o programa deve fazer

1. Pedir ao usuário, com a função `input()`, **três informações**, uma de cada vez e **nesta ordem**:

   | Ordem | Informação | Valores aceitos |
   |:---:|---|---|
   | 1 | Primeiro número | Qualquer número, inteiro ou decimal |
   | 2 | Segundo número | Qualquer número, inteiro ou decimal |
   | 3 | Operador | `+` (soma), `-` (subtração), `*` (multiplicação) ou `/` (divisão) |

2. Realizar a operação escolhida entre os dois números.
3. Exibir o resultado na tela.

## O que o programa deve exibir

| Situação | Saída esperada |
|---|---|
| O operador é válido e a conta pode ser feita | O valor do resultado, sem nenhum texto antes ou depois |
| Divisão em que o segundo número é zero | `Não é possível dividir por zero` |
| O operador informado não é um dos quatro aceitos | `Operador inválido` |

Detalhes importantes:

- Números decimais usam **ponto**, como em `2.5`.
- Nos casos de erro, o programa **não** deve exibir nenhum resultado.
- **A forma de escrever o valor é livre.** O que importa é que ele esteja correto. Por exemplo, `10` e `10.0` são aceitos, e `3.33` e `3.3333333333333335` também.
- O resultado (ou a mensagem de erro) deve ser a **última coisa exibida** pelo programa, em uma única linha.

> **Sugestão (opcional):** deixe a saída mais parecida com a de uma calculadora de verdade. Mostre os resultados inteiros sem casa decimal (`10` em vez de `10.0`). Se quiser ir além, limite também os decimais a **2 casas** (`3.33` em vez de `3.3333333333333335`). Isso não é obrigatório, mas deixa o resultado mais agradável de ler. Os exemplos abaixo mostram a saída da solução de referência, que mostra os inteiros sem casa decimal, mas não limita os decimais.

## Exemplos

| Entradas (na ordem) | O programa exibe |
|---|---|
| `8`, `2`, `+` | `10` |
| `3`, `5`, `-` | `-2` |
| `1.5`, `2`, `*` | `3` |
| `7`, `2`, `/` | `3.5` |
| `10`, `3`, `/` | `3.3333333333333335` |
| `10`, `0`, `/` | `Não é possível dividir por zero` |
| `5`, `3`, `%` | `Operador inválido` |

## Antes de programar

Pegue papel e caneta (ou uma ferramenta de desenho) e crie um **fluxograma** da sua calculadora:

- Quais informações entram?
- Quais decisões o programa precisa tomar?
- O que acontece em cada caminho possível?

Programar com o caminho já desenhado deixa o código mais limpo e facilita encontrar erros.

## Pontos de atenção

- **A ordem das perguntas importa.** O primeiro número vem antes do segundo número, e o operador vem por último.
- **Considere que o usuário sempre digitará números válidos** nos campos de número. Você só precisa tratar os casos de erro descritos acima.
- **Neste projeto, não crie funções próprias.** Resolva tudo com o que você já estudou.
- **O texto das mensagens de erro precisa ser idêntico ao da tabela**: mesmas palavras, acentos, pontuação, espaços e letras maiúsculas e minúsculas.
- **As perguntas que você mostra ao usuário são livres.** Escreva do jeito que preferir.

> **Lembre-se:** este projeto é corrigido automaticamente, e computadores são muito literais. Qualquer diferença nas mensagens, por menor que seja, conta como erro.
