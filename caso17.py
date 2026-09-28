idade = int(input("digitea idade do aluno: "))
curso = input("digite o nome do curso: ")
ano = int(input("digite o ano o ano: "))

if idade <= 0:
    print("idade inválida!")

elif curso.strip() == "":
    print("todos os campos são obrigatorios")

elif ano < 2020 or ano > 2026:
    print(" ano inválido!")

else:
    print("tudo certoooooo")
