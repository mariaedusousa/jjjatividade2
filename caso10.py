numero = -10

while numero != 0:
    try:
        numero = int(input("Digite um numero: "))
        if numero == 0:
         print("Programa fechado pois você digitou 0.")

    except ValueError:
        print("Digite apenas números inteiros postivios!!!")
