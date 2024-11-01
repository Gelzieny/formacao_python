"""Principais métodos do tipo texto"""

# Declaração
nome = 'Gelzieny'
sobrenome = 'R. Martins'
idade = 30
frase = "python e divertido!"
texto = "  Ola, Mundo!  "

#  capitalize(): Converte a primeira letra da string para maiúscula.
print(f"Converte a primeira letra em maiuscula: {frase.capitalize()}")

# title(): Converte a primeira letra de cada palavra para maiúscula.
print(f"Converte a primeira letra de cada palavra para maiuscula: {frase.title()}")


# strip(): Remove espaços em branco do início e do final da string.
print(f"Remove espaços em branco do inicio e do final: {texto.strip()}")

# lstrip(): Remove espaços em branco apenas do início.
print(f"Remove espaços em branco apenas do inicio: {texto.lstrip()}")

# rstrip(): Remove espaços em branco apenas do final.
print(f"Remove espacos em branco apenas do final: {texto.rstrip()}")

# join(iterável) => Junta elementos de um iterável (como lista) em uma única string
frutas = ["maca", "banana", "uva"]
print(", ".join(frutas))

# startswith(): Verifica se a string começa com a substring fornecida.
print(texto.startswith("python"))

# endswith(): Verifica se a string termina com a substring fornecida.
print(texto.endswith("python"))