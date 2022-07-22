nomes = ["Felipe", "Sara", "Vinícius", "Josué"]
print(nomes)

# Adiciona no final da lista
nomes.append("Jéssica")
nomes.append("Luana")
nomes.append("Batista")
print(nomes)

# Adiciona em uma posição específica
nomes.insert(1, "Syllas")
print(nomes)

# Remove a partir do elemento dado
nomes.remove("Syllas")
print(nomes)

# Remove a partir da posição
elem = nomes.pop()
print(f"Elemento removido: {elem}")
elem = nomes.pop(1)
print(f"Elemento removido: {elem}")
print(nomes)

# Retorna o índice a partir do elemento
print(nomes.index("Felipe"))
print(nomes.index("Josué"))

# Contar quantas vezes o elemento aparece
print(nomes.count("Vinícius"))
print(nomes.count("Sara"))

# Testa se o elemento existe ou não na lista
print("Vinícius" in nomes)
print("Sara" in nomes)
print("Sara" not in nomes)

# Ordenação da lista de forma crescente
nomes.sort()
print(nomes)

# Ordenação da lista de forma decrescente
nomes.sort(reverse=True)
print(nomes)

# Remove todos os elementos da lista
nomes.clear()
print(nomes)
