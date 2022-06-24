quantidade = 0
maior = 0
somatorio = 0

while True:
    numero = int(input("Digite um inteiro positivo: "))

    if numero > 0:
        quantidade += 1
        somatorio += numero

        if numero > maior:
            maior = numero
    elif numero == 0:
        break

print(f"A quantidade de números digitados foi {quantidade}.")
print(f"O maior número digitado foi {maior}.")
print(f"A média aritmética dos números foi {somatorio / quantidade:.2f}.")
