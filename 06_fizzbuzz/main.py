for numero in range(1, 1001):
    if numero % 15 == 0:
        print("Fizzbuzz")
    elif numero % 3 == 0:
        print("Fizz")
    elif numero % 5 == 0:
        print("Buzz")
    else:
        print(numero)