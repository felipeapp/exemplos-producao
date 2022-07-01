joao = 0
severina = 0
nulo = 0
branco = 0

while True:
    print(40 * "-")
    print("As opções são:")
    print("0. Finalizar votação")
    print("1. Votar em João Rodrigues")
    print("2. Votar em Severina da Luz")
    print("3. Nulo")
    print("4. Branco")
    opcao = int(input("Entre com o seu voto: "))

    if opcao == 0:
        print("Votação finalizada!")
        break
    elif opcao == 1:
        joao += 1
    elif opcao == 2:
        severina += 1
    elif opcao == 3:
        nulo += 1
    elif opcao == 4:
        branco += 1
    else:
        print("Opção inválida, tente novamente!")

total = joao + severina + nulo + branco

print(40 * "-")
print(f"Total de votos: {total}.")
print(f"Número de votos em João Rodrigues: {joao}.")
print(f"Número de votos em Severina da Luz: {severina}.")
print(f"Número de votos nulos: {nulo}.")
print(f"Número de votos brancos: {branco}.")
print(f"Porcentagem de votos nulos: {100 * nulo / total:.2f}%.")
print(f"Porcentagem de votos brancos: {100 * branco / total:.2f}%.")

if joao > severina:
    print("O vencedor foi João Rodrigues!")
elif severina > joao:
    print("A vencedora foi Severina da Luz!")
else:
    print("Houve empate na votação!")
