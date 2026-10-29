# Define uma função sem parâmetros que apenas exibe uma informação.
def sobre():
  print("Desenvolvido por: Rafael Queiróz")

# Define uma função que recebe o nome da turma e o ano e exibe esses dados.
def turma(turma, ano):
  print(f"Turma: {turma} - {ano}")

# Define uma função que recebe dois números e retorna a soma deles.
def somar(numero1, numero2):
  return numero1 + numero2

# Chama a função para exibir o nome do desenvolvedor.
sobre()
# Chama a função com a turma e o ano que serão exibidos.
turma("AD-05", 2026)

# Solicita dois valores ao usuário e converte as entradas para números decimais.
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Calcula a soma usando a função e guarda o valor retornado.
resultado = somar(numero1, numero2)
# Exibe a operação e o resultado.
print(f"A soma de {numero1} + {numero2} = {resultado}")