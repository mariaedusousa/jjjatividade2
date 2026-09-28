try: 
    nota = float(input("informe a nota guru: "))

    if nota < 0:
      print("apenas numeros positivosss, ja viu nota negativa animal")
    elif nota > 10:
      print("rapaz, so de 0 a 10")
    else:
       if nota >= 7:
        print("passouuuuu!")
       elif nota >= 5:
        print("hiiiii recuperação riririr.")
       else:
        print("nam volte pra casa logo(reprovado)")


except ValueError:
  print("nao sabia q nota tinha letra agora.")
