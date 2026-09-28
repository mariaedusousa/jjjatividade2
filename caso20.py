
try:
    nome = input("Nome do aluno: ").strip()
    idade = int(input("Idade: "))

    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))

    # Validação
    if nome == "":
        print("Erro: o nome não pode ficar vazio.")

    elif idade < 0:
        print("Erro: idade inválida.")

    elif nota1 < 0 or nota1 > 10:
        print("Erro: a nota 1 deve estar entre 0 e 10.")

    elif nota2 < 0 or nota2 > 10:
        print("Erro: a nota 2 deve estar entre 0 e 10.")

    elif nota3 < 0 or nota3 > 10:
        print("Erro: a nota 3 deve estar entre 0 e 10.")

    else:
        media = (nota1 + nota2 + nota3) / 3

        print("\n=== RESULTADO ===")
        print("Aluno:", nome)
        print("Idade:", idade)
        print("Média:", round(media, 2))

        if media >= 7:
            print("aprovado divuuuuuu")
        elif media >= 5:
            print("recuperação charaaaa")
        else:
            print("reprovado chara")

except ValueError:
    print("digite valores numéricos válidos.")
