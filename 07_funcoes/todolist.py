# Importa as cores e o código de redefinição usados para destacar o menu.
from cores import *

# Lista que guarda as tarefas enquanto o programa está em execução.
tarefas = []

# Exibe as opções disponíveis para o usuário.
def menu():
  print("\n" + FRENTE_AMARELO + "___MENU___" + RESET)
  print("1 - Adicionar Tarefa")
  print("2 - Listar Tarefas")
  print("3 - Remover Tarefa")
  print("4 - Sair")

# Pede uma descrição e acrescenta a nova tarefa ao final da lista.
def adicionarTarefa():
  tarefa = input("Digite o nome da tarefa: ")
  tarefas.append(tarefa)
  print("Tarefa Adicionada!")

# Exibe todas as tarefas numeradas ou informa quando a lista está vazia.
def listarTarefas():
  if len(tarefas) == 0:
    print("Nenhuma tarefa cadastrada")
  else:
    # enumerate(..., start=1) mostra números começando em 1,
    # como é mais natural para o usuário escolher uma tarefa.
    for numero, tarefa in enumerate(tarefas, start=1):
      print(numero, "-", tarefa)

# Mostra as tarefas e, se houver alguma, solicita qual deve ser removida.
def removerTarefa():
  listarTarefas()

  if len(tarefas) > 0:
    # A escolha é convertida para inteiro para permitir validar o número.
    numero = int(input("Digite o número da tarefa a remover: "))

    # As posições de uma lista Python começam em 0, mas a numeração
    # apresentada ao usuário começa em 1. Subtrair 1 converte a escolha
    # para o índice correspondente: por exemplo, a tarefa 1 está no índice 0.
    # pop remove essa tarefa da lista e retorna o valor removido.
    # Esta comparação encadeada verifica se o número escolhido está entre 1
    # e a quantidade de tarefas, incluindo os dois limites. É equivalente a
    # (1 <= numero) and (numero <= len(tarefas)); assim, só aceita uma tarefa
    # que realmente existe na lista.
    if 1 <= numero <= len(tarefas):
      tarefas.pop(numero - 1)
      print("Tarefa removida!")
    else:
      print("Número inválido")

# Inicializa a opção como texto vazio para iniciar o laço do menu.
opcao = ""

# Continua exibindo o menu até o usuário escolher a opção "4".
while opcao != "4":
  menu()
  # input sempre retorna o que foi digitado como texto.
  opcao = input("Escolha uma opção: ")

  # Executa a ação associada à opção digitada.
  if opcao == "1":
    adicionarTarefa()
  elif opcao == "2":
    listarTarefas()
  elif opcao == "3":
    removerTarefa()
  elif opcao == 4:
    # Esta condição compara texto com número; a opção "4" não entra aqui.
    print("Até logo!")
  else:
    print("Opção inválida!")