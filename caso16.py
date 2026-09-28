import os

ARQUIVO = "alunos.txt"


def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    idade = input("Digite a idade: ")
    curso = input("Digite o curso: ")

    try:
        arquivo = open(ARQUIVO, "a", encoding="utf-8")
        arquivo.write(f"{nome};{idade};{curso}\n")
        arquivo.close()

        print("\nAluno cadastrado com sucesso!")

    except Exception as erro:
        print("Erro ao cadastrar aluno:", erro)


def listar_alunos():
    try:
        arquivo = open(ARQUIVO, "r", encoding="utf-8")

        print("\n===== ALUNOS CADASTRADOS =====")

        conteudo = arquivo.readlines()

        if len(conteudo) == 0:
            print("Nenhum aluno cadastrado.")
        else:
            for aluno in conteudo:
                dados = aluno.strip().split(";")

                print(f"Nome: {dados[0]}")
                print(f"Idade: {dados[1]}")
                print(f"Curso: {dados[2]}")
                print("-----------------------------")

        arquivo.close()

    except FileNotFoundError:
        print("\nO arquivo 'alunos.txt' não existe.")
        print("Nenhum aluno foi cadastrado ainda.")


def consultar_arquivo():
    if os.path.exists(ARQUIVO):
        print("\nO arquivo 'alunos.txt' foi criado.")
    else:
        print("\nO arquivo 'alunos.txt' ainda não foi criado.")


def menu():
    while True:
        print("\nsistema de alunos")
        print("1 - Cadastrar aluno")
        print("2 - Listar alunos")
        print("3 - Consultar se o arquivo foi criado")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_aluno()

        elif opcao == "2":
            listar_alunos()

        elif opcao == "3":
            consultar_arquivo()

        elif opcao == "4":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida!")


menu()
