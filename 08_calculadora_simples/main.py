# Avaliação de laboratório Python: Calculadora Básica
# Passo 1: Obter os valores de entrada com input()

# Lê os dois números e converte o texto digitado em número decimal (float)
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Lê o operador, como +, -, * ou /
operador = input("Digite o operador (+, -, * ou /): ")

# Variável para guardar o resultado final
resultado = None

# Passo 2: Decidir qual operação realizar
if operador == "+":
    resultado = num1 + num2
elif operador == "-":
    resultado = num1 - num2
elif operador == "*":
    resultado = num1 * num2
elif operador == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Não é possível dividir por zero"
else:
    resultado = "Operador inválido"

# Passo 3: Exibir o resultado
# Isso deixa a saída mais amigável para iniciantes, por exemplo 4 em vez de 4.0.
if isinstance(resultado, float) and resultado.is_integer():
    print(int(resultado))
else:
    print(resultado)
