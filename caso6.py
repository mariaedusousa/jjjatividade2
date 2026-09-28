SENHA_CORRETA = "Escola@2026"
MAX_TENTATIVAS = 3

for tentativa in range(1, MAX_TENTATIVAS + 1):
    senha = input(f"Senha (tentativa {tentativa}/{MAX_TENTATIVAS}): ")
    if senha == SENHA_CORRETA:
        print("pode irrr!")
        break
    print("deu erradooo.")
else:
    print("acho q vc não é o dono, rala daqui.")
