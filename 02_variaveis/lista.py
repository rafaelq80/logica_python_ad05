# Cria uma lista inicial de nomes.
lista = [
    "Gabriel",
    "Vinicius",
    "Jussara",
    "Priscilla",
    "Maurício",
    "Josiane",
    "Diogo",
    "Felipe",
]

# Exibe todos os nomes da lista.
print(lista)

# Acessa o quarto item; os índices começam em zero.
print(lista[3])

# Lê um nome digitado pelo usuário e o adiciona ao final da lista.
lista.append(input("Digite um nome: "))

# Exibe a lista já com o novo nome.
print(lista)

# Remove o item de índice 2 (o terceiro nome da lista).
lista.pop(2)

# Exibe a lista após a remoção.
print(lista)
