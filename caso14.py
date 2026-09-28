print("cadastre produtos")

preco = input("Digite o preço do produto chef: ").strip()

if preco == "":
    print("Erro: o preço não foi informado.")
else:
    try:
        preco = float(preco)
        print("Preço informado: R$", preco)
    except ValueError:
        print("digite um preço válido.")
