curso = "Engenharia de Produção"

# Deixa a primeira letra em maiúsculo e o resto minúsculo
print(curso.capitalize())

# Centraliza o texto
print(curso.center(50, "*"))
print(curso.center(30, "#"))
print(curso.center(50, " "))

# Alinha o texto a esquerda
print(curso.ljust(50, "*"))

# Alinha o texto a direita
print(curso.rjust(50, "*"))

# Conta quantas vezes aparece no texto
print(curso.count("e"))
print(curso.count("E"))
print(curso.count("de"))
print(curso.count("x"))

# Verifica se o valor existe no texto
print("de" in curso)
print("x" not in curso)
print("e" not in curso)

# Testa se o texto começa com um prefixo
print(curso.startswith("Engenharia"))
print(curso.startswith("e"))

# Testa se o texto termina com um sufixo
print(curso.endswith("Produção"))
print(curso.endswith("ão"))

# Retorna o índice do valor
print(curso.find("de"))
print(curso.find("x"))
print(curso.find("a"))
print(curso.rfind("a"))  # Da direita para a esquerda

# Gera um texto todo em minúsculo
print(curso.lower())

# Gera um texto todo em maiúsculo
print(curso.upper())

# Verifica se é maiúsculo
print("A".islower())
print("a".islower())

# Verifica se é minúsculo
print("A".isupper())
print("a".isupper())

# Realiza a remoção de caracteres das extremidades
print("***Engenharia***".strip("*"))
print("$$Engenharia$$$$$$".strip("$"))
print("* *Engenharia**$ *".strip("*$ "))
print("***Engenharia***".lstrip("*"))  # Apenas da esquerda
print("***Engenharia***".rstrip("*"))  # Apenas da direita

# Tamanho da string
print(len(curso))
print(len("Programar é legal que demais!"))
print(len("Fácil, fácil e divertido!"))

# Contatenação de strings usando +
print("O curso de " + curso + " é muito legal!")
texto = ""
texto += "João, "
texto += "Ana, "
texto += "Carla!"
print(texto)
