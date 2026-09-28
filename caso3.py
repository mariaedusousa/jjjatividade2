aluno = []

while True:
    print("\n1. Armazenar aluno \n2. Consultar aluno \n")
    
    try:
        escolha = int(input("deseja consultar um aluno ou cadastrar? "))
        
        if escolha == 1:
            nome = str(input("Digite nome do aluno que você deseja cadastrar: "))
            aluno.append(nome)
            
            id_aut = len(aluno)
            print(f"cadastro com sucesso! Id é {id_aut}")
            
        elif escolha == 2:
            id = int(input("Informe o id do aluno que você quer: "))
            
            if id <= 0:
                print("Id inexistente ")
            elif (id - 1) >= len(aluno):
                print("nao existe aluno com esse id")
            else:
                print(f"o aluno na posição {id} é {aluno[id - 1]}")
            
        else:
            print("Opção inválida!")
            break
            
    except ValueError:
        print("Error! Digite apenas números")
