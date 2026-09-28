def verificar_usuario(idade, renda, cadastro):
    
    if idade < 18:
        return "Usuário menor de idade"
    
    elif renda < 2000:
        return "Renda abaixo do limite"
    
    elif cadastro == "inativo":
        return "Cadastro inativo"
    
    else:
        return "Usuário aprovado"


idade = int(input("Digite a idade: "))
renda = float(input("Digite a renda: "))
cadastro = input("Digite a situação do cadastro (ativo/inativo): ")

resultado = verificar_usuario(idade, renda, cadastro)

print(resultado)
