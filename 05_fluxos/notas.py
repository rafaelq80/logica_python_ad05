nome = input("Digite o Nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 7:
  print(f"{nome} foi aprovado(a) com a média {media}")
elif media >= 5:
  print(f"{nome} está de exame com a média {media}")
else:
  print(f"{nome} foi reprovado(a) com a média {media}")

