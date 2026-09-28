def calcular_compra():
    try:
        valor = float(input("Digite o valor da compra: R$ "))

        if valor < 0:
            print("Valor inválido!")
        elif valor <= 100:
            desconto = 0
            valor_final = valor
        else:
            desconto = valor * 0.10
            valor_final = valor - desconto

        if valor >= 0:
            print(f"\nValor da compra: R$ {valor:.2f}")
            print(f"Desconto: R$ {desconto:.2f}")
            print(f"Valor final: R$ {valor_final:.2f}")

    except ValueError:
        print("Digite um valor numérico válido!")


calcular_compra()
