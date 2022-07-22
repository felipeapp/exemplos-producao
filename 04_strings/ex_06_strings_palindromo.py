texto = input("Digite o texto: ")

caracteres_total = len(texto)
espacos_branco = texto.count(" ")
texto_sem_espacos = texto.replace(" ", "").lower()

tamanho = len(texto_sem_espacos)
palindromo = True
for i in range(tamanho // 2):
    if texto_sem_espacos[i] != texto_sem_espacos[tamanho - i - 1]:
        palindromo = False
        break

print(f"Quantidade de palavras: {espacos_branco + 1}.")
print(f"Caracteres contando com espaço: {caracteres_total}.")
print(f"Caracteres sem contar com espaço: {caracteres_total - espacos_branco}.")

if palindromo:
    print("O texto é um palíndromo!")
else:
    print("O texto não é um palíndromo!")
