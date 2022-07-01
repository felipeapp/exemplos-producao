num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# if num1 < num2:
#     menor = num1
# else:
#     menor = num2
menor = num1 if num1 < num2 else num2
mdc = 1

for i in range(menor, 1, -1):
    if num1 % i == 0 and num2 % i == 0:
        mdc = i
        break

print(f"O MDC entre {num1} e {num2} é {mdc}!")
