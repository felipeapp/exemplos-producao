while True:
    limite = int(input("Digite o valor limite: "))

    if limite > 0:
        break

    print("Valor inválido, tente novamente!")

for c in range(0, limite + 1, 2):
    print(c)
