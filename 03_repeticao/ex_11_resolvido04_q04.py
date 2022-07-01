while True:
    print(40 * "-")
    nome = input("Digite seu nome: ")
    data = input("Digite sua data de nascimento: ")
    celular = input("Digite seu número de celular: ")

    print(40 * "-")
    print("Você digitou as seguintes informações:")
    print(f"Nome: {nome}.")
    print(f"Data de Nascimento: {data}.")
    print(f"Número de Celular: {celular}.")

    while True:
        resposta = input("Os dados estão corretos (sim/não)? ")
        if resposta == "sim" or resposta == "não":
            break
        print("Resposta inválida, tente novamente!")

    if resposta == "sim":
        print("Obrigado pelas informações!")
        break
