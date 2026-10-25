# Solicita o nome do professor e guarda a resposta.
nome = input("Digite o seu nome: ")

# Lê quatro números e converte cada entrada para número decimal.
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))
numero4 = float(input("Digite o quarto número: "))

# Exibe o nome informado.
print(nome)

# Soma os quatro números.
resultado = numero1 + numero2 + numero3 + numero4

# Mostra a operação e o resultado em uma mensagem personalizada.
# Observe que foi utilzada uma f-string para inserir as variáveis na mensagem.
print(
    f"{numero1} mais {numero2} mais {numero3} mais {numero4},\nProfessor {nome} é muito fácil, é {resultado}"
)
