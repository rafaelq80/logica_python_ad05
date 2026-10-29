# Função sem retorno e sem parâmetros
def sobre():
  print("Desenvolvido por: Rafael Queiróz")

# Função sem retorno e com parâmetros
def turma(turma, ano):
  print(f"Turma: {turma} - {ano}")

# Função com retorno e com parâmetros
def somar(numero1, numero2):
  return numero1 + numero2

sobre()
turma("AD-05", 2026)

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

resultado = somar(numero1, numero2)
print(f"A soma de {numero1} + {numero2} = {resultado}")