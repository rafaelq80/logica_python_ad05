senha_correta = "turmaad05"
tentativas = 0
acertou = False

while tentativas < 3:
    senha = input("Digite a senha: ")
    tentativas += 1

    if senha == senha_correta:
        acertou = True
        break

    print("Errou!\n")

if acertou:
    print("Acesso Liberado!")
else:
    print("Número de tentativas excedido. Acesso bloqueado!")