while True:
    quantidade = int(input("Digite a quantidade de alunos da turma: "))
    if quantidade > 0:
        break
    print("Quantidade inválida, tente novamente!")

contador = 0

while contador < quantidade:
    print(30 * "-")

    while True:
        nota1 = float(input(f"Digite a primeira nota do aluno {contador + 1}: "))
        if 0 <= nota1 <= 10:
            break
        print("Primeira nota inválida, tente novamente!")

    while True:
        nota2 = float(input(f"Digite a segunda nota do aluno {contador + 1}: "))
        if 0 <= nota2 <= 10:
            break
        print("Segunda nota inválida, tente novamente!")

    media = (nota1 + nota2) / 2
    print(f"A média foi {media:.2f}!")

    if media >= 6:
        print("O aluno está aprovado!")
    elif media < 2:
        print("O aluno está reprovado")
    else:
        print("O aluno está em recuperação!")

    contador += 1
