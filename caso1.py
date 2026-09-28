try:
    idade = int(input("Qual sua idade bem ? "))
    if idade >= 18:
       print("Liberado mona!")
    elif idade <= 0:
       print("erro na idade.")
    else:
       print("ohhh mucilon,maioridade não atingida")

except ValueError:
    print("Digite apenas números")
