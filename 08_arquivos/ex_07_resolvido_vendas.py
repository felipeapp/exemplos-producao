# Solução anterior modelada para lista de listas
# [
#      codigo,     nome, valor, dia, mes,  ano
#     [   100, "Felipe", 99.99,  12,  12, 2022],
#     [   101,  "Maria", 50.99,   1,  10, 2022],
#     [   102,   "João",  9.99,   12, 10, 2022]
# ]
nome_arquivo = "vendas.csv"


def imprimir_venda(lista_campos):
    print("###")
    print(f"Código: {lista_campos[0]}")
    print(f"Nome: {lista_campos[1]}")
    print(f"Valor: R${lista_campos[2]}")
    print(f"Data: {lista_campos[3]}/{lista_campos[4]}/{lista_campos[5]}")


def buscar_por_codigo(codigo_busca):
    resultado = None

    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            campos = linha.strip().split(";")

            if codigo_busca == int(campos[0]):
                resultado = campos
                break

    return resultado


def main():
    while True:
        print(30 * "-")
        print("0 - Sair do programa")
        print("1 - Cadastrar uma venda")
        print("2 - Listar todas as vendas cadastradas")
        print("3 - Mostrar uma venda a partir de seu código")
        print("4 - Calcular o valor total das vendas em um mês do ano")
        opcao = int(input("Escolha sua opção: "))

        if opcao == 0:
            print("Finalizando programa...")
            break
        elif opcao == 1:
            codigo = int(input("Digite o código: "))
            venda = buscar_por_codigo(codigo)

            if venda is None:
                nome = input("Nome do cliente: ")
                valor = float(input("Valor da venda: "))
                dia = int(input("Digite o dia: "))
                mes = int(input("Digite o mês: "))
                ano = int(input("Digite o ano: "))

                with open(nome_arquivo, "a", encoding="utf-8") as arquivo:
                    arquivo.write(f"{codigo};{nome};{valor:.2f};{dia};{mes};{ano}\n")

                print("Cadastro da venda realizado com sucesso!")
            else:
                print("O código informado já está cadastrado para a venda:")
                imprimir_venda(venda)
        elif opcao == 2:
            with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
                for linha in arquivo:
                    imprimir_venda(linha.strip().split(";"))
        elif opcao == 3:
            codigo = int(input("Digite o código da venda: "))
            venda = buscar_por_codigo(codigo)

            if venda is None:
                print("O código informado não foi encontrado!")
            else:
                imprimir_venda(venda)
        elif opcao == 4:
            mes_busca = int(input("Digite o mês da busca: "))
            ano_busca = int(input("Digite o ano da busca: "))
            total = 0

            with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
                for linha in arquivo:
                    codigo, nome, valor, dia, mes, ano = linha.strip().split(";")

                    if mes_busca == int(mes) and ano_busca == int(ano):
                        total += float(valor)

            if total == 0:
                print("Não houve vendas no período!")
            else:
                print(f"O total de vendas para o período foi R${total:.2f}")
        else:
            print("Opção inválida, tente novamente!")


if __name__ == "__main__":
    with open(nome_arquivo, "a", encoding="utf-8"):
        pass

    main()
