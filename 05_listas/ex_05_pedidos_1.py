pedidos = [
    ["coxinha", 3.5, 10],
    ["coca-cola", 7.5, 3],
    ["pizza", 50.0, 2],
    ["pipoca", 2.5, 5],
    ["água mineral", 2.0, 10],
]

total = 0
print(50 * "-")

for nome, unitario, quantidade in pedidos:
    valor = unitario * quantidade
    total += valor
    print(f"{nome}: R${unitario} x {quantidade}un = R${valor}")

print(50 * "-")
print(f"Total dos pedidos: R${total}")
