def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media


nota1 = float(input("primeira nota: "))
nota2 = float(input("segunda nota: "))

media = calcular_media(nota1, nota2)

print("A média é:", media)

resultado = media + 1

print("Média após adicionar 1 ponto:", resultado)
