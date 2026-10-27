# Projeto 3 — FizzBuzz

> Conte de 1 a 1000, mas troque certos números por palavras.

| | |
|---|---|
| **Tema** | Repetição e tomada de decisões |
| **Nível** | Iniciante |
| **O que você vai praticar** | Repetir uma tarefa muitas vezes e escolher o que mostrar em cada repetição |

---

## Contexto

FizzBuzz é um jogo de contagem muito usado para ensinar crianças a dividir. Os jogadores contam em voz alta, em sequência, mas em certos números precisam dizer uma palavra no lugar do número. Quem errar sai da roda.

Ele também é um clássico da programação: um problema pequeno, mas que pede atenção a cada detalhe.

## As regras do jogo

Contando a partir do **1**, para cada número:

| Se o número for... | O programa mostra... |
|---|---|
| divisível por **3** | `Fizz` |
| divisível por **5** | `Buzz` |
| divisível por **3 e por 5 ao mesmo tempo** | `Fizzbuzz` |
| nenhum dos casos acima | o próprio número |

> **Atenção à grafia:** no caso do 3 e do 5 juntos, a palavra é escrita **`Fizzbuzz`**, com o **b minúsculo**.

## O que o programa deve fazer

Exibir o resultado do jogo para **todos os números de 1 até 1000**, **um por linha**, em ordem crescente.

## Exemplo

Nos primeiros 15 números, a saída é:

```
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
Fizzbuzz
```

A saída completa continua seguindo as mesmas regras, até chegar ao 1000.

## Pontos de atenção

- **O programa não pede nenhuma informação ao usuário.** Ele apenas exibe a sequência.
- **A saída deve conter somente a sequência.** Sem títulos, mensagens extras ou linhas a mais.
- **O último número da sequência é o 1000**, nem antes nem depois.
- **Letras maiúsculas e minúsculas contam.** `Fizz`, `Buzz` e `Fizzbuzz` devem ser escritos exatamente assim.

> **Lembre-se:** este projeto é corrigido automaticamente, e computadores são muito literais.