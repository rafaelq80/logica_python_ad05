# Coleta as informações que serão usadas para completar a história.
nome = input("Qual é o seu nome? ")
profissao = input("Qual é a sua profissão? ")
adjetivo1 = input("Digite o primeiro adjetivo: ")
adjetivo2 = input("Digite o segundo adjetivo: ")
comida1 = input("Digite a primeira comida: ")
comida2 = input("Digite a segunda comida: ")
sentimento = input("Digite um sentimento: ")

# Monta e exibe a história combinando as respostas fornecidas.
print(
    nome + " começou hoje o seu primeiro curso na Generation Brasil. "
    "Está cursando a formação em " + profissao + ". "
    "Achou a sua turma muito " + adjetivo1 +
    " mas o instrutor era, no mínimo, " + adjetivo2 + ". "
    "No almoço, comeu " + comida1 + " e " + comida2 +
    " enquanto revisava as suas anotações. "
    "Ao final do dia, sente-se " + sentimento + ", mas tem a determinação de concluir a jornada."
)

# Aspas triplas permitem escrever a f-string em várias linhas e preservar as quebras de linha.
print(f"""{nome} começou hoje o seu primeiro curso na Generation Brasil.
Está cursando a formação em {profissao}.
Achou a sua turma muito {adjetivo1}, mas o instrutor era, no mínimo, {adjetivo2}.
No almoço, comeu {comida1} e {comida2} enquanto revisava as suas anotações.
Ao final do dia, sente-se {sentimento}, mas tem a determinação de concluir a jornada.""")