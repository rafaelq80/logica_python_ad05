nomes_aprovados = ["João", "Maria", "Pedro", "Mariana"]

nome = input("Digite o seu nome: ").strip()

if nome.lower() in [nome_lista.lower() for nome_lista in nomes_aprovados]:
  print(f"{nome} aprovado(a)!")
else:
  print(f"{nome} reprovado(a)!")