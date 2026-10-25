# Projeto 2 — A História Maluca (Mad Lib)

<div align="center"><img src="https://i.imgur.com/QsU3CUo.png" title="source: imgur.com" width="50%"/></div>

> Peça algumas palavras soltas ao usuário e encaixe todas elas em uma história pronta.

| | |
|---|---|
| **Tema** | Entrada de dados e texto |
| **Nível** | Iniciante |
| **O que você vai praticar** | Receber informações do usuário, guardá-las e combiná-las em um texto |

---

## Contexto

*Mad Lib* é um jogo de palavras. Uma pessoa pede ao grupo palavras soltas (um nome, um adjetivo, uma comida...) sem contar para que servem. Depois, ela encaixa tudo nos espaços em branco de uma história pronta, e o resultado costuma ser bem engraçado.

Neste projeto, o seu programa assume o papel de quem conduz o jogo.

---

## O que o programa deve fazer

1. Pedir ao usuário **sete informações**, uma de cada vez e **nesta ordem**:

   | Ordem | Informação |
   |:---:|---|
   | 1 | Nome |
   | 2 | Profissão |
   | 3 | Primeiro adjetivo |
   | 4 | Segundo adjetivo |
   | 5 | Primeira comida |
   | 6 | Segunda comida |
   | 7 | Um sentimento |

2. Montar a história abaixo, trocando cada trecho entre `<` e `>` pela informação correspondente.
3. Exibir a história completa na tela.

## Modelo da história

```
<1-Nome> começou hoje o seu primeiro curso na Generation Brasil. 
Está cursando a formação em <2-Profissão>. 
Achou a sua turma muito <3-Primeiro-Adjetivo> mas o instrutor era, no mínimo, <4-Segundo-Adjetivo>. No almoço, comeu <5-Primeira-Comida> e <5-Segunda-Comida> enquanto revisava as suas anotações. 
Ao final do dia, sente-se <7-Um-Sentimento>, mas tem a determinação de concluir a jornada.

```

## Exemplo

Se o usuário informar, nesta ordem:

```
Ana
analista de dados
animada
paciente
lasanha
suco
ansiosa
```

a história exibida deve ser:

```
Ana começou hoje o seu primeiro curso na Generation Brasil. 
Está cursando a formação em analista de dados. 
Achou a sua turma muito animada mas o instrutor era, no mínimo, paciente. 
No almoço, comeu lasanha e suco enquanto revisava as suas anotações. 
Ao final do dia, sente-se ansiosa, mas tem a determinação de concluir a jornada.
```

---

## Pontos de atenção

- **A ordem das perguntas importa.** Cada resposta precisa ir para o lugar certo da história.
- **A história deve aparecer como um único parágrafo**, sem quebras de linha no meio.
- **O texto precisa ficar idêntico ao modelo**: mesmas palavras, pontuação, espaços e letras maiúsculas e minúsculas. As partes fixas não podem ser alteradas.
- **As perguntas que você mostra ao usuário são livres.** Escreva do jeito que preferir.

> **Lembre-se:** este projeto é corrigido automaticamente, e computadores são muito literais. Qualquer diferença no texto, por menor que seja, conta como erro.