while True:
    limite = int(input("Digite o valor limite: "))

    if limite > 0:
        break

    print("Valor inválido, tente novamente!")

c = 0

while c <= limite:
    # if c % 2 == 0:
    #     print(c)
    print(c)
    c += 2
