nomes = ["cris", "madu", "Meny", "ticole", "kikita", "bolinha"]

duplicados = []

for nome in nomes:
    if nomes.count(nome) > 1 and nome not in duplicados:
        duplicados.append(nome)

print("Nomes repetidos:", duplicados)
