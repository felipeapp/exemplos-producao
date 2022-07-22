composta = [[3, 2, 1], [3, 0, 7], [0, 6, 3]]
print(composta)

print(40 * "-")
print(composta[1])
print(composta[1][2])
print(composta[1:3])
print(len(composta))
print(40 * "-")

for lista in composta:
    for elemento in lista:
        print(elemento, end=" ")
    print()
