# Lembrando que venda é uma lista:
# [codigo, nome, valor, dia, mes, ano]
def calcular_periodo(vendas: list, mes: int, ano: int) -> float:
    total = 0

    for v in vendas:
        if v[4] == mes and v[5] == ano:
            total += v[2]

    return total


def buscar_por_codigo(vendas: list, codigo: int) -> list | None:
    resultado = None

    for v in vendas:
        if v[0] == codigo:
            resultado = v
            break

    return resultado


# Lembrando que venda é uma lista:
# [codigo, nome, valor, dia, mes, ano]
def imprimir(venda):
    print(f"\nCódigo: {venda[0]}")
    print(f"Nome: {venda[1]}")
    print(f"Valor: R${venda[2]:.2f}")
    print(f"Data: {venda[3]}/{venda[4]}/{venda[5]}")
