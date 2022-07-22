"""
Use uma lista de listas para armazenar um conjunto de
produtos com seus preços e quantidades, simulando a ideia
de um carrinho de pedidos. O programa apresentará ao
usuário a opção de encerrar ou adicionar um novo produto.
Se ele escolher adicionar, o programa deve pedir o nome,
o preço e a quantiade do produto, caso ele escolha
encerrar, o programa mostrará a lista de produtos com
seus preços e o valor total do carrinho. O preço e a quantidade
do produto deve ser validado como sempre maior do que zero.
O nome do produto deve sempre ter três caracteres no mínimo.
"""

pedidos = []

while True:
    print(50 * "-")
    print("0 - Finalizar a compra")
    print("1 - Adicionar produto")
    opcao = int(input("Escolha sua opção: "))

    if opcao == 0:
        if pedidos:
            total = 0
            print(50 * "-")

            for nome, preco, quantidade in pedidos:
                valor = preco * quantidade
                total += valor
                print(f"{nome}: R${preco} x {quantidade}un = R${valor}")

            print(50 * "-")
            print(f"Total da compra: R${total}")
        else:
            print("Nenhum pedido encontrado!")

        break
    elif opcao == 1:
        while True:
            nome = input("Digite o nome: ")
            if len(nome) >= 3:
                break
            print("O nome deve ter pelo menos três caracteres!")

        while True:
            preco = float(input("Digite o preço: "))
            if preco > 0:
                break
            print("O preço deve ser maior que zero!")

        while True:
            quantidade = int(input("Digite a quantidade: "))
            if quantidade > 0:
                break
            print("A quantidade deve ser maior que zero!")

        pedidos.append([nome, preco, quantidade])
        print("Produdo adicionado com sucesso!")
    else:
        print("Opção inválida, tente novamete!")
