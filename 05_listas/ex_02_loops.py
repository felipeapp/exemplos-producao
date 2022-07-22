nomes = ["Felipe", "Sara", "Vinícius", "Josué"]
print(nomes)

# Passar em todos os elementos usando while (prefira usar for)
i = 0
while i < len(nomes):
    print(nomes[i])
    i += 1

print(30 * "-")

# Usando for para passar em todos os elementos (forma 1)
for elem in nomes:
    print(elem)

print(30 * "-")

# Usando for para passar em todos os elementos (forma 2)
for i, e in enumerate(nomes):
    print(f"O índice {i} é {e}.")
