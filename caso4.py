while True:
    try:
        preco = float(input("Digite o preço: ").strip())
        break
    except ValueError:
        print("Digite um valor numéricooooo e de preferencia valido")

print("Preço:", preco)
